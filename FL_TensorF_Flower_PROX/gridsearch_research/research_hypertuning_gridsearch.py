#!/usr/bin/env python3
"""
FEDPROX INDIVIDUAL EXPERIMENT RUNNER
====================================

Script untuk menjalankan satu eksperimen FedProx dengan hyperparameters dari environment variables.
Digunakan oleh run_gridsearch.py sebagai subprocess untuk setiap kombinasi parameter.

Environment Variables Expected:
- GRIDSEARCH_BATCH_SIZE: Batch size untuk training
- GRIDSEARCH_LOCAL_EPOCHS: Jumlah local epochs per round
- GRIDSEARCH_LEARNING_RATE: Learning rate untuk optimizer
- GRIDSEARCH_MU: Proximal term coefficient (FedProx-specific)
- GRIDSEARCH_OUTPUT_DIR: Directory untuk menyimpan hasil
- GRIDSEARCH_EXP_NAME: Nama eksperimen

Author: AI Assistant for Federated Learning Research
Date: December 2025
"""

import sys
import os
from pathlib import Path

# CRITICAL: Add parent directory to Python path for Ray workers
# This prevents "ModuleNotFoundError: No module named 'task'" in Ray workers
sys.path.insert(0, str(Path(__file__).parent.parent))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
import gc
import json
import pickle
import warnings
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report, accuracy_score, f1_score, 
    precision_score, recall_score, confusion_matrix
)

import tensorflow as tf
import keras
from keras import backend as K

# Flower imports
import flwr as fl
from flwr.simulation import start_simulation
from flwr.server.strategy import FedProx

# Local imports - ProximalModel is CRITICAL for FedProx
from task import get_model_by_type, ProximalModel
from utils import (
    split_data_non_iid_label,
    evaluate_model_metrics,
    prepare_client_configs,
    print_summary_table
)

# Suppress warnings
warnings.filterwarnings('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Set random seeds
np.random.seed(42)
tf.random.set_seed(42)

# ============================================================================
# READ HYPERPARAMETERS FROM ENVIRONMENT VARIABLES
# ============================================================================
BATCH_SIZE = int(os.environ.get('GRIDSEARCH_BATCH_SIZE', '512'))
LOCAL_EPOCHS = int(os.environ.get('GRIDSEARCH_LOCAL_EPOCHS', '1'))
LEARNING_RATE = float(os.environ.get('GRIDSEARCH_LEARNING_RATE', '0.001'))
MU = float(os.environ.get('GRIDSEARCH_MU', '0.01'))  # FedProx-specific
ALPHA = float(os.environ.get('GRIDSEARCH_ALPHA', '0.3'))  # Dirichlet distribution parameter
OUTPUT_DIR = Path(os.environ.get('GRIDSEARCH_OUTPUT_DIR', './output'))
EXP_NAME = os.environ.get('GRIDSEARCH_EXP_NAME', 'experiment')

# Fixed parameters
NUM_ROUNDS = 20
NUM_CLIENTS = 5
FRAMEWORK = "Flower (flwr)"
ALGORITHM = "Federated Proximal (FedProx)"
DATA_DISTRIBUTION = "Non-IID (Dirichlet) - Natural Imbalance"

# ============================================================================

print("="*80)
print("FEDPROX EXPERIMENT RUNNER")
print("="*80)
print(f"Experiment: {EXP_NAME}")
print(f"Configuration:")
print(f"  - Batch Size: {BATCH_SIZE}")
print(f"  - Local Epochs: {LOCAL_EPOCHS}")
print(f"  - Learning Rate: {LEARNING_RATE}")
print(f"  - Mu (Proximal Term): {MU}")
print(f"  - Alpha (Dirichlet): {ALPHA}")
print(f"  - Num Rounds: {NUM_ROUNDS}")
print(f"  - Num Clients: {NUM_CLIENTS}")
print(f"  - Output Directory: {OUTPUT_DIR}")
print("="*80)

# Create output directories
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
PLOTS_DIR = OUTPUT_DIR / 'plots'
PLOTS_DIR.mkdir(exist_ok=True)
MODELS_DIR = OUTPUT_DIR / 'models'
MODELS_DIR.mkdir(exist_ok=True)

# ============================================================================
# DATA LOADING - LOAD PREPROCESSED DATA (GPU-OPTIMIZED)
# ============================================================================

print("\n" + "="*70)
print("LOAD PREPROCESSED DATA (GPU-OPTIMIZED)")
print("="*70)
print("\nPreprocessing done externally using:")
print("/home/elnoersan/Skripsi/Paper/NotebookTODO/EDA/preprocessing_pipeline.py")
print("\nBenefits:")
print("  - 5-10 minutes → <5 seconds loading time")
print("  - No data leakage (transformers fit only on train)")
print("  - Reproducible across all experiments")
print("  - No SMOTE (preserves natural Non-IID distribution)")

# ============================================================================
# BINARY CLASSIFICATION PREPARATION - LOAD FROM PICKLE
# ============================================================================

print("\n[1/2] Loading binary classification data...")
with open('/home/elnoersan/Skripsi/Paper/NotebookTODO/EDA/processed_artifacts/binary_preprocessed.pkl', 'rb') as f:
    binary_data = pickle.load(f)

X_train_bin_scaled = binary_data['X_train']
X_test_bin_scaled = binary_data['X_test']
y_train_bin = binary_data['y_train']
y_test_bin = binary_data['y_test']

print(f"✓ Binary data loaded:")
print(f"  - Train: {X_train_bin_scaled.shape}")
print(f"  - Test: {X_test_bin_scaled.shape}")
print(f"  - Features: {binary_data.get('metadata', {}).get('n_features_final', 'N/A')}")

gc.collect()

# ============================================================================
# MULTI-CLASS CLASSIFICATION PREPARATION - LOAD FROM PICKLE
# ============================================================================

print("\n[2/2] Loading multi-class classification data...")
with open('/home/elnoersan/Skripsi/Paper/NotebookTODO/EDA/processed_artifacts/multiclass_preprocessed.pkl', 'rb') as f:
    multi_data = pickle.load(f)

X_train_multi_scaled = multi_data['X_train']
X_test_multi_scaled = multi_data['X_test']
y_train_multi = multi_data['y_train']
y_test_multi = multi_data['y_test']
num_classes = multi_data['num_classes']
class_names = multi_data['class_names']  # Load from pickle!
le_target = multi_data['target_encoder']  # Load LabelEncoder from pickle!

print(f"✓ Multi-class data loaded:")
print(f"  - Train: {X_train_multi_scaled.shape}")
print(f"  - Test: {X_test_multi_scaled.shape}")
print(f"  - Classes: {num_classes}")
print(f"  - Class names: {class_names}")
print(f"  - Features: {multi_data.get('metadata', {}).get('n_features_final', 'N/A')}")

print("\n" + "="*70)
print("DATA READY FOR TRAINING!")
print("="*70)
print("✓ No data leakage (preprocessed separately)")
print("✓ Train/test split done before encoding")
print("✓ All transformers fit only on training data")
print(f"✓ Time saved: ~5-10 minutes → <5 seconds")
print("="*70)

gc.collect()

# ============================================================================
# DISTRIBUTE DATA TO CLIENTS (NON-IID)
# ============================================================================

print("\n" + "="*80)
print("DISTRIBUTING DATA TO CLIENTS - NON-IID")
print("="*80)

print("\n[1/2] Splitting Binary data with Dirichlet distribution...")
print(f"      Alpha = {ALPHA} (lower = more heterogeneous)")
client_data_binary = split_data_non_iid_label(
    X_train_bin_scaled, 
    y_train_bin, 
    n_clients=NUM_CLIENTS, 
    alpha=ALPHA
)

print("\n[2/2] Splitting Multi-class data with Dirichlet distribution...")
print(f"      Alpha = {ALPHA} (lower = more heterogeneous)")
client_data_multi = split_data_non_iid_label(
    X_train_multi_scaled, 
    y_train_multi, 
    n_clients=NUM_CLIENTS, 
    alpha=ALPHA
)

print("\nData distribution completed")

# ============================================================================
# FLOWER CLIENT WITH FEDPROX
# ============================================================================

class FlowerClientProx(fl.client.NumPyClient):
    """Flower client with FedProx proximal term"""
    
    def __init__(self, client_data, test_data, model_type, input_shape, num_classes, config):
        self.X_train, self.y_train = client_data
        self.X_test, self.y_test = test_data
        self.model_type = model_type
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.config = config
        self.base_model = None
        self.proximal_model = None
    
    def get_parameters(self, config):
        if self.proximal_model is None:
            self.base_model = get_model_by_type(
                self.model_type,
                self.input_shape,
                self.num_classes,
                self.config['learning_rate']
            )
            return self.base_model.get_weights()
        return self.base_model.get_weights()
    
    def fit(self, parameters, config):
        if self.base_model is None:
            self.base_model = get_model_by_type(
                self.model_type,
                self.input_shape,
                self.num_classes,
                self.config['learning_rate']
            )
        
        # Set weights from server
        self.base_model.set_weights(parameters)
        
        # Get proximal mu from server config
        proximal_mu = config.get('proximal_mu', 0.01)
        
        # Wrap with ProximalModel for FedProx
        self.proximal_model = ProximalModel(self.base_model, parameters, proximal_mu)
        
        # CRITICAL: Compile the ProximalModel
        if self.num_classes == 1:  # Binary classification
            self.proximal_model.compile(
                optimizer=tf.keras.optimizers.Adam(learning_rate=self.config['learning_rate']),
                loss='binary_crossentropy',
                metrics=['accuracy']
            )
        else:  # Multi-class classification
            self.proximal_model.compile(
                optimizer=tf.keras.optimizers.Adam(learning_rate=self.config['learning_rate']),
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy']
            )
        
        # Prepare data based on model type
        if 'cnn' in self.model_type:
            X_train_reshaped = self.X_train.reshape(-1, self.input_shape, 1).astype(np.float32)
        else:
            X_train_reshaped = self.X_train.astype(np.float32)
        
        y_train_prep = self.y_train.astype(np.float32)
        
        # Train with proximal term
        history = self.proximal_model.fit(
            X_train_reshaped,
            y_train_prep,
            epochs=self.config['local_epochs'],
            batch_size=self.config['batch_size'],
            verbose=0
        )
        
        # Return metrics like AVG version does
        metrics = {
            "train_loss": float(history.history['loss'][-1]),
            "train_acc": float(history.history['accuracy'][-1])
        }
        
        return self.base_model.get_weights(), len(self.X_train), metrics
    
    def evaluate(self, parameters, config):
        if self.base_model is None:
            self.base_model = get_model_by_type(
                self.model_type,
                self.input_shape,
                self.num_classes,
                self.config['learning_rate']
            )
        
        self.base_model.set_weights(parameters)
        
        # Prepare test data
        if 'cnn' in self.model_type:
            X_test_reshaped = self.X_test.reshape(-1, self.input_shape, 1).astype(np.float32)
        else:
            X_test_reshaped = self.X_test.astype(np.float32)
        
        y_test_prep = self.y_test.astype(np.float32)
        
        loss, accuracy = self.base_model.evaluate(X_test_reshaped, y_test_prep, verbose=0)
        
        return loss, len(self.X_test), {"eval_acc": float(accuracy)}

def create_client_fn_prox(client_data, test_data, model_type, input_shape, num_classes, config):
    """Factory function for creating FedProx clients"""
    def client_fn(cid: str):
        client_idx = int(cid)
        return FlowerClientProx(
            client_data[client_idx],
            test_data,
            model_type,
            input_shape,
            num_classes,
            config
        )
    return client_fn

# ============================================================================
# FEDERATED LEARNING FUNCTION WITH FEDPROX
# ============================================================================

def run_federated_learning_fedprox(
    client_data,
    test_data,
    model_type,
    input_shape,
    num_classes,
    num_rounds=20,
    num_clients=5,
    local_epochs=1,
    batch_size=256,
    learning_rate=0.001,
    mu=0.01,  # FedProx proximal term
    fraction_fit=1.0,
    fraction_evaluate=1.0
):
    """Run FedProx federated learning with Flower simulation"""
    
    print(f"\n--- Training {model_type} with FedProx (mu={mu}) ---")
    
    # Client configuration
    config = {
        'local_epochs': local_epochs,
        'batch_size': batch_size,
        'learning_rate': learning_rate
    }
    
    # Create client factory
    client_fn = create_client_fn_prox(
        client_data,
        test_data,
        model_type,
        input_shape,
        num_classes,
        config
    )
    
    # Get initial parameters
    initial_model = get_model_by_type(model_type, input_shape, num_classes, learning_rate)
    initial_parameters = fl.common.ndarrays_to_parameters(initial_model.get_weights())
    
    # Track final weights and history
    final_weights = [None]
    history_dict = {
        'train_accuracy': [], 'train_loss': [],
        'eval_accuracy': [], 'eval_loss': [],
        'round_time': [], 'total_time': 0
    }
    round_start_time = [time.time()]
    
    # Custom FedProx strategy with detailed metrics tracking (matches AVG pattern)
    class FedProxWithMetrics(FedProx):
        def aggregate_fit(self, server_round, results, failures):
            round_time = time.time() - round_start_time[0]
            history_dict['round_time'].append(round_time)
            
            aggregated_result = super().aggregate_fit(server_round, results, failures)
            
            if aggregated_result is not None:
                final_weights[0] = aggregated_result[0]
                if results:
                    train_losses = [fit_res.metrics.get('train_loss', 0) for _, fit_res in results if 'train_loss' in fit_res.metrics]
                    train_accs = [fit_res.metrics.get('train_acc', 0) for _, fit_res in results if 'train_acc' in fit_res.metrics]
                    if train_losses:
                        avg_loss = np.mean(train_losses)
                        history_dict['train_loss'].append(avg_loss)
                        print(f"      Round {server_round} - Avg Train Loss: {avg_loss:.4f}")
                    if train_accs:
                        avg_acc = np.mean(train_accs)
                        history_dict['train_accuracy'].append(avg_acc)
                        print(f"      Round {server_round} - Avg Train Acc: {avg_acc:.4f} - Time: {round_time:.2f}s")
            
            round_start_time[0] = time.time()
            return aggregated_result
        
        def aggregate_evaluate(self, server_round, results, failures):
            aggregated_result = super().aggregate_evaluate(server_round, results, failures)
            if results:
                eval_losses = [eval_res.loss for _, eval_res in results]
                eval_accs = [eval_res.metrics.get('eval_acc', 0) for _, eval_res in results if 'eval_acc' in eval_res.metrics]
                if eval_losses:
                    history_dict['eval_loss'].append(np.mean(eval_losses))
                if eval_accs:
                    history_dict['eval_accuracy'].append(np.mean(eval_accs))
            return aggregated_result
    
    # Initialize strategy with proximal_mu
    strategy = FedProxWithMetrics(
        fraction_fit=fraction_fit,
        fraction_evaluate=fraction_evaluate,
        min_fit_clients=max(2, int(num_clients * fraction_fit)),
        min_evaluate_clients=max(2, int(num_clients * fraction_evaluate)),
        min_available_clients=num_clients,
        initial_parameters=initial_parameters,
        proximal_mu=mu,  # FedProx-specific parameter
        on_fit_config_fn=lambda server_round: {'proximal_mu': mu}  # Pass mu to clients
    )
    
    # Run simulation
    start_time = time.time()
    
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore')
        history = start_simulation(
            client_fn=client_fn,
            num_clients=num_clients,
            config=fl.server.ServerConfig(num_rounds=num_rounds),
            strategy=strategy,
        )
    
    total_time = time.time() - start_time
    history_dict['total_time'] = total_time
    
    # Get final model with trained weights
    final_model = get_model_by_type(model_type, input_shape, num_classes, learning_rate)
    if final_weights[0] is not None:
        parameters = fl.common.parameters_to_ndarrays(final_weights[0])
        final_model.set_weights(parameters)
        print(f"   ✓ Model weights updated from federated training")
    else:
        print(f"   ⚠ Warning: Using initial model weights")
    
    print(f"\nFederated learning completed in {total_time:.2f}s")
    return final_model, history_dict

# ============================================================================
# TRAIN ALL MODELS
# ============================================================================

print("\n" + "="*80)
print("STARTING FEDPROX TRAINING")
print(f"Mu (Proximal Term) = {MU}")
print("="*80)

all_models = {}
all_histories = {}
all_metrics = {}

# Binary Models
print("\n--- BINARY CLASSIFICATION ---")

print("\nTraining MLP Binary...")
all_models['mlp_binary'], all_histories['mlp_binary'] = run_federated_learning_fedprox(
    client_data_binary,
    (X_test_bin_scaled, y_test_bin),
    'mlp_binary',
    X_train_bin_scaled.shape[1],
    1,
    num_rounds=NUM_ROUNDS,
    num_clients=NUM_CLIENTS,
    local_epochs=LOCAL_EPOCHS,
    batch_size=BATCH_SIZE,
    learning_rate=LEARNING_RATE,
    mu=MU
)

print("\nTraining CNN Binary...")
all_models['cnn_binary'], all_histories['cnn_binary'] = run_federated_learning_fedprox(
    client_data_binary,
    (X_test_bin_scaled, y_test_bin),
    'cnn_binary',
    X_train_bin_scaled.shape[1],
    1,
    num_rounds=NUM_ROUNDS,
    num_clients=NUM_CLIENTS,
    local_epochs=LOCAL_EPOCHS,
    batch_size=BATCH_SIZE,
    learning_rate=LEARNING_RATE,
    mu=MU
)

# Multi-class Models
print("\n--- MULTI-CLASS CLASSIFICATION ---")

print("\nTraining MLP Multi-class...")
all_models['mlp_multi'], all_histories['mlp_multi'] = run_federated_learning_fedprox(
    client_data_multi,
    (X_test_multi_scaled, y_test_multi),
    'mlp_multi',
    X_train_multi_scaled.shape[1],
    num_classes,
    num_rounds=NUM_ROUNDS,
    num_clients=NUM_CLIENTS,
    local_epochs=LOCAL_EPOCHS,
    batch_size=BATCH_SIZE,
    learning_rate=LEARNING_RATE,
    mu=MU
)

print("\nTraining CNN Multi-class...")
all_models['cnn_multi'], all_histories['cnn_multi'] = run_federated_learning_fedprox(
    client_data_multi,
    (X_test_multi_scaled, y_test_multi),
    'cnn_multi',
    X_train_multi_scaled.shape[1],
    num_classes,
    num_rounds=NUM_ROUNDS,
    num_clients=NUM_CLIENTS,
    local_epochs=LOCAL_EPOCHS,
    batch_size=BATCH_SIZE,
    learning_rate=LEARNING_RATE,
    mu=MU
)

print("\nAll models trained successfully!")

# ============================================================================
# EVALUATE MODELS
# ============================================================================

print("\n" + "="*80)
print("EVALUATING ALL MODELS")
print("="*80)

# Binary Models Evaluation
print("\n--- BINARY MODELS ---")

print("\n[1/4] MLP Binary...")
X_test_eval = X_test_bin_scaled.astype(np.float32)
with warnings.catch_warnings():
    warnings.filterwarnings('ignore')
    y_pred_prob = all_models['mlp_binary'].predict(X_test_eval, verbose=0)
y_pred = (y_pred_prob > 0.5).astype(int).flatten()
all_metrics['mlp_binary'] = evaluate_model_metrics(
    y_test_bin, y_pred, "MLP Binary (FedProx)", is_binary=True,
    target_names=['Normal', 'Attack'],
    y_pred_proba=y_pred_prob
)

print("\n[2/4] CNN Binary...")
X_test_eval_cnn = X_test_bin_scaled.reshape(-1, X_train_bin_scaled.shape[1], 1).astype(np.float32)
with warnings.catch_warnings():
    warnings.filterwarnings('ignore')
    y_pred_prob = all_models['cnn_binary'].predict(X_test_eval_cnn, verbose=0)
y_pred = (y_pred_prob > 0.5).astype(int).flatten()
all_metrics['cnn_binary'] = evaluate_model_metrics(
    y_test_bin, y_pred, "CNN Binary (FedProx)", is_binary=True,
    target_names=['Normal', 'Attack'],
    y_pred_proba=y_pred_prob
)

# Multi-class Models Evaluation
print("\n--- MULTI-CLASS MODELS ---")

print("\n[3/4] MLP Multi-class...")
X_test_eval = X_test_multi_scaled.astype(np.float32)
with warnings.catch_warnings():
    warnings.filterwarnings('ignore')
    y_pred_prob = all_models['mlp_multi'].predict(X_test_eval, verbose=0)
y_pred = np.argmax(y_pred_prob, axis=1)
all_metrics['mlp_multi'] = evaluate_model_metrics(
    y_test_multi, y_pred, "MLP Multi (FedProx)", is_binary=False,
    target_names=le_target.classes_,
    y_pred_proba=y_pred_prob
)

print("\n[4/4] CNN Multi-class...")
X_test_eval_cnn = X_test_multi_scaled.reshape(-1, X_train_multi_scaled.shape[1], 1).astype(np.float32)
with warnings.catch_warnings():
    warnings.filterwarnings('ignore')
    y_pred_prob = all_models['cnn_multi'].predict(X_test_eval_cnn, verbose=0)
y_pred = np.argmax(y_pred_prob, axis=1)
all_metrics['cnn_multi'] = evaluate_model_metrics(
    y_test_multi, y_pred, "CNN Multi (FedProx)", is_binary=False,
    target_names=le_target.classes_,
    y_pred_proba=y_pred_prob
)

print("\n" + "="*80)
print("EVALUATION COMPLETED")
print("="*80)

# ============================================================================
# SAVE RESULTS
# ============================================================================
print("\n--- SAVING RESULTS ---")

# Save models
for model_name, model in all_models.items():
    model_path = MODELS_DIR / f"{model_name}.keras"
    model.save(model_path)
    print(f"✓ Saved {model_name} to {model_path}")

# Prepare results summary
results_summary = {
    'experiment_name': EXP_NAME,
    'hyperparameters': {
        'batch_size': BATCH_SIZE,
        'local_epochs': LOCAL_EPOCHS,
        'learning_rate': LEARNING_RATE,
        'mu': MU,  # FedProx-specific
        'alpha': ALPHA,
        'num_rounds': NUM_ROUNDS,
        'num_clients': NUM_CLIENTS
    },
    'binary': {},
    'multi': {}
}

for name in ['MLP Binary', 'CNN Binary']:
    key = name.lower().replace(' ', '_')
    results_summary['binary'][name] = {
        'accuracy': float(all_metrics[key]['accuracy']),
        'precision': float(all_metrics[key]['precision']),
        'recall': float(all_metrics[key]['recall']),
        'f1_score': float(all_metrics[key]['f1_score']),
        'auc_roc': float(all_metrics[key].get('auc_roc', 0))
    }

for name in ['MLP Multi', 'CNN Multi']:
    key = name.lower().replace(' ', '_')
    results_summary['multi'][name] = {
        'accuracy': float(all_metrics[key]['accuracy']),
        'precision': float(all_metrics[key]['precision']),
        'recall': float(all_metrics[key]['recall']),
        'f1_score': float(all_metrics[key]['f1_score']),
        'auc_roc': float(all_metrics[key].get('auc_roc', 0))
    }

# Save results
results_file = OUTPUT_DIR / 'results_summary.json'
with open(results_file, 'w') as f:
    json.dump(results_summary, f, indent=2)
print(f"✓ Saved results summary to {results_file}")

# ============================================================================
# GENERATE VISUALIZATIONS
# ============================================================================
print("\n--- GENERATING VISUALIZATIONS ---")

plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(3, 2, figsize=(16, 18))

model_names = ['MLP Binary', 'CNN Binary', 'MLP Multi', 'CNN Multi']
model_keys = ['mlp_binary', 'cnn_binary', 'mlp_multi', 'cnn_multi']
colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D']
markers = ['o', 's', '^', 'd']

# Plot 1: Training Accuracy
axes[0, 0].set_title(f'Training Accuracy per Round\n{EXP_NAME}', fontsize=12, fontweight='bold')
for i, (name, key) in enumerate(zip(model_names, model_keys)):
    if all_histories[key]['train_accuracy']:
        rounds = list(range(1, len(all_histories[key]['train_accuracy']) + 1))
        axes[0, 0].plot(rounds, all_histories[key]['train_accuracy'], 
                       label=name, marker=markers[i], color=colors[i], linewidth=2, markersize=6)
axes[0, 0].set_xlabel('Round')
axes[0, 0].set_ylabel('Accuracy')
axes[0, 0].legend(loc='lower right', fontsize=9)
axes[0, 0].grid(True, alpha=0.3)

# Plot 2: Training Loss
axes[0, 1].set_title(f'Training Loss per Round\n{EXP_NAME}', fontsize=12, fontweight='bold')
for i, (name, key) in enumerate(zip(model_names, model_keys)):
    if all_histories[key]['train_loss']:
        rounds = list(range(1, len(all_histories[key]['train_loss']) + 1))
        axes[0, 1].plot(rounds, all_histories[key]['train_loss'], 
                       label=name, marker=markers[i], color=colors[i], linewidth=2, markersize=6)
axes[0, 1].set_xlabel('Round')
axes[0, 1].set_ylabel('Loss')
axes[0, 1].legend(loc='upper right', fontsize=9)
axes[0, 1].grid(True, alpha=0.3)

# Plot 3: Metrics Comparison
accuracies = [all_metrics[key]['accuracy'] for key in model_keys]
f1_scores = [all_metrics[key]['f1_score'] for key in model_keys]

x_pos = np.arange(len(model_names))
width = 0.35
bars1 = axes[1, 0].bar(x_pos - width/2, accuracies, width, label='Accuracy', color=colors, alpha=0.8)
bars2 = axes[1, 0].bar(x_pos + width/2, f1_scores, width, label='F1-Score', color=colors, alpha=0.6)

axes[1, 0].set_title('Accuracy vs F1-Score', fontsize=12, fontweight='bold')
axes[1, 0].set_ylabel('Score')
axes[1, 0].set_xticks(x_pos)
axes[1, 0].set_xticklabels(model_names, rotation=45, ha='right')
axes[1, 0].legend()
axes[1, 0].set_ylim(0, 1.1)

# Plot 4: Precision vs Recall
precisions = [all_metrics[key]['precision'] for key in model_keys]
recalls = [all_metrics[key]['recall'] for key in model_keys]

bars3 = axes[1, 1].bar(x_pos - width/2, precisions, width, label='Precision', color=colors, alpha=0.8)
bars4 = axes[1, 1].bar(x_pos + width/2, recalls, width, label='Recall', color=colors, alpha=0.6)

axes[1, 1].set_title('Precision vs Recall', fontsize=12, fontweight='bold')
axes[1, 1].set_ylabel('Score')
axes[1, 1].set_xticks(x_pos)
axes[1, 1].set_xticklabels(model_names, rotation=45, ha='right')
axes[1, 1].legend()
axes[1, 1].set_ylim(0, 1.1)

# Plot 5: Confusion Matrix - Best Binary
best_binary_key = 'mlp_binary' if all_metrics['mlp_binary']['f1_score'] > all_metrics['cnn_binary']['f1_score'] else 'cnn_binary'
best_binary_name = 'MLP Binary' if best_binary_key == 'mlp_binary' else 'CNN Binary'
y_pred_best = all_metrics[best_binary_key]['predictions']
cm = confusion_matrix(y_test_bin, y_pred_best)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[2, 0],
            xticklabels=['Normal', 'Attack'], yticklabels=['Normal', 'Attack'])
axes[2, 0].set_title(f'Confusion Matrix - {best_binary_name}', fontsize=12, fontweight='bold')
axes[2, 0].set_ylabel('True Label')
axes[2, 0].set_xlabel('Predicted Label')

# Plot 6: All Metrics Summary
metrics_data = []
for key in model_keys:
    metrics_data.append([
        all_metrics[key]['accuracy'],
        all_metrics[key]['precision'],
        all_metrics[key]['recall'],
        all_metrics[key]['f1_score']
    ])

x_metrics = np.arange(4)
bar_width = 0.2

for i, (name, data) in enumerate(zip(model_names, metrics_data)):
    axes[2, 1].bar(x_metrics + i*bar_width, data, bar_width, 
                   label=name, color=colors[i], alpha=0.8)

axes[2, 1].set_title('All Metrics Summary', fontsize=12, fontweight='bold')
axes[2, 1].set_ylabel('Score')
axes[2, 1].set_xticks(x_metrics + bar_width * 1.5)
axes[2, 1].set_xticklabels(['Accuracy', 'Precision', 'Recall', 'F1-Score'])
axes[2, 1].legend(loc='lower right', fontsize=8)
axes[2, 1].set_ylim(0, 1.1)
axes[2, 1].grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plot_file = PLOTS_DIR / 'comprehensive_results.png'
plt.savefig(plot_file, dpi=300, bbox_inches='tight')
print(f"✓ Saved plots to {plot_file}")
plt.close()

# ============================================================================
# GENERATE EXPERIMENT REPORT
# ============================================================================
print("\n--- GENERATING EXPERIMENT REPORT ---")

report_file = OUTPUT_DIR / 'experiment_report.md'
with open(report_file, 'w') as f:
    f.write(f"# Experiment Report: {EXP_NAME}\n\n")
    f.write(f"**Date**: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    
    f.write("## Hyperparameters\n\n")
    f.write(f"- **Batch Size**: {BATCH_SIZE}\n")
    f.write(f"- **Local Epochs**: {LOCAL_EPOCHS}\n")
    f.write(f"- **Learning Rate**: {LEARNING_RATE}\n")
    f.write(f"- **Mu (Proximal Term)**: {MU}\n")
    f.write(f"- **Number of Rounds**: {NUM_ROUNDS}\n")
    f.write(f"- **Number of Clients**: {NUM_CLIENTS}\n\n")
    
    f.write("## Results Summary\n\n")
    f.write("### Binary Classification\n\n")
    f.write("| Model | Accuracy | Precision | Recall | F1-Score | AUC-ROC |\n")
    f.write("|-------|----------|-----------|--------|----------|----------|\n")
    for name in ['MLP Binary', 'CNN Binary']:
        key = name.lower().replace(' ', '_')
        m = all_metrics[key]
        f.write(f"| {name} | {m['accuracy']:.4f} | {m['precision']:.4f} | "
               f"{m['recall']:.4f} | {m['f1_score']:.4f} | {m.get('auc_roc', 0):.4f} |\n")
    
    f.write("\n### Multi-class Classification\n\n")
    f.write("| Model | Accuracy | Precision | Recall | F1-Score | AUC-ROC |\n")
    f.write("|-------|----------|-----------|--------|----------|----------|\n")
    for name in ['MLP Multi', 'CNN Multi']:
        key = name.lower().replace(' ', '_')
        m = all_metrics[key]
        f.write(f"| {name} | {m['accuracy']:.4f} | {m['precision']:.4f} | "
               f"{m['recall']:.4f} | {m['f1_score']:.4f} | {m.get('auc_roc', 0):.4f} |\n")
    
    f.write("\n## Training Time\n\n")
    for name, key in zip(model_names, model_keys):
        total_time = all_histories[key]['total_time']
        avg_time = np.mean(all_histories[key]['round_time'])
        f.write(f"- **{name}**: Total={total_time:.2f}s, Avg/Round={avg_time:.2f}s\n")
    
    f.write("\n## Visualizations\n\n")
    f.write(f"![Results]({PLOTS_DIR.name}/comprehensive_results.png)\n\n")
    
    f.write("## Files Generated\n\n")
    f.write("- `results_summary.json` - Metrics in JSON format\n")
    f.write("- `models/` - Saved trained models\n")
    f.write("- `plots/` - Visualization plots\n")

print(f"✓ Saved experiment report to {report_file}")

# ============================================================================
# FINAL SUMMARY
# ============================================================================
print("\n" + "="*80)
print("EXPERIMENT COMPLETED SUCCESSFULLY")
print("="*80)
print(f"Experiment Name: {EXP_NAME}")
print(f"Output Directory: {OUTPUT_DIR}")
print(f"\nBest Binary Model: {best_binary_name}")
print(f"  - F1-Score: {all_metrics[best_binary_key]['f1_score']:.4f}")
print(f"  - Accuracy: {all_metrics[best_binary_key]['accuracy']:.4f}")

best_multi_key = 'mlp_multi' if all_metrics['mlp_multi']['f1_score'] > all_metrics['cnn_multi']['f1_score'] else 'cnn_multi'
best_multi_name = 'MLP Multi' if best_multi_key == 'mlp_multi' else 'CNN Multi'
print(f"\nBest Multi-class Model: {best_multi_name}")
print(f"  - F1-Score: {all_metrics[best_multi_key]['f1_score']:.4f}")
print(f"  - Accuracy: {all_metrics[best_multi_key]['accuracy']:.4f}")

print("\n" + "="*80)
print("ALL FILES SAVED SUCCESSFULLY")
print("="*80)
