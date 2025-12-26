# Federated Learning Hyperparameter Grid Search - Summary Report

**Date**: 2025-12-10 12:03:53

**Total Experiments**: 24

## Executive Summary

- ✅ **Completed**: 24/24
- ❌ **Failed**: 0/24
- ⏱️ **Total Time**: 5.01 hours (300.9 minutes)
- 📊 **Avg Time per Experiment**: 12.5 minutes

## Grid Search Configuration

```python
BATCH_SIZES = [256, 512, 1024]
LOCAL_EPOCHS = [1, 2]
LEARNING_RATES = [0.001, 0.0005]
ALPHAS = [0.3, 5.0]
Total Combinations = 24
```

## All Experiments

| # | Experiment Name | Batch Size | Epochs | Learning Rate | Alpha | Status | Duration (min) |
|---|----------------|------------|--------|---------------|-------|--------|----------------|
| 1 | `bs256_epoch1_lr0p0010_alpha0p3` | 256 | 1 | 0.001 | 0.3 | ✅ completed | 10.3 |
| 2 | `bs256_epoch1_lr0p0010_alpha5p0` | 256 | 1 | 0.001 | 5.0 | ✅ completed | 10.4 |
| 3 | `bs256_epoch1_lr0p0005_alpha0p3` | 256 | 1 | 0.0005 | 0.3 | ✅ completed | 10.1 |
| 4 | `bs256_epoch1_lr0p0005_alpha5p0` | 256 | 1 | 0.0005 | 5.0 | ✅ completed | 10.4 |
| 5 | `bs256_epoch2_lr0p0010_alpha0p3` | 256 | 2 | 0.001 | 0.3 | ✅ completed | 15.1 |
| 6 | `bs256_epoch2_lr0p0010_alpha5p0` | 256 | 2 | 0.001 | 5.0 | ✅ completed | 14.2 |
| 7 | `bs256_epoch2_lr0p0005_alpha0p3` | 256 | 2 | 0.0005 | 0.3 | ✅ completed | 14.7 |
| 8 | `bs256_epoch2_lr0p0005_alpha5p0` | 256 | 2 | 0.0005 | 5.0 | ✅ completed | 14.2 |
| 9 | `bs512_epoch1_lr0p0010_alpha0p3` | 512 | 1 | 0.001 | 0.3 | ✅ completed | 10.0 |
| 10 | `bs512_epoch1_lr0p0010_alpha5p0` | 512 | 1 | 0.001 | 5.0 | ✅ completed | 10.5 |
| 11 | `bs512_epoch1_lr0p0005_alpha0p3` | 512 | 1 | 0.0005 | 0.3 | ✅ completed | 10.1 |
| 12 | `bs512_epoch1_lr0p0005_alpha5p0` | 512 | 1 | 0.0005 | 5.0 | ✅ completed | 10.3 |
| 13 | `bs512_epoch2_lr0p0010_alpha0p3` | 512 | 2 | 0.001 | 0.3 | ✅ completed | 14.8 |
| 14 | `bs512_epoch2_lr0p0010_alpha5p0` | 512 | 2 | 0.001 | 5.0 | ✅ completed | 14.6 |
| 15 | `bs512_epoch2_lr0p0005_alpha0p3` | 512 | 2 | 0.0005 | 0.3 | ✅ completed | 15.0 |
| 16 | `bs512_epoch2_lr0p0005_alpha5p0` | 512 | 2 | 0.0005 | 5.0 | ✅ completed | 14.7 |
| 17 | `bs1024_epoch1_lr0p0010_alpha0p3` | 1024 | 1 | 0.001 | 0.3 | ✅ completed | 10.0 |
| 18 | `bs1024_epoch1_lr0p0010_alpha5p0` | 1024 | 1 | 0.001 | 5.0 | ✅ completed | 10.4 |
| 19 | `bs1024_epoch1_lr0p0005_alpha0p3` | 1024 | 1 | 0.0005 | 0.3 | ✅ completed | 10.1 |
| 20 | `bs1024_epoch1_lr0p0005_alpha5p0` | 1024 | 1 | 0.0005 | 5.0 | ✅ completed | 10.2 |
| 21 | `bs1024_epoch2_lr0p0010_alpha0p3` | 1024 | 2 | 0.001 | 0.3 | ✅ completed | 14.9 |
| 22 | `bs1024_epoch2_lr0p0010_alpha5p0` | 1024 | 2 | 0.001 | 5.0 | ✅ completed | 15.2 |
| 23 | `bs1024_epoch2_lr0p0005_alpha0p3` | 1024 | 2 | 0.0005 | 0.3 | ✅ completed | 15.1 |
| 24 | `bs1024_epoch2_lr0p0005_alpha5p0` | 1024 | 2 | 0.0005 | 5.0 | ✅ completed | 15.6 |

## Performance Comparison

### Binary Classification Results

| Experiment | Batch Size | Epochs | LR | Alpha | MLP Acc | MLP F1 | CNN Acc | CNN F1 |
|------------|------------|--------|-----|-------|---------|--------|---------|--------|
| `bs256_epoch1_lr0p0010_alpha0p3` | 256 | 1 | 0.001 | 0.3 | 0.9552 | 0.9714 | 0.9573 | 0.9727 |
| `bs256_epoch1_lr0p0010_alpha5p0` | 256 | 1 | 0.001 | 5.0 | 0.9563 | 0.9720 | 0.9676 | 0.9785 |
| `bs256_epoch1_lr0p0005_alpha0p3` | 256 | 1 | 0.0005 | 0.3 | 0.9500 | 0.9682 | 0.9572 | 0.9727 |
| `bs256_epoch1_lr0p0005_alpha5p0` | 256 | 1 | 0.0005 | 5.0 | 0.9568 | 0.9724 | 0.9593 | 0.9739 |
| `bs256_epoch2_lr0p0010_alpha0p3` | 256 | 2 | 0.001 | 0.3 | 0.9546 | 0.9710 | 0.8891 | 0.9222 |
| `bs256_epoch2_lr0p0010_alpha5p0` | 256 | 2 | 0.001 | 5.0 | 0.9662 | 0.9776 | 0.9688 | 0.9792 |
| `bs256_epoch2_lr0p0005_alpha0p3` | 256 | 2 | 0.0005 | 0.3 | 0.9561 | 0.9720 | 0.9574 | 0.9728 |
| `bs256_epoch2_lr0p0005_alpha5p0` | 256 | 2 | 0.0005 | 5.0 | 0.9658 | 0.9774 | 0.9558 | 0.9717 |
| `bs512_epoch1_lr0p0010_alpha0p3` | 512 | 1 | 0.001 | 0.3 | 0.9562 | 0.9721 | 0.9560 | 0.9719 |
| `bs512_epoch1_lr0p0010_alpha5p0` | 512 | 1 | 0.001 | 5.0 | 0.9567 | 0.9724 | 0.9657 | 0.9772 |
| `bs512_epoch1_lr0p0005_alpha0p3` | 512 | 1 | 0.0005 | 0.3 | 0.9562 | 0.9720 | 0.9571 | 0.9726 |
| `bs512_epoch1_lr0p0005_alpha5p0` | 512 | 1 | 0.0005 | 5.0 | 0.9568 | 0.9724 | 0.9667 | 0.9779 |
| `bs512_epoch2_lr0p0010_alpha0p3` | 512 | 2 | 0.001 | 0.3 | 0.9568 | 0.9724 | 0.8644 | 0.9180 |
| `bs512_epoch2_lr0p0010_alpha5p0` | 512 | 2 | 0.001 | 5.0 | 0.9661 | 0.9776 | 0.9421 | 0.9608 |
| `bs512_epoch2_lr0p0005_alpha0p3` | 512 | 2 | 0.0005 | 0.3 | 0.9562 | 0.9720 | 0.9048 | 0.9413 |
| `bs512_epoch2_lr0p0005_alpha5p0` | 512 | 2 | 0.0005 | 5.0 | 0.9570 | 0.9725 | 0.9660 | 0.9774 |
| `bs1024_epoch1_lr0p0010_alpha0p3` | 1024 | 1 | 0.001 | 0.3 | 0.9555 | 0.9716 | 0.9553 | 0.9714 |
| `bs1024_epoch1_lr0p0010_alpha5p0` | 1024 | 1 | 0.001 | 5.0 | 0.9569 | 0.9725 | 0.9492 | 0.9658 |
| `bs1024_epoch1_lr0p0005_alpha0p3` | 1024 | 1 | 0.0005 | 0.3 | 0.9539 | 0.9706 | 0.9573 | 0.9727 |
| `bs1024_epoch1_lr0p0005_alpha5p0` | 1024 | 1 | 0.0005 | 5.0 | 0.9569 | 0.9725 | 0.9632 | 0.9755 |
| `bs1024_epoch2_lr0p0010_alpha0p3` | 1024 | 2 | 0.001 | 0.3 | 0.9553 | 0.9715 | 0.9578 | 0.9730 |
| `bs1024_epoch2_lr0p0010_alpha5p0` | 1024 | 2 | 0.001 | 5.0 | 0.9569 | 0.9724 | 0.9669 | 0.9781 |
| `bs1024_epoch2_lr0p0005_alpha0p3` | 1024 | 2 | 0.0005 | 0.3 | 0.9556 | 0.9717 | 0.9580 | 0.9731 |
| `bs1024_epoch2_lr0p0005_alpha5p0` | 1024 | 2 | 0.0005 | 5.0 | 0.9570 | 0.9725 | 0.9674 | 0.9784 |

### Multi-class Classification Results

| Experiment | Batch Size | Epochs | LR | Alpha | MLP Acc | MLP F1 | CNN Acc | CNN F1 |
|------------|------------|--------|-----|-------|---------|--------|---------|--------|
| `bs256_epoch1_lr0p0010_alpha0p3` | 256 | 1 | 0.001 | 0.3 | 0.7111 | 0.6831 | 0.4319 | 0.3299 |
| `bs256_epoch1_lr0p0010_alpha5p0` | 256 | 1 | 0.001 | 5.0 | 0.7621 | 0.7508 | 0.6057 | 0.5389 |
| `bs256_epoch1_lr0p0005_alpha0p3` | 256 | 1 | 0.0005 | 0.3 | 0.6716 | 0.6349 | 0.7223 | 0.6973 |
| `bs256_epoch1_lr0p0005_alpha5p0` | 256 | 1 | 0.0005 | 5.0 | 0.7345 | 0.7181 | 0.7807 | 0.7637 |
| `bs256_epoch2_lr0p0010_alpha0p3` | 256 | 2 | 0.001 | 0.3 | 0.6936 | 0.6626 | 0.5229 | 0.4581 |
| `bs256_epoch2_lr0p0010_alpha5p0` | 256 | 2 | 0.001 | 5.0 | 0.7709 | 0.7637 | 0.6190 | 0.5813 |
| `bs256_epoch2_lr0p0005_alpha0p3` | 256 | 2 | 0.0005 | 0.3 | 0.7102 | 0.6825 | 0.7098 | 0.6626 |
| `bs256_epoch2_lr0p0005_alpha5p0` | 256 | 2 | 0.0005 | 5.0 | 0.7795 | 0.7742 | 0.5747 | 0.4864 |
| `bs512_epoch1_lr0p0010_alpha0p3` | 512 | 1 | 0.001 | 0.3 | 0.6723 | 0.6357 | 0.4522 | 0.3625 |
| `bs512_epoch1_lr0p0010_alpha5p0` | 512 | 1 | 0.001 | 5.0 | 0.7524 | 0.7428 | 0.5967 | 0.5526 |
| `bs512_epoch1_lr0p0005_alpha0p3` | 512 | 1 | 0.0005 | 0.3 | 0.6677 | 0.6312 | 0.7327 | 0.7099 |
| `bs512_epoch1_lr0p0005_alpha5p0` | 512 | 1 | 0.0005 | 5.0 | 0.7330 | 0.7228 | 0.7588 | 0.7461 |
| `bs512_epoch2_lr0p0010_alpha0p3` | 512 | 2 | 0.001 | 0.3 | 0.7118 | 0.6814 | 0.7555 | 0.7347 |
| `bs512_epoch2_lr0p0010_alpha5p0` | 512 | 2 | 0.001 | 5.0 | 0.7905 | 0.7846 | 0.4025 | 0.3058 |
| `bs512_epoch2_lr0p0005_alpha0p3` | 512 | 2 | 0.0005 | 0.3 | 0.7047 | 0.6673 | 0.7146 | 0.6668 |
| `bs512_epoch2_lr0p0005_alpha5p0` | 512 | 2 | 0.0005 | 5.0 | 0.7827 | 0.7770 | 0.7713 | 0.7502 |
| `bs1024_epoch1_lr0p0010_alpha0p3` | 1024 | 1 | 0.001 | 0.3 | 0.6635 | 0.6206 | 0.6547 | 0.5941 |
| `bs1024_epoch1_lr0p0010_alpha5p0` | 1024 | 1 | 0.001 | 5.0 | 0.7119 | 0.6782 | 0.5681 | 0.4538 |
| `bs1024_epoch1_lr0p0005_alpha0p3` | 1024 | 1 | 0.0005 | 0.3 | 0.6834 | 0.6536 | 0.7104 | 0.6814 |
| `bs1024_epoch1_lr0p0005_alpha5p0` | 1024 | 1 | 0.0005 | 5.0 | 0.6926 | 0.6473 | 0.6115 | 0.5717 |
| `bs1024_epoch2_lr0p0010_alpha0p3` | 1024 | 2 | 0.001 | 0.3 | 0.7042 | 0.6720 | 0.7511 | 0.7296 |
| `bs1024_epoch2_lr0p0010_alpha5p0` | 1024 | 2 | 0.001 | 5.0 | 0.7779 | 0.7716 | 0.8005 | 0.7946 |
| `bs1024_epoch2_lr0p0005_alpha0p3` | 1024 | 2 | 0.0005 | 0.3 | 0.6762 | 0.6384 | 0.7475 | 0.7317 |
| `bs1024_epoch2_lr0p0005_alpha5p0` | 1024 | 2 | 0.0005 | 5.0 | 0.7383 | 0.7312 | 0.7405 | 0.7040 |

## Best Configurations

### Binary Classification

**Best MLP Binary (Accuracy)**: `bs256_epoch2_lr0p0010_alpha5p0`
- Parameters: {'batch_size': 256, 'local_epochs': 2, 'learning_rate': 0.001, 'alpha': 5.0}
- Accuracy: 0.9662
- F1-Score: 0.9776

**Best CNN Binary (F1-Score)**: `bs256_epoch2_lr0p0010_alpha5p0`
- Parameters: {'batch_size': 256, 'local_epochs': 2, 'learning_rate': 0.001, 'alpha': 5.0}
- Accuracy: 0.9688
- F1-Score: 0.9792

### Multi-class Classification

**Best MLP Multi (Accuracy)**: `bs512_epoch2_lr0p0010_alpha5p0`
- Parameters: {'batch_size': 512, 'local_epochs': 2, 'learning_rate': 0.001, 'alpha': 5.0}
- Accuracy: 0.7905
- F1-Score: 0.7846

**Best CNN Multi (F1-Score)**: `bs1024_epoch2_lr0p0010_alpha5p0`
- Parameters: {'batch_size': 1024, 'local_epochs': 2, 'learning_rate': 0.001, 'alpha': 5.0}
- Accuracy: 0.8005
- F1-Score: 0.7946

## Hyperparameter Impact Analysis

### Batch Size Impact

Analysis of how different batch sizes affect model performance.

- **Batch Size 256**: Avg Binary Accuracy = 0.9576 (8 experiments)
- **Batch Size 512**: Avg Binary Accuracy = 0.9578 (8 experiments)
- **Batch Size 1024**: Avg Binary Accuracy = 0.9560 (8 experiments)

### Local Epochs Impact

Analysis of how different local epochs affect model performance.

- **1 Epoch(s)**: Avg Binary Accuracy = 0.9556 (12 experiments)
- **2 Epoch(s)**: Avg Binary Accuracy = 0.9586 (12 experiments)

### Learning Rate Impact

Analysis of how different learning rates affect model performance.

- **Learning Rate 0.001**: Avg Binary Accuracy = 0.9577 (12 experiments)
- **Learning Rate 0.0005**: Avg Binary Accuracy = 0.9565 (12 experiments)

## Recommendations

Based on the grid search results:

1. **Optimal Configuration for Binary Classification**:
   - Use configuration from: `bs256_epoch2_lr0p0010_alpha5p0`
   - Parameters: {'batch_size': 256, 'local_epochs': 2, 'learning_rate': 0.001, 'alpha': 5.0}

2. **Optimal Configuration for Multi-class Classification**:
   - Use configuration from: `bs1024_epoch2_lr0p0010_alpha5p0`
   - Parameters: {'batch_size': 1024, 'local_epochs': 2, 'learning_rate': 0.001, 'alpha': 5.0}

3. **Training Time vs Performance Trade-off**:
   - Review the duration column to balance accuracy with training time
   - Consider faster configurations if performance difference is minimal

## Experiment Directory Structure

```
gridsearch_research/
├── all_experiments.json          # Complete experiment tracking
├── summary_report.md             # This file
├── bs256_epoch1_lr0p0010_alpha0p3/
│   ├── experiment_log.txt        # Detailed execution log
│   ├── results_summary.json      # Metrics and results
│   ├── experiment_report.md      # Individual report
│   ├── plots/                    # Visualization plots
│   └── models/                   # Saved models
├── bs256_epoch1_lr0p0010_alpha5p0/
│   ├── experiment_log.txt        # Detailed execution log
│   ├── results_summary.json      # Metrics and results
│   ├── experiment_report.md      # Individual report
│   ├── plots/                    # Visualization plots
│   └── models/                   # Saved models
├── bs256_epoch1_lr0p0005_alpha0p3/
│   ├── experiment_log.txt        # Detailed execution log
│   ├── results_summary.json      # Metrics and results
│   ├── experiment_report.md      # Individual report
│   ├── plots/                    # Visualization plots
│   └── models/                   # Saved models
└── ...
```

## Conclusion

Grid search completed with 24 successful experiments out of 24 total.
Review individual experiment reports in each subdirectory for detailed analysis.

---
*Report generated on 2025-12-10 at 12:03:53*
