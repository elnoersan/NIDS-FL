BINARY CLASSIFICATION - Top 5 Pairwise Comparisons:
--------------------------------------------------------------------------------

Configuration: BS=256, Epochs=2, LR=0.0005, Model=CNN Binary
  Accuracy:  α=0.3: 0.9574 | α=5.0: 0.9558 | Diff: -0.0017
  F1-Score:  α=0.3: 0.9728 | α=5.0: 0.9717 | Diff: -0.0011
  AUC-ROC:   α=0.3: 0.9975 | α=5.0: 0.9235 | Diff: -0.0740
  Winner: Alpha 0.3 (Non-IID)

Configuration: BS=1024, Epochs=2, LR=0.0005, Model=CNN Binary
  Accuracy:  α=0.3: 0.9580 | α=5.0: 0.9674 | Diff: +0.0094
  F1-Score:  α=0.3: 0.9731 | α=5.0: 0.9784 | Diff: +0.0052
  AUC-ROC:   α=0.3: 0.9974 | α=5.0: 0.9968 | Diff: -0.0006
  Winner: Alpha 0.3 (Non-IID)

MULTI-CLASS CLASSIFICATION - Top 5 Pairwise Comparisons:
--------------------------------------------------------------------------------

Configuration: BS=512, Epochs=2, LR=0.0005, Model=CNN Multi
  Accuracy:  α=0.3: 0.7146 | α=5.0: 0.7713 | Diff: +0.0567
  F1-Score:  α=0.3: 0.6668 | α=5.0: 0.7502 | Diff: +0.0834
  AUC-ROC:   α=0.3: 0.9840 | α=5.0: 0.9769 | Diff: -0.0070
  Winner: Alpha 0.3 (Non-IID)

Configuration: BS=1024, Epochs=2, LR=0.001, Model=CNN Multi
  Accuracy:  α=0.3: 0.7511 | α=5.0: 0.8005 | Diff: +0.0494
  F1-Score:  α=0.3: 0.7296 | α=5.0: 0.7946 | Diff: +0.0650
  AUC-ROC:   α=0.3: 0.9837 | α=5.0: 0.9825 | Diff: -0.0012
  Winner: Alpha 0.3 (Non-IID)

RERUN TO RESEARCH_NOTEBOOK.IPYNB
--------------------------------------------------------------------------------
BS=256, Epochs=2, LR=0.0005, Alpha= 0.3 && 5
BS=512, Epochs=2, LR=0.0005, Alpha= 0.3 && 5
BS=1024, Epochs=2, LR=0.0005, Alpha= 0.3 && 5
BS=1023, Epochs=2, LR=0.001, Alpha= 0.3 && 5