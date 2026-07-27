import os
import time
import json
import pickle
import numpy as np
import tensorflow as tf
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# Hardware-Aware Settings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
tf.get_logger().setLevel('ERROR')

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

def get_model(model_type, task, input_shape, num_classes=None):
    """Model Factory for MLP and CNN, Binary and Multiclass."""
    from tensorflow.keras.layers import Dense, Dropout, BatchNormalization, Conv1D, MaxPooling1D, Flatten, Input
    from tensorflow.keras.regularizers import l2
    
    model = tf.keras.Sequential()
    model.add(Input(shape=input_shape))
    
    if model_type == 'mlp':
        if task == 'binary':
            model.add(Dense(256, activation='relu', kernel_regularizer=l2(1e-4)))
            model.add(BatchNormalization())
            model.add(Dropout(0.3))
            model.add(Dense(128, activation='relu', kernel_regularizer=l2(1e-4)))
            model.add(Dropout(0.3))
            model.add(Dense(64, activation='relu'))
            model.add(Dropout(0.2))
            model.add(Dense(1, activation='sigmoid'))
        else: # multiclass
            model.add(Dense(512, activation='relu', kernel_regularizer=l2(1e-4)))
            model.add(BatchNormalization())
            model.add(Dropout(0.4))
            model.add(Dense(256, activation='relu', kernel_regularizer=l2(1e-4)))
            model.add(Dropout(0.4))
            model.add(Dense(128, activation='relu'))
            model.add(Dropout(0.3))
            model.add(Dense(num_classes, activation='softmax'))
            
    elif model_type == 'cnn':
        if task == 'binary':
            model.add(Conv1D(64, 3, padding='same', activation='relu'))
            model.add(BatchNormalization())
            model.add(MaxPooling1D(2))
            model.add(Conv1D(32, 3, padding='same', activation='relu'))
            model.add(BatchNormalization())
            model.add(MaxPooling1D(2))
            model.add(Flatten())
            model.add(Dense(128, activation='relu'))
            model.add(Dropout(0.4))
            model.add(Dense(1, activation='sigmoid'))
        else: # multiclass
            model.add(Conv1D(128, 3, padding='same', activation='relu'))
            model.add(BatchNormalization())
            model.add(MaxPooling1D(2))
            model.add(Conv1D(64, 3, padding='same', activation='relu'))
            model.add(BatchNormalization())
            model.add(MaxPooling1D(2))
            model.add(Flatten())
            model.add(Dense(128, activation='relu'))
            model.add(Dropout(0.4))
            model.add(Dense(num_classes, activation='softmax'))
            
    return model

class ProximalModel(tf.keras.Model):
    def __init__(self, model_base, global_weights_initial, mu=0.01):
        super().__init__()
        self.model = model_base
        # CRITICAL: Store only trainable weights for proximal term
        self.global_trainable_weights = [
            tf.convert_to_tensor(w, dtype=tf.float32) 
            for w in self._extract_trainable_weights(model_base, global_weights_initial)
        ]
        self.mu = mu
    
    def _extract_trainable_weights(self, model, all_weights):
        """Extract only the weights that correspond to trainable variables."""
        trainable_indices = []
        all_weight_shapes = [w.shape for w in model.get_weights()]
        trainable_shapes = [(v.name, v.shape) for v in model.trainable_weights]
        
        idx = 0
        for name, shape in trainable_shapes:
            while idx < len(all_weight_shapes):
                if all_weight_shapes[idx] == shape:
                    trainable_indices.append(idx)
                    idx += 1
                    break
                idx += 1
        
        return [all_weights[i] for i in trainable_indices]
    
    def call(self, inputs):
        return self.model(inputs)
    
    def train_step(self, data):
        x, y = data
        with tf.GradientTape() as tape:
            y_pred = self.model(x, training=True)
            local_loss = self.compiled_loss(y, y_pred, regularization_losses=self.model.losses)
            proximal_term = 0.0
            for local_w, global_w in zip(self.model.trainable_weights, self.global_trainable_weights):
                proximal_term += tf.reduce_sum(tf.square(local_w - global_w))
            total_loss = local_loss + (self.mu / 2.0) * proximal_term
        gradients = tape.gradient(total_loss, self.model.trainable_weights)
        self.optimizer.apply_gradients(zip(gradients, self.model.trainable_weights))
        self.compiled_metrics.update_state(y, y_pred)
        return {m.name: m.result() for m in self.metrics}

def compile_model(model, task):
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.0005)
    if task == 'binary':
        loss = 'binary_crossentropy'
    else:
        loss = 'sparse_categorical_crossentropy'
    model.compile(optimizer=optimizer, loss=loss, metrics=['accuracy'])
    return model

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

def run_federated_scenario(X_train, y_train, X_test, y_test, num_clients, alpha, model_type, task, strategy, mu=None, seed=42):
    print(f"\n--- Running {task.upper()} | {model_type.upper()} | {strategy} | Alpha: {alpha} ---")
    start_time = time.time()
    
    # 1. Partition Data
    client_datasets = partition_dirichlet(X_train, y_train, num_clients, alpha, seed)
    
    # 2. Reshape for CNN if needed
    if model_type == 'cnn':
        input_shape = (X_train.shape[1], 1)
        X_test_run = X_test.reshape(-1, X_train.shape[1], 1)
        for i in range(num_clients):
            X_c, y_c = client_datasets[i]
            client_datasets[i] = (X_c.reshape(-1, X_train.shape[1], 1), y_c)
    else:
        input_shape = (X_train.shape[1],)
        X_test_run = X_test

    num_classes = len(np.unique(y_train)) if task == 'multiclass' else None
    
    # Initialize global model
    global_model = get_model(model_type, task, input_shape, num_classes)
    global_weights = global_model.get_weights()
    
    # Federated rounds
    num_rounds = 20
    batch_size = 512
    local_epochs = 1
    
    total_samples = sum(len(client_datasets[i][0]) for i in range(num_clients))
    
    for r in range(num_rounds):
        new_weights_list = []
        
        for i in range(num_clients):
            X_c, y_c = client_datasets[i]
            
            # Local model
            local_base_model = get_model(model_type, task, input_shape, num_classes)
            local_base_model.set_weights(global_weights)
            
            if strategy.startswith('FedProx'):
                model_to_train = ProximalModel(local_base_model, global_weights, mu=mu)
            else:
                model_to_train = local_base_model
                
            model_to_train = compile_model(model_to_train, task)
            
            # Train
            model_to_train.fit(X_c, y_c, batch_size=batch_size, epochs=local_epochs, verbose=0)
            
            if strategy.startswith('FedProx'):
                new_weights_list.append(model_to_train.model.get_weights())
            else:
                new_weights_list.append(model_to_train.get_weights())
                
        # Aggregate (Weighted FedAvg)
        weighted_weights = []
        for weights_group in zip(*new_weights_list):
            avg = sum(w * (len(client_datasets[i][0]) / total_samples) for i, w in enumerate(weights_group))
            weighted_weights.append(avg)
            
        global_weights = weighted_weights
        global_model.set_weights(global_weights)
        
        # Evaluate
        eval_model = get_model(model_type, task, input_shape, num_classes)
        eval_model.set_weights(global_weights)
        eval_model = compile_model(eval_model, task)
        
        loss, acc = eval_model.evaluate(X_test_run, y_test, verbose=0)
        print(f"Round {r+1}/20 - Loss: {loss:.4f}, Acc: {acc:.4f}")
        
    # Final evaluation for metrics
    y_pred_prob = eval_model.predict(X_test_run, verbose=0)
    acc, prec, rec, f1, auc, ws = calculate_metrics(y_test, y_pred_prob, task)
    
    end_time = time.time()
    duration = end_time - start_time
    print(f"Scenario completed in {duration:.2f}s - Final WS: {ws:.4f}")
    
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
    results = []
    
    binary_path = 'EDA/processed_artifacts/binary_preprocessed.pkl'
    multiclass_path = 'EDA/processed_artifacts/multiclass_preprocessed.pkl'
    
    datasets = {
        'binary': load_dataset(binary_path),
        'multiclass': load_dataset(multiclass_path)
    }
    
    alphas = [0.3, 5.0]
    models = ['mlp', 'cnn']
    
    for task, data in datasets.items():
        if data is None:
            continue
            
        X_train, X_test, y_train, y_test = data['X_train'], data['X_test'], data['y_train'], data['y_test']
        
        # Ensure y is proper shape
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
    print("\n=== THESIS BENCHMARK RESULTS ===")
    print(f"{'Task':<10} | {'Model':<7} | {'Strategy':<16} | {'Alpha':<5} | {'Acc':<7} | {'Prec':<7} | {'Rec':<7} | {'F1':<7} | {'AUC':<7} | {'WS':<7}")
    print("-" * 95)
    for r in results:
        print(f"{r['Task']:<10} | {r['Model']:<7} | {r['Strategy']:<16} | {r['Alpha']:<5} | {r['Acc']:.4f}  | {r['Prec']:.4f}  | {r['Rec']:.4f}  | {r['F1']:.4f}  | {r['AUC']:.4f}  | {r['WS']:.4f}")

    # Save to JSON
    with open('thesis_benchmark_results.json', 'w') as f:
        json.dump(results, f, indent=4)
        
    print("\nBenchmark complete. Results saved to thesis_benchmark_results.json")

if __name__ == '__main__':
    main()
