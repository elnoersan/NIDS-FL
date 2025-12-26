#!/usr/bin/env python3
"""
Federated Learning Research - Grid Search Version
==================================================
This version accepts hyperparameters from environment variables
and saves all outputs to a specified directory.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
import os
import gc
import json
import sys
from pathlib import Path
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
from flwr.server.strategy import FedAvg

# Local imports - go up one directory to find task.py and utils.py
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from task import get_model_by_type
from utils import (
    split_data_non_iid_label,
    evaluate_model_metrics,
    prepare_client_configs,
    print_summary_table
)
import pickle
from tabulate import tabulate
import warnings

# Set random seeds
np.random.seed(42)
tf.random.set_seed(42)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# ============================================================================
# HYPERPARAMETERS FROM ENVIRONMENT VARIABLES
# ============================================================================
BATCH_SIZE = int(os.environ.get('GRIDSEARCH_BATCH_SIZE', '256'))
LOCAL_EPOCHS = int(os.environ.get('GRIDSEARCH_LOCAL_EPOCHS', '1'))
LEARNING_RATE = float(os.environ.get('GRIDSEARCH_LEARNING_RATE', '0.001'))
ALPHA = float(os.environ.get('GRIDSEARCH_ALPHA', '0.3'))  # Dirichlet distribution parameter
OUTPUT_DIR = Path(os.environ.get('GRIDSEARCH_OUTPUT_DIR', './output'))
EXP_NAME = os.environ.get('GRIDSEARCH_EXP_NAME', 'experiment')

# Create output directories
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
PLOTS_DIR = OUTPUT_DIR / 'plots'
PLOTS_DIR.mkdir(exist_ok=True)
MODELS_DIR = OUTPUT_DIR / 'models'
MODELS_DIR.mkdir(exist_ok=True)

# Fixed parameters
NUM_ROUNDS = 20
NUM_CLIENTS = 5
FRAMEWORK = "Flower (flwr)"
ALGORITHM = "Federated Averaging (FedAvg)"
DATA_DISTRIBUTION = "Non-IID (Dirichlet) - Natural Imbalance"

print("="*80)
print("FEDERATED AVERAGING (FEDAVG) WITH FLOWER - GRID SEARCH MODE")
print("="*80)
print(f"Experiment: {EXP_NAME}")
print(f"Configuration: {NUM_CLIENTS} Clients, {NUM_ROUNDS} Rounds, {LOCAL_EPOCHS} Local Epochs")
print("Hyperparameters:")
print(f"  - Batch Size: {BATCH_SIZE}")
print(f"  - Local Epochs: {LOCAL_EPOCHS}")
print(f"  - Learning Rate: {LEARNING_RATE}")
print(f"  - Alpha (Dirichlet): {ALPHA}")
print(f"Output Directory: {OUTPUT_DIR}")
print(f"Data Distribution: {DATA_DISTRIBUTION}")
print("="*80 + "\n")

print(f"TensorFlow version: {tf.__version__}")
print(f"Flower version: {fl.__version__}\n")

# ============================================================================
# LOAD PREPROCESSED DATA (GPU-OPTIMIZED)
# ============================================================================
print("="*70)
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
# SPLIT DATA TO CLIENTS (NON-IID)
# ============================================================================
print("="*80)
print("DISTRIBUTING DATA TO CLIENTS - NON-IID")
print("="*80)

print(f"\n[1/2] Splitting Binary data (Alpha={ALPHA})...")
client_data_binary = split_data_non_iid_label(
    X_train_bin_scaled, y_train_bin, n_clients=NUM_CLIENTS, alpha=ALPHA
)

print(f"\n[2/2] Splitting Multi-class data (Alpha={ALPHA})...")
client_data_multi = split_data_non_iid_label(
    X_train_multi_scaled, y_train_multi, n_clients=NUM_CLIENTS, alpha=ALPHA
)

print("\n" + "="*80)
print("DATA SPLIT COMPLETED")
print("="*80 + "\n")

# ============================================================================
# FLOWER CLIENT DEFINITION
# ============================================================================
class FlowerClient(fl.client.NumPyClient):
    def __init__(self, client_id, X_train, y_train, X_test, y_test, 
                 model_type, input_shape, num_classes, config):
        self.client_id = client_id
        self.X_train = X_train.astype(np.float32)
        self.y_train = y_train
        self.X_test = X_test.astype(np.float32) if X_test is not None else None
        self.y_test = y_test
        self.model_type = model_type
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.config = config
        self.model = None
        
        if 'cnn' in model_type:
            self.X_train = self.X_train.reshape(-1, input_shape, 1)
            if self.X_test is not None:
                self.X_test = self.X_test.reshape(-1, input_shape, 1)
    
    def get_parameters(self, config):
        if self.model is None:
            self.model = get_model_by_type(
                self.model_type, self.input_shape, 
                self.num_classes, self.config['learning_rate']
            )
        return self.model.get_weights()
    
    def set_parameters(self, parameters):
        if self.model is None:
            self.model = get_model_by_type(
                self.model_type, self.input_shape, 
                self.num_classes, self.config['learning_rate']
            )
        self.model.set_weights(parameters)
    
    def fit(self, parameters, config):
        self.set_parameters(parameters)
        history = self.model.fit(
            self.X_train, self.y_train,
            epochs=self.config['local_epochs'],
            batch_size=self.config['batch_size'],
            verbose=0
        )
        metrics = {
            "train_loss": history.history['loss'][-1],
            "train_acc": history.history['accuracy'][-1]
        }
        return self.get_parameters(config), len(self.X_train), metrics
    
    def evaluate(self, parameters, config):
        if self.X_test is None:
            return 0.0, 0, {}
        self.set_parameters(parameters)
        loss, accuracy = self.model.evaluate(
            self.X_test, self.y_test, 
            batch_size=self.config['batch_size'], 
            verbose=0
        )
        return loss, len(self.X_test), {"eval_acc": accuracy}


def create_client_fn(client_data, test_data, model_type, input_shape, num_classes, config):
    X_test, y_test = test_data
    def client_fn(cid: str) -> FlowerClient:
        client_id = int(cid)
        X_train, y_train = client_data[client_id]
        return FlowerClient(
            client_id, X_train, y_train, X_test, y_test,
            model_type, input_shape, num_classes, config
        )
    return client_fn

# ============================================================================
# FEDERATED LEARNING FUNCTION
# ============================================================================
def run_federated_learning_flower(
    client_data, test_data, model_type, input_shape, num_classes,
    num_rounds, num_clients, local_epochs, batch_size, learning_rate,
    fraction_fit=1.0, fraction_evaluate=1.0
):
    print(f"\n[INFO] Starting Flower FL for {model_type}...")
    print(f"   Clients: {num_clients} | Rounds: {num_rounds} | Local epochs: {local_epochs}")
    
    config = {
        'local_epochs': local_epochs,
        'batch_size': batch_size,
        'learning_rate': learning_rate
    }
    
    client_fn = create_client_fn(client_data, test_data, model_type, input_shape, num_classes, config)
    initial_model = get_model_by_type(model_type, input_shape, num_classes, learning_rate)
    initial_parameters = fl.common.ndarrays_to_parameters(initial_model.get_weights())
    
    final_weights = [None]
    history_dict = {
        'train_accuracy': [], 'train_loss': [],
        'eval_accuracy': [], 'eval_loss': [],
        'round_time': [], 'total_time': 0
    }
    round_start_time = [time.time()]
    
    class FedAvgWithWeights(FedAvg):
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
    
    strategy = FedAvgWithWeights(
        fraction_fit=fraction_fit,
        fraction_evaluate=fraction_evaluate,
        min_fit_clients=max(2, int(num_clients * fraction_fit)),
        min_evaluate_clients=max(2, int(num_clients * fraction_evaluate)),
        min_available_clients=num_clients,
        initial_parameters=initial_parameters,
    )
    
    start_time = time.time()
    history = start_simulation(
        client_fn=client_fn,
        num_clients=num_clients,
        config=fl.server.ServerConfig(num_rounds=num_rounds),
        strategy=strategy,
    )
    total_time = time.time() - start_time
    history_dict['total_time'] = total_time
    
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
print("STARTING FEDERATED TRAINING")
print("="*80)

all_models = {}
all_histories = {}
all_metrics = {}

print("\n--- BINARY DETECTION MODELS ---")
print("\nTraining MLP Binary...")
all_models['mlp_binary'], all_histories['mlp_binary'] = run_federated_learning_flower(
    client_data_binary, (X_test_bin_scaled, y_test_bin),
    'mlp_binary', X_train_bin_scaled.shape[1], 1,
    NUM_ROUNDS, NUM_CLIENTS, LOCAL_EPOCHS, BATCH_SIZE, LEARNING_RATE
)

print("\nTraining CNN Binary...")
all_models['cnn_binary'], all_histories['cnn_binary'] = run_federated_learning_flower(
    client_data_binary, (X_test_bin_scaled, y_test_bin),
    'cnn_binary', X_train_bin_scaled.shape[1], 1,
    NUM_ROUNDS, NUM_CLIENTS, LOCAL_EPOCHS, BATCH_SIZE, LEARNING_RATE
)

print("\n--- MULTI-CLASS MODELS ---")
print("\nTraining MLP Multi-class...")
all_models['mlp_multi'], all_histories['mlp_multi'] = run_federated_learning_flower(
    client_data_multi, (X_test_multi_scaled, y_test_multi),
    'mlp_multi', X_train_multi_scaled.shape[1], num_classes,
    NUM_ROUNDS, NUM_CLIENTS, LOCAL_EPOCHS, BATCH_SIZE, LEARNING_RATE
)

print("\nTraining CNN Multi-class...")
all_models['cnn_multi'], all_histories['cnn_multi'] = run_federated_learning_flower(
    client_data_multi, (X_test_multi_scaled, y_test_multi),
    'cnn_multi', X_train_multi_scaled.shape[1], num_classes,
    NUM_ROUNDS, NUM_CLIENTS, LOCAL_EPOCHS, BATCH_SIZE, LEARNING_RATE
)

print("\nAll models trained successfully!")

# ============================================================================
# EVALUATE MODELS
# ============================================================================
print("\n" + "="*80)
print("EVALUATING ALL MODELS")
print("="*80)

print("\n--- BINARY MODELS ---")
print("\n[1/4] MLP Binary...")
X_test_eval = X_test_bin_scaled.astype(np.float32)
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=DeprecationWarning)
    y_pred_prob = all_models['mlp_binary'].predict(X_test_eval, verbose=0)
y_pred = (y_pred_prob > 0.5).astype(int).flatten()
all_metrics['MLP Binary'] = evaluate_model_metrics(
    y_test_bin, y_pred, "MLP Binary (FedAvg)", is_binary=True,
    target_names=['Normal', 'Attack'], y_pred_proba=y_pred_prob
)

print("\n[2/4] CNN Binary...")
X_test_eval_cnn = X_test_bin_scaled.reshape(-1, X_train_bin_scaled.shape[1], 1).astype(np.float32)
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=DeprecationWarning)
    y_pred_prob = all_models['cnn_binary'].predict(X_test_eval_cnn, verbose=0)
y_pred = (y_pred_prob > 0.5).astype(int).flatten()
all_metrics['CNN Binary'] = evaluate_model_metrics(
    y_test_bin, y_pred, "CNN Binary (FedAvg)", is_binary=True,
    target_names=['Normal', 'Attack'], y_pred_proba=y_pred_prob
)

print("\n--- MULTI-CLASS MODELS ---")
print("\n[3/4] MLP Multi-class...")
X_test_eval = X_test_multi_scaled.astype(np.float32)
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=DeprecationWarning)
    y_pred_prob = all_models['mlp_multi'].predict(X_test_eval, verbose=0)
y_pred = np.argmax(y_pred_prob, axis=1)
all_metrics['MLP Multi'] = evaluate_model_metrics(
    y_test_multi, y_pred, "MLP Multi (FedAvg)", is_binary=False,
    target_names=le_target.classes_, y_pred_proba=y_pred_prob
)

print("\n[4/4] CNN Multi-class...")
X_test_eval_cnn = X_test_multi_scaled.reshape(-1, X_train_multi_scaled.shape[1], 1).astype(np.float32)
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=DeprecationWarning)
    y_pred_prob = all_models['cnn_multi'].predict(X_test_eval_cnn, verbose=0)
y_pred = np.argmax(y_pred_prob, axis=1)
all_metrics['CNN Multi'] = evaluate_model_metrics(
    y_test_multi, y_pred, "CNN Multi (FedAvg)", is_binary=False,
    target_names=le_target.classes_, y_pred_proba=y_pred_prob
)

print("\n" + "="*80)

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
        'alpha': ALPHA,
        'num_rounds': NUM_ROUNDS,
        'num_clients': NUM_CLIENTS
    },
    'binary': {},
    'multi': {}
}

for name in ['MLP Binary', 'CNN Binary']:
    results_summary['binary'][name] = {
        'accuracy': float(all_metrics[name]['accuracy']),
        'precision': float(all_metrics[name]['precision']),
        'recall': float(all_metrics[name]['recall']),
        'f1_score': float(all_metrics[name]['f1_score']),
        'auc_roc': float(all_metrics[name].get('auc_roc', 0))
    }

for name in ['MLP Multi', 'CNN Multi']:
    results_summary['multi'][name] = {
        'accuracy': float(all_metrics[name]['accuracy']),
        'precision': float(all_metrics[name]['precision']),
        'recall': float(all_metrics[name]['recall']),
        'f1_score': float(all_metrics[name]['f1_score']),
        'auc_roc': float(all_metrics[name].get('auc_roc', 0))
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
accuracies = [all_metrics[name]['accuracy'] for name in model_names]
f1_scores = [all_metrics[name]['f1_score'] for name in model_names]

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
precisions = [all_metrics[name]['precision'] for name in model_names]
recalls = [all_metrics[name]['recall'] for name in model_names]

bars3 = axes[1, 1].bar(x_pos - width/2, precisions, width, label='Precision', color=colors, alpha=0.8)
bars4 = axes[1, 1].bar(x_pos + width/2, recalls, width, label='Recall', color=colors, alpha=0.6)

axes[1, 1].set_title('Precision vs Recall', fontsize=12, fontweight='bold')
axes[1, 1].set_ylabel('Score')
axes[1, 1].set_xticks(x_pos)
axes[1, 1].set_xticklabels(model_names, rotation=45, ha='right')
axes[1, 1].legend()
axes[1, 1].set_ylim(0, 1.1)

# Plot 5: Confusion Matrix - Best Binary
best_binary = 'MLP Binary' if all_metrics['MLP Binary']['f1_score'] > all_metrics['CNN Binary']['f1_score'] else 'CNN Binary'
y_pred_best = all_metrics[best_binary]['predictions']
cm = confusion_matrix(y_test_bin, y_pred_best)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[2, 0],
            xticklabels=['Normal', 'Attack'], yticklabels=['Normal', 'Attack'])
axes[2, 0].set_title(f'Confusion Matrix - {best_binary}', fontsize=12, fontweight='bold')
axes[2, 0].set_ylabel('True Label')
axes[2, 0].set_xlabel('Predicted Label')

# Plot 6: All Metrics Summary
metrics_data = []
for name in model_names:
    metrics_data.append([
        all_metrics[name]['accuracy'],
        all_metrics[name]['precision'],
        all_metrics[name]['recall'],
        all_metrics[name]['f1_score']
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
    f.write(f"- **Alpha (Dirichlet)**: {ALPHA}\n")
    f.write(f"- **Number of Rounds**: {NUM_ROUNDS}\n")
    f.write(f"- **Number of Clients**: {NUM_CLIENTS}\n\n")
    
    f.write("## Results Summary\n\n")
    f.write("### Binary Classification\n\n")
    f.write("| Model | Accuracy | Precision | Recall | F1-Score | AUC-ROC |\n")
    f.write("|-------|----------|-----------|--------|----------|----------|\n")
    for name in ['MLP Binary', 'CNN Binary']:
        m = all_metrics[name]
        f.write(f"| {name} | {m['accuracy']:.4f} | {m['precision']:.4f} | "
               f"{m['recall']:.4f} | {m['f1_score']:.4f} | {m.get('auc_roc', 0):.4f} |\n")
    
    f.write("\n### Multi-class Classification\n\n")
    f.write("| Model | Accuracy | Precision | Recall | F1-Score | AUC-ROC |\n")
    f.write("|-------|----------|-----------|--------|----------|----------|\n")
    for name in ['MLP Multi', 'CNN Multi']:
        m = all_metrics[name]
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
print(f"\nBest Binary Model: {best_binary}")
print(f"  - F1-Score: {all_metrics[best_binary]['f1_score']:.4f}")
print(f"  - Accuracy: {all_metrics[best_binary]['accuracy']:.4f}")

best_multi = 'MLP Multi' if all_metrics['MLP Multi']['f1_score'] > all_metrics['CNN Multi']['f1_score'] else 'CNN Multi'
print(f"\nBest Multi-class Model: {best_multi}")
print(f"  - F1-Score: {all_metrics[best_multi]['f1_score']:.4f}")
print(f"  - Accuracy: {all_metrics[best_multi]['accuracy']:.4f}")

print("\n" + "="*80 + "\n")
