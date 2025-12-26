# FedProx Grid Search - Quick Reference

## 🚀 Quick Start

```bash
cd gridsearch_research
./start_gridsearch.sh
```

## 📊 What Gets Tested

- **Batch Sizes:** [256, 512]
- **Local Epochs:** [1, 2]
- **Learning Rates:** [0.001, 0.0005]
- **Mu (Proximal Term):** [0.001, 0.01, 0.1] ⭐

**Total:** 24 experiments × 4 models = 96 models  
**Duration:** 8-12 hours

## 🔍 Monitor Progress

```bash
python3 check_progress.py
```

## 📁 Results Location

```
gridsearch_research/grid_search_results/
├── all_experiments.json      # Tracking data
├── summary_report.md          # Final comprehensive report
└── bs{}_ep{}_lr{}_mu{}/      # Individual experiments
```

## 🎯 Key Features

✅ **FedProx-Specific:** Tests different mu (proximal term) values  
✅ **Auto-Resume:** Skips completed experiments  
✅ **Progress Tracking:** Real-time monitoring  
✅ **Comprehensive Reports:** Detailed analysis with mu parameter insights  
✅ **Ray Worker Fix:** PYTHONPATH configured to prevent import errors

## 📖 Full Documentation

See **GRIDSEARCH_GUIDE.md** for:
- Understanding FedProx vs FedAvg
- Mu parameter explanation
- Troubleshooting guide
- Advanced usage
- Results interpretation

## 🔬 What is Mu?

**Mu (μ)** is the proximal term coefficient in FedProx:

```
Local Loss = Original Loss + (μ/2) × ||w - w_global||²
```

- **Low mu (0.001):** Close to FedAvg behavior
- **Medium mu (0.01):** Recommended for Non-IID data
- **High mu (0.1):** Strong regularization for extreme heterogeneity

This grid search finds the optimal mu for your TON_IoT dataset!

## ⚙️ Customization

Edit `run_gridsearch.py` to change parameter grid:

```python
BATCH_SIZES = [256, 512]
LOCAL_EPOCHS = [1, 2]
LEARNING_RATES = [0.001, 0.0005]
MU_VALUES = [0.001, 0.01, 0.1]  # Adjust this!
```

## 🆘 Troubleshooting

**Import errors?** → Already fixed via PYTHONPATH  
**Out of memory?** → Reduce batch sizes or NUM_CLIENTS  
**Too slow?** → Reduce NUM_ROUNDS in research_hypertuning_gridsearch.py  

See GRIDSEARCH_GUIDE.md for detailed solutions.

---

**Created:** December 2025  
**Algorithm:** FedProx (Federated Proximal)  
**Framework:** Flower (flwr)
