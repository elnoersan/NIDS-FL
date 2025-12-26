# Experiment Report: bs512_epoch2_lr0p0005_alpha5p0

**Date**: 2025-12-10 10:22:16

## Hyperparameters

- **Batch Size**: 512
- **Local Epochs**: 2
- **Learning Rate**: 0.0005
- **Alpha (Dirichlet)**: 5.0
- **Number of Rounds**: 20
- **Number of Clients**: 5

## Results Summary

### Binary Classification

| Model | Accuracy | Precision | Recall | F1-Score | AUC-ROC |
|-------|----------|-----------|--------|----------|----------|
| MLP Binary | 0.9570 | 0.9490 | 0.9973 | 0.9725 | 0.9961 |
| CNN Binary | 0.9660 | 0.9921 | 0.9631 | 0.9774 | 0.9964 |

### Multi-class Classification

| Model | Accuracy | Precision | Recall | F1-Score | AUC-ROC |
|-------|----------|-----------|--------|----------|----------|
| MLP Multi | 0.7827 | 0.8096 | 0.7827 | 0.7770 | 0.9800 |
| CNN Multi | 0.7713 | 0.8213 | 0.7713 | 0.7502 | 0.9769 |

## Training Time

- **MLP Binary**: Total=72.30s, Avg/Round=3.58s
- **CNN Binary**: Total=206.19s, Avg/Round=10.25s
- **MLP Multi**: Total=108.94s, Avg/Round=5.40s
- **CNN Multi**: Total=475.98s, Avg/Round=23.65s

## Visualizations

![Results](plots/comprehensive_results.png)

## Files Generated

- `results_summary.json` - Metrics in JSON format
- `models/` - Saved trained models
- `plots/` - Visualization plots
