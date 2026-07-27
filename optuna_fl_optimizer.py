import os
import sys
import pickle
import numpy as np
import optuna
import tensorflow as tf
from pathlib import Path

# Fix memory growth for TF
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
    except RuntimeError as e:
        print(e)

# Suppress TF logging for cleaner Optuna output
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
tf.get_logger().setLevel('ERROR')

sys.path.append(os.path.abspath('FL_TensorF_Flower_PROX'))
from task import ProximalModel, get_model_by_type
from utils import split_data_non_iid_label

print("="*70)
print("Optuna Hyperparameter Optimization for Federated Learning (NIDS-FL)")
print("="*70)

# 1. Load Dataset
data_path = Path('EDA/processed_artifacts/binary_preprocessed.pkl')
if not data_path.exists():
    print(f"Error: {data_path} not found.")
    sys.exit(1)

with open(data_path, 'rb') as f:
    data = pickle.load(f)

X_train, y_train = data['X_train'], data['y_train']
X_test, y_test = data['X_test'], data['y_test']
input_shape = X_train.shape[1]

num_clients = 3
num_rounds = 3  # Fast evaluation for HPO

def objective(trial):
    """
    Optuna objective function for tuning FL hyperparameters.
    Replaces the bloated manual GridSearch.
    """
    # Suggest Hyperparameters
    lr = trial.suggest_float("lr", 1e-4, 1e-2, log=True)
    batch_size = trial.suggest_categorical("batch_size", [128, 256, 512, 1024])
    local_epochs = trial.suggest_int("local_epochs", 1, 3)
    mu = trial.suggest_float("mu", 0.001, 0.1, log=True)
    alpha = trial.suggest_categorical("alpha", [0.3, 5.0]) # Heterogeneity 

    # Prepare Data
    client_datasets = split_data_non_iid_label(X_train, y_train, num_clients, alpha=alpha)
    
    # Global Model Init
    global_model = get_model_by_type('mlp_binary', input_shape=input_shape, learning_rate=lr)
    global_weights = global_model.get_weights()
    
    # Federated Training Loop
    for round_num in range(1, num_rounds + 1):
        new_weights_list = []
        
        for client_id in range(num_clients):
            X_local, y_local = client_datasets[client_id]
            
            # Local Training with FedProx
            base_model = get_model_by_type('mlp_binary', input_shape=input_shape, learning_rate=lr)
            base_model.set_weights(global_weights)
            
            prox_model = ProximalModel(base_model, global_weights, mu=mu)
            prox_model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=lr), 
                               loss='binary_crossentropy', metrics=['accuracy'])
            
            prox_model.fit(X_local, y_local, epochs=local_epochs, batch_size=batch_size, verbose=0)
            new_weights_list.append(prox_model.model.get_weights())
            
        # FedAvg Aggregation
        global_weights = [np.mean(weights_group, axis=0) for weights_group in zip(*new_weights_list)]
        
    # Evaluate Global Model
    global_model.set_weights(global_weights)
    loss, acc = global_model.evaluate(X_test, y_test, verbose=0)
    
    # We want to MAXIMIZE accuracy
    return acc

if __name__ == "__main__":
    # Create an Optuna study. It can use SQLite to save progress without generating thousands of files.
    study = optuna.create_study(
        study_name="NIDS_FL_Optimization",
        direction="maximize", 
        storage="sqlite:///optuna_fl_study.db", 
        load_if_exists=True
    )
    
    print("\n🚀 Starting Bayesian Hyperparameter Optimization...")
    # Run 10 trials as a quick example. (In production, increase n_trials)
    study.optimize(objective, n_trials=10)
    
    print("\n" + "="*70)
    print("🏆 OPTIMIZATION FINISHED")
    print("="*70)
    print(f"Best Trial: {study.best_trial.number}")
    print(f"Best Accuracy: {study.best_value:.4f}")
    print("Best Hyperparameters:")
    for key, value in study.best_params.items():
        print(f"  - {key}: {value}")
    print("\n✅ Database saved to 'optuna_fl_study.db' (No bloated folders/images created!)")
