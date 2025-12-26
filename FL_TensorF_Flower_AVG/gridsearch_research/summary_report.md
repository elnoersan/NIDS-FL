# Federated Learning Hyperparameter Grid Search - Summary Report

**Date**: 2025-12-09 12:07:18

**Total Experiments**: 2

## Executive Summary

- ✅ **Completed**: 2/2
- ❌ **Failed**: 0/2
- ⏱️ **Total Time**: 0.07 hours (4.0 minutes)
- 📊 **Avg Time per Experiment**: 2.0 minutes

## Grid Search Configuration

```python
BATCH_SIZES = [256]
LOCAL_EPOCHS = [1]
LEARNING_RATES = [0.001, 0.0005]
Total Combinations = 2
```

## All Experiments

| # | Experiment Name | Batch Size | Epochs | Learning Rate | Status | Duration (min) |
|---|----------------|------------|--------|---------------|--------|----------------|
| 1 | `bs256_epoch1_lr0p0010` | 256 | 1 | 0.001 | ✅ completed | 2.1 |
| 2 | `bs256_epoch1_lr0p0005` | 256 | 1 | 0.0005 | ✅ completed | 1.9 |

## Performance Comparison

### Binary Classification Results

| Experiment | Batch Size | Epochs | LR | MLP Acc | MLP F1 | CNN Acc | CNN F1 |
|------------|------------|--------|-----|---------|--------|---------|--------|
| `bs256_epoch1_lr0p0010` | 256 | 1 | 0.001 | 0.4440 | 0.5772 | 0.6701 | 0.7850 |
| `bs256_epoch1_lr0p0005` | 256 | 1 | 0.0005 | 0.2750 | 0.1882 | 0.2369 | 0.0000 |

### Multi-class Classification Results

| Experiment | Batch Size | Epochs | LR | MLP Acc | MLP F1 | CNN Acc | CNN F1 |
|------------|------------|--------|-----|---------|--------|---------|--------|
| `bs256_epoch1_lr0p0010` | 256 | 1 | 0.001 | 0.0945 | 0.0212 | 0.0232 | 0.0088 |
| `bs256_epoch1_lr0p0005` | 256 | 1 | 0.0005 | 0.0176 | 0.0138 | 0.0950 | 0.0191 |

## Best Configurations

### Binary Classification

**Best MLP Binary (Accuracy)**: `bs256_epoch1_lr0p0010`
- Parameters: {'batch_size': 256, 'local_epochs': 1, 'learning_rate': 0.001}
- Accuracy: 0.4440
- F1-Score: 0.5772

**Best CNN Binary (F1-Score)**: `bs256_epoch1_lr0p0010`
- Parameters: {'batch_size': 256, 'local_epochs': 1, 'learning_rate': 0.001}
- Accuracy: 0.6701
- F1-Score: 0.7850

### Multi-class Classification

**Best MLP Multi (Accuracy)**: `bs256_epoch1_lr0p0010`
- Parameters: {'batch_size': 256, 'local_epochs': 1, 'learning_rate': 0.001}
- Accuracy: 0.0945
- F1-Score: 0.0212

**Best CNN Multi (F1-Score)**: `bs256_epoch1_lr0p0005`
- Parameters: {'batch_size': 256, 'local_epochs': 1, 'learning_rate': 0.0005}
- Accuracy: 0.0950
- F1-Score: 0.0191

## Hyperparameter Impact Analysis

### Batch Size Impact

Analysis of how different batch sizes affect model performance.

- **Batch Size 256**: Avg Binary Accuracy = 0.3595 (2 experiments)

### Local Epochs Impact

Analysis of how different local epochs affect model performance.

- **1 Epoch(s)**: Avg Binary Accuracy = 0.3595 (2 experiments)

### Learning Rate Impact

Analysis of how different learning rates affect model performance.

- **Learning Rate 0.001**: Avg Binary Accuracy = 0.4440 (1 experiments)
- **Learning Rate 0.0005**: Avg Binary Accuracy = 0.2750 (1 experiments)

## Recommendations

Based on the grid search results:

1. **Optimal Configuration for Binary Classification**:
   - Use configuration from: `bs256_epoch1_lr0p0010`
   - Parameters: {'batch_size': 256, 'local_epochs': 1, 'learning_rate': 0.001}

2. **Optimal Configuration for Multi-class Classification**:
   - Use configuration from: `bs256_epoch1_lr0p0005`
   - Parameters: {'batch_size': 256, 'local_epochs': 1, 'learning_rate': 0.0005}

3. **Training Time vs Performance Trade-off**:
   - Review the duration column to balance accuracy with training time
   - Consider faster configurations if performance difference is minimal

## Experiment Directory Structure

```
gridsearch_research/
├── all_experiments.json          # Complete experiment tracking
├── summary_report.md             # This file
├── bs256_epoch1_lr0p0010/
│   ├── experiment_log.txt        # Detailed execution log
│   ├── results_summary.json      # Metrics and results
│   ├── experiment_report.md      # Individual report
│   ├── plots/                    # Visualization plots
│   └── models/                   # Saved models
├── bs256_epoch1_lr0p0005/
│   ├── experiment_log.txt        # Detailed execution log
│   ├── results_summary.json      # Metrics and results
│   ├── experiment_report.md      # Individual report
│   ├── plots/                    # Visualization plots
│   └── models/                   # Saved models
└── ...
```

## Conclusion

Grid search completed with 2 successful experiments out of 2 total.
Review individual experiment reports in each subdirectory for detailed analysis.

---
*Report generated on 2025-12-09 at 12:07:18*
