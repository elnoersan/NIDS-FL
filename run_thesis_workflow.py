import os
import sys
import pickle
import numpy as np
import tensorflow as tf
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

def simulate_fl(X_train, y_train, X_test, y_test, num_clients=3, num_rounds=2, local_epochs=1, batch_size=256, alpha=0.3, strategy='FedAvg', mu=0.01):
    print(f"\n[{strategy} | Alpha={alpha}] Partitioning data...")
    client_datasets = split_data_non_iid_label(X_train, y_train, num_clients, alpha=alpha)
    
    input_shape = X_train.shape[1]
    global_model = get_model_by_type('mlp_binary', input_shape=input_shape)
    global_weights = global_model.get_weights()
    
    start_time = time.time()
    
    for round_num in range(1, num_rounds + 1):
        print(f"  Round {round_num}/{num_rounds} running...")
        new_weights_list = []
        for client_id in range(num_clients):
            X_local, y_local = client_datasets[client_id]
            base_model = get_model_by_type('mlp_binary', input_shape=input_shape)
            base_model.set_weights(global_weights)
            
            if strategy == 'FedProx':
                model_to_train = ProximalModel(base_model, global_weights, mu=mu)
            else:
                model_to_train = base_model
                
            model_to_train.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), 
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
    return {"strategy": strategy, "alpha": alpha, "accuracy": acc, "precision": prec, "recall": rec, "f1": f1}

if __name__ == "__main__":
    print("="*70)
    print("THESIS WORKFLOW EXECUTION: FEDERATED LEARNING FOR NIDS")
    print("="*70)
    
    # 1. PREPROCESSING
    print("\n[Phase 1] Data Preprocessing & Loading")
    data_path = Path('EDA/processed_artifacts/binary_preprocessed.pkl')
    with open(data_path, 'rb') as f:
        data = pickle.load(f)
    print(f"✓ Loaded {data['X_train'].shape[0]} training samples and {data['X_test'].shape[0]} test samples.")
    print(f"✓ Features optimized to {data['X_train'].shape[1]} security-aware dimensions.")
    
    # Limit dataset size slightly for fast end-to-end execution
    limit = 50000
    X_train, y_train = data['X_train'][:limit], data['y_train'][:limit]
    X_test, y_test = data['X_test'][:10000], data['y_test'][:10000]
    
    results = []
    # 2. EXPERIMENT 1: FedAvg with high heterogeneity
    results.append(simulate_fl(X_train, y_train, X_test, y_test, alpha=0.3, strategy='FedAvg'))
    
    # 3. EXPERIMENT 2: FedProx with high heterogeneity
    results.append(simulate_fl(X_train, y_train, X_test, y_test, alpha=0.3, strategy='FedProx'))
    
    # 4. EXPERIMENT 3: FedProx with low heterogeneity (IID-like)
    results.append(simulate_fl(X_train, y_train, X_test, y_test, alpha=5.0, strategy='FedProx'))
    
    print("\n" + "="*70)
    print("THESIS RESULTS SUMMARY")
    print("="*70)
    for res in results:
        print(f"{res['strategy']} (Alpha={res['alpha']}): Acc={res['accuracy']:.4f}, F1={res['f1']:.4f}")
    
    # Save results to a file for reporting
    import json
    with open('thesis_workflow_results.json', 'w') as f:
        json.dump(results, f)
    print("\n✓ Results saved to thesis_workflow_results.json")
