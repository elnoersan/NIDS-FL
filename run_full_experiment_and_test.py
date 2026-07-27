import os
import sys
import pickle
import numpy as np
import tensorflow as tf
from pathlib import Path

# Add FL_TensorF_Flower_PROX to path to reuse its utilities
sys.path.append(os.path.abspath('FL_TensorF_Flower_PROX'))
from task import ProximalModel, get_model_by_type
from utils import split_data_non_iid_label, evaluate_model_metrics

# Fix memory growth for TF
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
    except RuntimeError as e:
        print(e)

print("="*70)
print("NIDS-FL: FULL PIPELINE EXECUTION (FEDPROX + SIMPLE PENTEST)")
print("="*70)

# 1. Load the fixed 45-feature preprocessed dataset
data_path = Path('EDA/processed_artifacts/binary_preprocessed.pkl')
if not data_path.exists():
    print(f"Error: {data_path} not found. Please run preprocessing first.")
    sys.exit(1)

print("\n[1] Loading Preprocessed Dataset (45 Features)...")
with open(data_path, 'rb') as f:
    data = pickle.load(f)

X_train = data['X_train']
y_train = data['y_train']
X_test = data['X_test']
y_test = data['y_test']

input_shape = X_train.shape[1]
print(f"✓ Dataset loaded successfully. Input features: {input_shape}")
if input_shape != 45:
    print(f"⚠️ Warning: Expected 45 features, got {input_shape}")

# 2. Simulate Federated Learning Data Partitioning (Dirichlet Non-IID)
print("\n[2] Partitioning Data for 3 Clients (Non-IID Alpha=0.3)...")
num_clients = 3
client_datasets = split_data_non_iid_label(X_train, y_train, num_clients, alpha=0.3)
print("✓ Data partitioned using Dirichlet distribution.")

# 3. Initialize Global Model
print("\n[3] Initializing Global Model (FedProx - MLP Binary)...")
global_model = get_model_by_type('mlp_binary', input_shape=input_shape)
global_weights = global_model.get_weights()

# 4. Simulate FedProx Training (2 Rounds)
num_rounds = 2
local_epochs = 2
mu = 0.01

print(f"\n[4] Starting Federated Learning Simulation ({num_rounds} Rounds)...")
for round_num in range(1, num_rounds + 1):
    print(f"\n--- Round {round_num} ---")
    new_weights_list = []
    
    for client_id in range(num_clients):
        X_local, y_local = client_datasets[client_id]
        
        # Create client proximal model
        base_model = get_model_by_type('mlp_binary', input_shape=input_shape)
        base_model.set_weights(global_weights) # Initialize with global weights
        
        prox_model = ProximalModel(base_model, global_weights, mu=mu)
        prox_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        
        # Train local model
        prox_model.fit(X_local, y_local, epochs=local_epochs, batch_size=256, verbose=0)
        new_weights_list.append(prox_model.model.get_weights())
        
    # FedAvg Aggregation step
    print("  Aggregating local models...")
    aggregated_weights = []
    for weights_group in zip(*new_weights_list):
        aggregated_weights.append(np.mean(weights_group, axis=0))
        
    global_weights = aggregated_weights
    global_model.set_weights(global_weights)
    
    # Evaluate Global Model
    loss, acc = global_model.evaluate(X_test, y_test, verbose=0)
    print(f"  Global Model Validation - Loss: {loss:.4f}, Accuracy: {acc:.4f}")

print("\n✓ Federated Learning completed. Global model updated.")

# 5. Simple External Pentest / Testing Simulation
print("\n" + "="*70)
print("[5] EXTERNAL PENTEST & TRAFFIC SIMULATION")
print("="*70)
print("Simulating live network traffic interception and prediction outside the training loop...\n")

# Randomly select a few attack and normal payloads from the test set
np.random.seed(42)
normal_idx = np.where(y_test == 0)[0]
attack_idx = np.where(y_test == 1)[0]

test_indices = np.concatenate([
    np.random.choice(normal_idx, 3, replace=False),
    np.random.choice(attack_idx, 3, replace=False)
])
np.random.shuffle(test_indices)

payloads = X_test[test_indices]
true_labels = y_test[test_indices]

attack_types = {0: "Normal Traffic", 1: "Malicious Attack"}

success_count = 0
for i, (payload, true_label) in enumerate(zip(payloads, true_labels)):
    # Simulating sending payload to API
    print(f"[Packet {i+1}] Intercepting network payload (Size: {len(payload)} features)...")
    
    # Predict using the trained global model
    payload_input = np.expand_dims(payload, axis=0)
    prediction_prob = global_model.predict(payload_input, verbose=0)[0][0]
    predicted_class = 1 if prediction_prob > 0.5 else 0
    
    true_desc = attack_types[true_label]
    pred_desc = attack_types[predicted_class]
    
    if predicted_class == true_label:
        status = "✅ DEFENDED / DETECTED"
        success_count += 1
    else:
        status = "❌ BREACHED / MISSED"
        
    print(f"   -> True Nature : {true_desc}")
    print(f"   -> IDS Verdict : {pred_desc} (Confidence: {prediction_prob:.2%})")
    print(f"   -> Result      : {status}\n")

accuracy = success_count / len(test_indices)
print(f"Pentest Simulation Complete! IDS Detection Rate on test payload: {accuracy:.2%}")
print("="*70)
print("Pipeline Execution Finished Successfully.")
