import os
import sys
import pickle
import numpy as np
import tensorflow as tf
import optuna
from pathlib import Path
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import time

# Suppress TF logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
tf.get_logger().setLevel('ERROR')

sys.path.append(os.path.abspath('FL_TensorF_Flower_PROX'))
from task import ProximalModel, get_model_by_type
from utils import split_data_non_iid_label

def evaluate_metrics(y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, zero_division=0)
    rec = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)
    return acc, prec, rec, f1

def simulate_fl(X_train, y_train, X_test, y_test, num_clients=3, num_rounds=3, local_epochs=1, batch_size=256, alpha=0.3, strategy='FedAvg', mu=0.01, lr=0.001):
    print(f"[{strategy} | Alpha={alpha}] Partitioning data...")
    client_datasets = split_data_non_iid_label(X_train, y_train, num_clients, alpha=alpha)
    
    input_shape = X_train.shape[1]
    global_model = get_model_by_type('mlp_binary', input_shape=input_shape, learning_rate=lr)
    global_weights = global_model.get_weights()
    
    start_time = time.time()
    
    for round_num in range(1, num_rounds + 1):
        # print(f"  Round {round_num}/{num_rounds} running...")
        new_weights_list = []
        for client_id in range(num_clients):
            X_local, y_local = client_datasets[client_id]
            base_model = get_model_by_type('mlp_binary', input_shape=input_shape, learning_rate=lr)
            base_model.set_weights(global_weights)
            
            if strategy == 'FedProx':
                model_to_train = ProximalModel(base_model, global_weights, mu=mu)
            else:
                model_to_train = base_model
                
            model_to_train.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=lr), 
                                   loss='binary_crossentropy', metrics=['accuracy'])
            model_to_train.fit(X_local, y_local, epochs=local_epochs, batch_size=batch_size, verbose=0)
            
            if strategy == 'FedProx':
                new_weights_list.append(model_to_train.model.get_weights())
            else:
                new_weights_list.append(model_to_train.get_weights())
                
        # Aggregate
        global_weights = [np.mean(w, axis=0) for w in zip(*new_weights_list)]
        global_model.set_weights(global_weights)
        
    duration = time.time() - start_time
    
    # Evaluate
    y_pred_prob = global_model.predict(X_test, verbose=0)
    y_pred = (y_pred_prob > 0.5).astype(int).flatten()
    
    acc, prec, rec, f1 = evaluate_metrics(y_test, y_pred)
    
    print(f"  -> Acc: {acc:.4f} | Prec: {prec:.4f} | Rec: {rec:.4f} | F1: {f1:.4f} (Time: {duration:.1f}s)")
    return {"strategy": strategy, "alpha": alpha, "accuracy": acc, "precision": prec, "recall": rec, "f1": f1, "duration": duration}

if __name__ == "__main__":
    print("="*70)
    print("PHASE 1: OPTUNA BAYESIAN OPTIMIZATION (Hardware Aware)")
    print("="*70)
    
    data_path = Path('EDA/processed_artifacts/binary_preprocessed.pkl')
    with open(data_path, 'rb') as f:
        data = pickle.load(f)
    
    # Use a small subset to find hyperparameters quickly without burning the R5 3500 CPU
    X_train_sub, y_train_sub = data['X_train'][:30000], data['y_train'][:30000]
    X_test_sub, y_test_sub = data['X_test'][:10000], data['y_test'][:10000]
    
    def objective(trial):
        lr = trial.suggest_float("lr", 1e-4, 5e-3, log=True)
        batch_size = trial.suggest_categorical("batch_size", [256, 512])
        local_epochs = trial.suggest_int("local_epochs", 1, 2)
        mu = trial.suggest_float("mu", 0.005, 0.05, log=True)
        
        # We tune using FedProx with moderate heterogeneity
        res = simulate_fl(X_train_sub, y_train_sub, X_test_sub, y_test_sub, 
                          num_clients=3, num_rounds=2, local_epochs=local_epochs, 
                          batch_size=batch_size, alpha=0.5, strategy='FedProx', mu=mu, lr=lr)
        return res['accuracy']

    # Disable optuna massive logging
    optuna.logging.set_verbosity(optuna.logging.WARNING)
    study = optuna.create_study(direction="maximize")
    print("Running 5 Optuna trials to find optimal hyperparameters...")
    study.optimize(objective, n_trials=5)
    
    best_params = study.best_params
    print(f"✓ Optuna found Best Params: {best_params}")
    
    print("\n" + "="*70)
    print("PHASE 2: APPLE-TO-APPLE FULL COMPARISON")
    print("="*70)
    print("Running on FULL DATASET using Optuna's parameters.")
    
    # Full dataset
    X_train_full, y_train_full = data['X_train'], data['y_train']
    X_test_full, y_test_full = data['X_test'], data['y_test']
    
    # Common settings for apple-to-apple
    common_args = {
        'X_train': X_train_full, 'y_train': y_train_full,
        'X_test': X_test_full, 'y_test': y_test_full,
        'num_clients': 3,
        'num_rounds': 5,          # 5 rounds for the full benchmark
        'local_epochs': best_params['local_epochs'],
        'batch_size': best_params['batch_size'],
        'lr': best_params['lr'],
        'mu': best_params['mu']
    }
    
    results = []
    print("\n[Scenario 1] High Heterogeneity (Non-IID Alpha=0.3)")
    results.append(simulate_fl(**common_args, alpha=0.3, strategy='FedAvg'))
    results.append(simulate_fl(**common_args, alpha=0.3, strategy='FedProx'))
    
    print("\n[Scenario 2] Low Heterogeneity (IID-like Alpha=5.0)")
    results.append(simulate_fl(**common_args, alpha=5.0, strategy='FedAvg'))
    results.append(simulate_fl(**common_args, alpha=5.0, strategy='FedProx'))
    
    print("\n" + "="*70)
    print("FINAL APPLE-TO-APPLE RESULT")
    print("="*70)
    print(f"Host Config Optimized: Ryzen 5 3500 | 32GB RAM | GPU Offloaded (CPU Mode)")
    print(f"Params Used: Rounds=5, Epochs={best_params['local_epochs']}, Batch={best_params['batch_size']}, LR={best_params['lr']:.5f}, Mu={best_params['mu']:.4f}\n")
    
    print(f"{'Strategy':<10} | {'Alpha':<5} | {'Accuracy':<10} | {'F1-Score':<10} | {'Time (s)':<10}")
    print("-" * 55)
    for r in results:
        print(f"{r['strategy']:<10} | {r['alpha']:<5} | {r['accuracy']:.4f}     | {r['f1']:.4f}     | {r['duration']:.1f}s")
