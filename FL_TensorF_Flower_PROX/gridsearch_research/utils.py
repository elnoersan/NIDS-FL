"""Utility functions for Federated Learning with Flower and FedProx.

This module contains helper functions for data splitting, evaluation, and visualization.
"""

import numpy as np
import pandas as pd
from typing import List, Tuple, Dict, Any
from sklearn.metrics import (
    classification_report, accuracy_score, f1_score, 
    precision_score, recall_score, confusion_matrix,
    roc_auc_score, roc_curve
)
try:
    from IPython.display import display, HTML
except Exception:
    display = None
    HTML = None


def split_data_non_iid_label(
    X: np.ndarray, 
    y: np.ndarray, 
    n_clients: int = 3, 
    alpha: float = 0.4
) -> List[Tuple[np.ndarray, np.ndarray]]:
    """
    Split data for clients with Non-IID distribution using Dirichlet distribution.

    Parameters
    ----------
    X : np.ndarray, shape (n_samples, n_features)
        Feature data.
    y : np.ndarray, shape (n_samples,)
        Class labels.
    n_clients : int, default=3
        Number of clients (partitions) desired.
    alpha : float, default=0.4
        Dirichlet concentration parameter. Smaller values → more non-uniform distribution.

    Returns
    -------
    List[Tuple[np.ndarray, np.ndarray]]
        Each element is (X_client, y_client) for one client, shuffled.
    """
    print(f"\n[INFO] Splitting data for {n_clients} clients with Non-IID (alpha={alpha})...")

    # Ensure data is in numpy array format
    X_np = X if isinstance(X, np.ndarray) else X.to_numpy()
    y_np = y if isinstance(y, np.ndarray) else y.to_numpy()

    # Original label distribution
    unique_labels, counts = np.unique(y_np, return_counts=True)

    # Allocate indices to each client (based on Dirichlet)
    client_indices = [[] for _ in range(n_clients)]

    for label_idx, label in enumerate(unique_labels):
        # Indices of samples with this label
        label_indices = np.where(y_np == label)[0]
        np.random.shuffle(label_indices)

        # Proportions to allocate to each client
        proportions = np.random.dirichlet(np.repeat(alpha, n_clients))

        # Scale proportions to the number of samples for this label
        proportions = proportions / proportions.sum() * counts[label_idx]
        proportions = np.round(proportions).astype(int)

        # Adjust for rounding differences
        diff = counts[label_idx] - proportions.sum()
        if diff != 0:
            proportions[np.random.choice(n_clients)] += diff

        # Distribute indices to each client
        start = 0
        for i in range(n_clients):
            end = start + proportions[i]
            client_indices[i].extend(label_indices[start:end])
            start = end

    # Create list of (X_client, y_client) for each client
    final_client_data = []

    for i in range(n_clients):
        if not client_indices[i]:
            # If client gets no data, give 10 random samples
            print(f"    Warning: Client {i+1} received no data. Giving 10 random samples.")
            random_indices = np.random.choice(len(X_np), 10, replace=False)
            X_client, y_client = X_np[random_indices], y_np[random_indices]
        else:
            # Remove duplicate indices and get data
            indices = list(set(client_indices[i]))
            X_client, y_client = X_np[indices], y_np[indices]

        # Shuffle client data locally
        shuffle_idx = np.random.permutation(len(X_client))
        X_client = X_client[shuffle_idx]
        y_client = y_client[shuffle_idx]

        final_client_data.append((X_client, y_client))

        # Display brief statistics per client
        unique, cnts = np.unique(y_client, return_counts=True)
        print(
            f"    Client {i+1}: {len(X_client):>4} samples, "
            f"distribution: {dict(zip(unique, cnts))}"
        )

    # Jika data bersifat binary, tampilkan tabel distribusi per klien secara HTML
    try:
        # Coba ambil label unik dari seluruh data
        unique_labels_all, _ = np.unique(y_np, return_counts=True)
        if len(unique_labels_all) == 2:
            label0 = unique_labels_all[0]
            label1 = unique_labels_all[1]
            rows_summary = []
            total_samples = 0
            total_label0 = 0
            total_label1 = 0
            for idx, (Xc, yc) in enumerate(final_client_data):
                total = len(yc)
                cnt0 = int((yc == label0).sum())
                cnt1 = int((yc == label1).sum())
                total_samples += total
                total_label0 += cnt0
                total_label1 += cnt1
                rows_summary.append({
                    'Client': f'Client {idx+1}',
                    'Total Samples': total,
                    'Normal': cnt0,
                    'Normal %': 100.0 * cnt0 / total if total > 0 else 0.0,
                    'Attack': cnt1,
                    'Attack %': 100.0 * cnt1 / total if total > 0 else 0.0,
                })

            df_dist = pd.DataFrame(rows_summary)
            # add TOTAL row
            df_dist = df_dist.append({
                'Client': 'TOTAL',
                'Total Samples': total_samples,
                'Normal': total_label0,
                'Normal %': '-',
                'Attack': total_label1,
                'Attack %': '-'
            }, ignore_index=True)

            # Heterogeneity metrics
            attack_ratios = df_dist.loc[df_dist['Client'] != 'TOTAL', 'Attack %'] / 100.0
            attack_range = (attack_ratios.min(), attack_ratios.max()) if len(attack_ratios) > 0 else (0, 0)
            attack_std = float(attack_ratios.std()) if len(attack_ratios) > 0 else 0.0

            if display is not None and HTML is not None:
                html = '<h3 style="margin-bottom:6px;">DISTRIBUSI BINARY DATA PER KLIEN</h3>'
                html += df_dist.to_html(index=False, justify='left')
                html += '<pre style="margin-top:8px;">\nHETEROGENEITY METRICS:\n'
                html += f"  - Attack ratio range: {attack_range[0]:.3f} - {attack_range[1]:.3f}\n"
                html += f"  - Attack ratio std dev: {attack_std:.3f}\n"
                html += '</pre>'
                display(HTML(html))
    except Exception:
        # Jangan ganggu alur jika ada masalah pembuatan tabel HTML
        pass

    return final_client_data


def evaluate_model_metrics(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    model_name: str,
    is_binary: bool = True,
    target_names: List[str] = None,
    y_pred_proba: np.ndarray = None
) -> Dict[str, Any]:
    """Evaluate model with comprehensive metrics including AUC-ROC.
    
    Args:
        y_true: True labels
        y_pred: Predicted labels
        model_name: Name of the model for display
        is_binary: Whether this is binary classification
        target_names: Names of target classes
        y_pred_proba: Predicted probabilities for AUC-ROC calculation
        
    Returns:
        Dictionary of metrics
    """
    # Determine averaging method
    average_method = 'binary' if is_binary else 'weighted'
    
    # Calculate metrics
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average=average_method, zero_division=0)
    recall = recall_score(y_true, y_pred, average=average_method, zero_division=0)
    f1 = f1_score(y_true, y_pred, average=average_method, zero_division=0)
    
    # Calculate AUC-ROC if probabilities provided
    auc_roc = None
    if y_pred_proba is not None:
        try:
            if is_binary:
                # For binary classification, use probability of positive class
                if len(y_pred_proba.shape) > 1:
                    y_score = y_pred_proba[:, 1] if y_pred_proba.shape[1] > 1 else y_pred_proba[:, 0]
                else:
                    y_score = y_pred_proba
                auc_roc = roc_auc_score(y_true, y_score)
            else:
                # For multi-class, use one-vs-rest
                auc_roc = roc_auc_score(y_true, y_pred_proba, multi_class='ovr', average='weighted')
        except Exception as e:
            print(f"   Warning: Could not calculate AUC-ROC: {e}")
            auc_roc = None
    
    # Print results
    print(f"\nEVALUATION METRICS - {model_name}:")
    print(f"   - Accuracy: {accuracy:.4f}")
    print(f"   - Precision: {precision:.4f}")
    print(f"   - Recall: {recall:.4f}")
    print(f"   - F1 Score: {f1:.4f}")
    if auc_roc is not None:
        print(f"   - AUC-ROC: {auc_roc:.4f}")
    
    # Print classification report if target names provided
    if target_names is not None:
        print(f"\nCLASSIFICATION REPORT:")
        print(classification_report(y_true, y_pred, target_names=target_names, zero_division=0))
    
    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1_score': f1,
        'auc_roc': auc_roc if auc_roc is not None else 0.0,
        'predictions': y_pred
    }


def prepare_client_configs(
    client_data: List[Tuple[np.ndarray, np.ndarray]],
    test_data: Tuple[np.ndarray, np.ndarray] = None
) -> List[Dict[str, Any]]:
    """Prepare node configurations for Flower clients.
    
    Args:
        client_data: List of (X_train, y_train) tuples for each client
        test_data: Optional tuple of (X_test, y_test) for global evaluation
        
    Returns:
        List of node configuration dictionaries
    """
    node_configs = []
    
    for i, (X_train, y_train) in enumerate(client_data):
        config = {
            "partition-id": i,
            "X_train": X_train,
            "y_train": y_train,
        }
        
        # Add test data if provided
        if test_data is not None:
            X_test, y_test = test_data
            config["X_test"] = X_test
            config["y_test"] = y_test
        
        node_configs.append(config)
    
    return node_configs


def extract_metrics_from_history(history: Dict[str, Any]) -> Dict[str, List[float]]:
    """Extract and organize metrics from Flower training history.
    
    Args:
        history: History object returned from Flower strategy
        
    Returns:
        Dictionary with organized metrics
    """
    metrics = {
        'train_accuracy': [],
        'train_loss': [],
        'eval_accuracy': [],
        'eval_loss': [],
    }
    
    # Extract metrics from history
    # This will be filled during actual training
    
    return metrics


def print_summary_table(results: Dict[str, Dict[str, float]]) -> None:
    """Print a formatted summary table of all model results.
    
    Args:
        results: Dictionary mapping model names to their metrics
    """
    # Build DataFrame for pretty display (and HTML)
    rows = []
    for model_name, metrics in results.items():
        rows.append({
            'Model': model_name,
            'Accuracy': metrics.get('accuracy', 0.0),
            'Precision': metrics.get('precision', 0.0),
            'Recall': metrics.get('recall', 0.0),
            'F1-Score': metrics.get('f1_score', 0.0),
            'AUC-ROC': metrics.get('auc_roc', 0.0),
        })

    df = pd.DataFrame(rows).set_index('Model')
    df = df.sort_values(by='F1-Score', ascending=False)

    # Try to display as HTML in notebooks, otherwise print plain text
    try:
        if display is not None and HTML is not None:
            html = '<h3>SUMMARY OF ALL MODELS (FedProx)</h3>'
            html += df.to_html(float_format='%.4f')
            # Best models
            best_f1_model = max(results.items(), key=lambda x: x[1]['f1_score'])
            best_recall_model = max(results.items(), key=lambda x: x[1]['recall'])
            best_auc_model = max(results.items(), key=lambda x: x[1].get('auc_roc', 0))
            html += '<pre style="margin-top:8px;">\nBEST MODELS:\n'
            html += f"   - Highest F1 Score: {best_f1_model[0]} (F1: {best_f1_model[1]['f1_score']:.4f})\n"
            html += f"   - Highest Recall: {best_recall_model[0]} (Recall: {best_recall_model[1]['recall']:.4f})\n"
            html += f"   - Highest AUC-ROC: {best_auc_model[0]} (AUC: {best_auc_model[1].get('auc_roc', 0):.4f})\n"
            html += '</pre>'
            display(HTML(html))
            return
    except Exception:
        pass

    # Fallback to plain text
    print('\n' + '='*80)
    print('SUMMARY OF ALL MODELS (FedProx)')
    print('='*80)
    print(df.to_string(float_format=lambda x: f"{x:.4f}"))
