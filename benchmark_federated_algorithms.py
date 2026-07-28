import os
import time
import json
import pickle
import copy
import gc
import numpy as np

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# Hardware-Aware Settings
# Disable cuDNN to avoid CUDNN_STATUS_SUBLIBRARY_VERSION_MISMATCH with TF libs
torch.backends.cudnn.enabled = False
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {device}")

# Global configuration (can be overridden by --quick flag)
NUM_ROUNDS = 20

def load_dataset(filepath):
    """Load dataset from pickle file."""
    if not os.path.exists(filepath):
        print(f"Warning: Dataset not found at {filepath}")
        return None
    with open(filepath, 'rb') as f:
        data = pickle.load(f)
    return data

def partition_dirichlet(X, y, num_clients, alpha, seed=42):
    """
    Partition the dataset using Dirichlet distribution.
    Uses a seed to ensure exact same partitions for fairness in comparison.
    """
    np.random.seed(seed)
    num_classes = len(np.unique(y))
    client_indices = [[] for _ in range(num_clients)]
    
    for c in range(num_classes):
        idx_c = np.where(y == c)[0]
        np.random.shuffle(idx_c)
        
        # Dirichlet distribution for the current class over clients
        proportions = np.random.dirichlet(np.repeat(alpha, num_clients))
        # Ensure minimum of 1 sample per client for each class if possible, or just distribute
        proportions = np.array([p * (len(idx_c) < num_clients and p == max(proportions) or 1) for p in proportions])
        proportions = proportions / proportions.sum()
        
        splits = (np.cumsum(proportions) * len(idx_c)).astype(int)[:-1]
        splits = np.split(idx_c, splits)
        
        for i in range(num_clients):
            client_indices[i].extend(splits[i])
            
    client_datasets = []
    for i in range(num_clients):
        idx = np.array(client_indices[i])
        np.random.shuffle(idx)
        client_datasets.append((X[idx], y[idx]))
        
    return client_datasets

class MLP(nn.Module):
    def __init__(self, input_features, num_classes, task='binary'):
        super(MLP, self).__init__()
        out_features = 1 if task == 'binary' else num_classes
        self.net = nn.Sequential(
            nn.Linear(input_features, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(64, out_features)
        )

    def forward(self, x):
        return self.net(x)

class CNN1D(nn.Module):
    def __init__(self, input_features, num_classes, task='binary'):
        super(CNN1D, self).__init__()
        out_features = 1 if task == 'binary' else num_classes
        
        self.features = nn.Sequential(
            nn.Conv1d(1, 64, kernel_size=3, padding=1),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.MaxPool1d(2),
            nn.Conv1d(64, 32, kernel_size=3, padding=1),
            nn.BatchNorm1d(32),
            nn.ReLU(),
            nn.MaxPool1d(2)
        )
        
        # dummy pass to get flattened shape dynamically
        dummy = torch.zeros(1, 1, input_features)
        dummy_out = self.features(dummy)
        flat_size = dummy_out.view(1, -1).size(1)
        
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(flat_size, 128),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(128, out_features)
        )

    def forward(self, x):
        # x shape: (N, features)
        x = x.unsqueeze(1) # (N, 1, features)
        x = self.features(x)
        x = self.classifier(x)
        return x

def calculate_metrics(y_true, y_pred_prob, task):
    if task == 'binary':
        y_pred = (y_pred_prob > 0.5).astype(int)
        acc = accuracy_score(y_true, y_pred)
        prec = precision_score(y_true, y_pred, zero_division=0)
        rec = recall_score(y_true, y_pred, zero_division=0)
        f1 = f1_score(y_true, y_pred, zero_division=0)
        try:
            auc = roc_auc_score(y_true, y_pred_prob)
        except ValueError:
            auc = 0.5
    else:
        y_pred = np.argmax(y_pred_prob, axis=1)
        acc = accuracy_score(y_true, y_pred)
        prec = precision_score(y_true, y_pred, average='weighted', zero_division=0)
        rec = recall_score(y_true, y_pred, average='weighted', zero_division=0)
        f1 = f1_score(y_true, y_pred, average='weighted', zero_division=0)
        try:
            auc = roc_auc_score(y_true, y_pred_prob, multi_class='ovr', average='weighted')
        except ValueError:
            auc = 0.5
            
    ws = 0.20 * acc + 0.20 * prec + 0.20 * rec + 0.20 * f1 + 0.20 * auc
    return acc, prec, rec, f1, auc, ws

def train_client(model, global_model, train_loader, task, strategy, mu, epochs=1):
    model.train()
    optimizer = optim.Adam(model.parameters(), lr=0.0005, weight_decay=1e-4)
    criterion = nn.BCEWithLogitsLoss() if task == 'binary' else nn.CrossEntropyLoss()
    
    if global_model is not None:
        global_model.eval()
        
    for ep in range(epochs):
        for x_batch, y_batch in train_loader:
            x_batch = x_batch.to(device)
            y_batch = y_batch.to(device)
            
            optimizer.zero_grad()
            outputs = model(x_batch)
            
            if task == 'binary':
                outputs = outputs.view(-1)
                loss = criterion(outputs, y_batch.view(-1).float())
            else:
                loss = criterion(outputs, y_batch.long())
                
            if strategy.startswith('FedProx') and global_model is not None:
                proximal_term = 0.0
                for w, w_t in zip(model.parameters(), global_model.parameters()):
                    proximal_term += (w - w_t).norm(2) ** 2
                loss += (mu / 2) * proximal_term
                
            loss.backward()
            optimizer.step()

def evaluate_model(model, loader, task):
    model.eval()
    y_true = []
    y_pred_prob = []
    criterion = nn.BCEWithLogitsLoss() if task == 'binary' else nn.CrossEntropyLoss()
    total_loss = 0.0
    
    with torch.no_grad():
        for x_batch, y_batch in loader:
            x_batch = x_batch.to(device)
            y_batch = y_batch.to(device)
            
            outputs = model(x_batch)
            
            if task == 'binary':
                outputs = outputs.view(-1)
                loss = criterion(outputs, y_batch.view(-1).float())
                probs = torch.sigmoid(outputs)
                y_pred_prob.extend(probs.cpu().numpy())
            else:
                loss = criterion(outputs, y_batch.long())
                probs = torch.softmax(outputs, dim=1)
                y_pred_prob.extend(probs.cpu().numpy())
                
            total_loss += loss.item() * x_batch.size(0)
            y_true.extend(y_batch.cpu().numpy())
            
    avg_loss = total_loss / len(y_true)
    y_true = np.array(y_true)
    y_pred_prob = np.array(y_pred_prob)
    
    if task == 'binary':
        y_true = y_true.reshape(-1)
        
    acc, prec, rec, f1, auc, ws = calculate_metrics(y_true, y_pred_prob, task)
    return avg_loss, acc, prec, rec, f1, auc, ws, y_pred_prob

def run_federated_scenario(X_train, y_train, X_test, y_test, num_clients, alpha, model_type, task, strategy, mu=None, seed=42):
    print(f"\n--- Running {task.upper()} | {model_type.upper()} | {strategy} | Alpha: {alpha} ---")
    start_time = time.time()
    
    # Partition Data
    client_datasets = partition_dirichlet(X_train, y_train, num_clients, alpha, seed)
    
    input_shape = X_train.shape[1]
    num_classes = len(np.unique(y_train)) if task == 'multiclass' else 2
    
    # Create DataLoaders
    batch_size = 512
    client_loaders = []
    for i in range(num_clients):
        X_c, y_c = client_datasets[i]
        dataset = TensorDataset(torch.tensor(X_c, dtype=torch.float32), 
                                torch.tensor(y_c, dtype=torch.long if task=='multiclass' else torch.float32))
        client_loaders.append(DataLoader(dataset, batch_size=batch_size, shuffle=True))
        
    test_dataset = TensorDataset(torch.tensor(X_test, dtype=torch.float32), 
                                 torch.tensor(y_test, dtype=torch.long if task=='multiclass' else torch.float32))
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    
    total_samples = sum(len(cd[0]) for cd in client_datasets)
    client_weights = [len(cd[0]) / total_samples for cd in client_datasets]
    
    # Initialize global model
    ModelClass = MLP if model_type == 'mlp' else CNN1D
    global_model = ModelClass(input_shape, num_classes, task).to(device)
    
    num_rounds = NUM_ROUNDS
    local_epochs = 1
    
    for r in range(num_rounds):
        new_state_dicts = []
        
        for i in range(num_clients):
            local_model = ModelClass(input_shape, num_classes, task).to(device)
            local_model.load_state_dict(global_model.state_dict())
            
            train_client(local_model, global_model, client_loaders[i], task, strategy, mu, epochs=local_epochs)
            
            new_state_dicts.append(copy.deepcopy(local_model.state_dict()))
            
            del local_model
            torch.cuda.empty_cache()
            gc.collect()
            
        # FedAvg Aggregation
        avg_state_dict = copy.deepcopy(new_state_dicts[0])
        for key in avg_state_dict.keys():
            avg_state_dict[key] = avg_state_dict[key] * client_weights[0]
            for i in range(1, num_clients):
                avg_state_dict[key] += new_state_dicts[i][key] * client_weights[i]
                
        global_model.load_state_dict(avg_state_dict)
        
        # Free memory of new_state_dicts
        del new_state_dicts
        torch.cuda.empty_cache()
        gc.collect()
        
        # Evaluate
        loss, acc, prec, rec, f1, auc, ws, _ = evaluate_model(global_model, test_loader, task)
        print(f"Round {r+1}/{num_rounds} - Loss: {loss:.4f}, Acc: {acc:.4f}")
        
    # Final eval metrics
    _, acc, prec, rec, f1, auc, ws, y_pred_prob = evaluate_model(global_model, test_loader, task)
    
    end_time = time.time()
    duration = end_time - start_time
    print(f"Scenario completed in {duration:.2f}s - Final WS: {ws:.4f}")
    
    del global_model
    torch.cuda.empty_cache()
    gc.collect()
    
    return {
        'Task': task.capitalize(),
        'Model': model_type.upper(),
        'Strategy': strategy,
        'Alpha': alpha,
        'Acc': acc,
        'Prec': prec,
        'Rec': rec,
        'F1': f1,
        'AUC': auc,
        'WS': ws,
        'Duration_s': duration
    }

def main():
    import argparse
    parser = argparse.ArgumentParser(description='NIDS-FL Thesis Benchmark PyTorch')
    parser.add_argument('--quick', action='store_true', help='Quick mode: 3 rounds, binary MLP only')
    args = parser.parse_args()

    results = []
    
    binary_path = 'EDA/processed_artifacts/binary_preprocessed.pkl'
    multiclass_path = 'EDA/processed_artifacts/multiclass_preprocessed.pkl'
    
    datasets = {
        'binary': load_dataset(binary_path),
    }
    if not args.quick:
        datasets['multiclass'] = load_dataset(multiclass_path)
    
    alphas = [0.3, 5.0]
    models = ['mlp'] if args.quick else ['mlp', 'cnn']
    
    global NUM_ROUNDS
    if args.quick:
        NUM_ROUNDS = 3
    
    for task, data in datasets.items():
        if data is None:
            continue
            
        X_train, X_test, y_train, y_test = data['X_train'], data['X_test'], data['y_train'], data['y_test']
        
        # Ensure y is proper shape (1D for both binary and multiclass in PyTorch, but BCE needs float and CE needs long)
        if len(y_train.shape) > 1 and y_train.shape[1] > 1:
            y_train = np.argmax(y_train, axis=1)
            y_test = np.argmax(y_test, axis=1)
            
        for alpha in alphas:
            for model_type in models:
                # FedAvg
                res_avg = run_federated_scenario(X_train, y_train, X_test, y_test, 5, alpha, model_type, task, 'FedAvg', seed=42)
                results.append(res_avg)
                
                # FedProx mu=0.01
                res_prox1 = run_federated_scenario(X_train, y_train, X_test, y_test, 5, alpha, model_type, task, 'FedProx μ=0.01', mu=0.01, seed=42)
                results.append(res_prox1)
                
                # FedProx mu=0.001
                res_prox2 = run_federated_scenario(X_train, y_train, X_test, y_test, 5, alpha, model_type, task, 'FedProx μ=0.001', mu=0.001, seed=42)
                results.append(res_prox2)

    # Print clean table
    print("\n=== THESIS BENCHMARK RESULTS (PYTORCH) ===")
    print(f"{'Task':<10} | {'Model':<7} | {'Strategy':<16} | {'Alpha':<5} | {'Acc':<7} | {'Prec':<7} | {'Rec':<7} | {'F1':<7} | {'AUC':<7} | {'WS':<7}")
    print("-" * 95)
    for r in results:
        print(f"{r['Task']:<10} | {r['Model']:<7} | {r['Strategy']:<16} | {r['Alpha']:<5} | {r['Acc']:.4f}  | {r['Prec']:.4f}  | {r['Rec']:.4f}  | {r['F1']:.4f}  | {r['AUC']:.4f}  | {r['WS']:.4f}")

    # Save to JSON
    with open('thesis_benchmark_results_pytorch.json', 'w') as f:
        json.dump(results, f, indent=4)
        
    print("\nBenchmark complete. Results saved to thesis_benchmark_results_pytorch.json")

if __name__ == '__main__':
    main()
