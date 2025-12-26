# Experiment Report: bs256_epoch2_lr0p0005_alpha5p0

**Date**: 2025-12-10 08:42:20

## Hyperparameters

- **Batch Size**: 256
- **Local Epochs**: 2
- **Learning Rate**: 0.0005
- **Alpha (Dirichlet)**: 5.0
- **Number of Rounds**: 20
- **Number of Clients**: 5

## Results Summary

### Binary Classification

| Model | Accuracy | Precision | Recall | F1-Score | AUC-ROC |
|-------|----------|-----------|--------|----------|----------|
| MLP Binary | 0.9658 | 0.9889 | 0.9661 | 0.9774 | 0.9953 |
| CNN Binary | 0.9558 | 0.9489 | 0.9957 | 0.9717 | 0.9235 |

### Multi-class Classification

| Model | Accuracy | Precision | Recall | F1-Score | AUC-ROC |
|-------|----------|-----------|--------|----------|----------|
| MLP Multi | 0.7795 | 0.8102 | 0.7795 | 0.7742 | 0.9808 |
| CNN Multi | 0.5747 | 0.6455 | 0.5747 | 0.4864 | 0.8982 |

## Training Time

- **MLP Binary**: Total=84.55s, Avg/Round=4.19s
- **CNN Binary**: Total=206.44s, Avg/Round=10.24s
- **MLP Multi**: Total=127.83s, Avg/Round=6.34s
- **CNN Multi**: Total=417.54s, Avg/Round=20.77s

## Visualizations

![Results](plots/comprehensive_results.png)

## Files Generated

- `results_summary.json` - Metrics in JSON format
- `models/` - Saved trained models
- `plots/` - Visualization plots
