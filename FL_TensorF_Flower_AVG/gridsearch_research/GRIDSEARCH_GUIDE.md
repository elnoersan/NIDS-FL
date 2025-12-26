# 🔬 Grid Search Quick Start - COMPREHENSIVE GUIDE

## 📋 Overview

This infrastructure runs **20 automated hyperparameter experiments** for federated learning:

**Grid Parameters:**
- Batch Size: 32, 64, 128, 256, 512 (5 values)
- Local Epochs: 1, 2 (2 values)
- Learning Rate: 0.001, 0.0005 (2 values)
- **Total: 5 × 2 × 2 = 20 experiments**

**What Gets Trained:**
Each experiment trains 4 models:
1. MLP Binary Classification
2. CNN Binary Classification  
3. MLP Multi-class Classification
4. CNN Multi-class Classification

**Total Models Trained: 20 × 4 = 80 models!**

---

## 🚀 HOW TO START (Super Simple!)

### Step 1: Navigate to folder
```bash
cd "/home/elnoersan/Skripsi/Paper/NotebookTODO/Testing Notebook/FednonIID/Avg/FL_TensorF_Flower_AVG"
```

### Step 2: Activate environment
```bash
source /home/elnoersan/Skripsi/Paper/.venv/bin/activate.fish
```

### Step 3: Run it!
```bash
./start_gridsearch.sh
```

**That's it!** ✅ The system runs everything automatically.

---

## ⏱️ Time Expectations

| Item | Duration |
|------|----------|
| Single experiment | 15-30 min |
| All 20 experiments | 5-10 hours |
| Overnight run | ✅ Recommended |

---

## 📊 Monitoring (While It Runs)

Open a **new terminal** and use these commands:

### Check Overall Progress
```bash
python check_progress.py
```
Shows:
- How many experiments completed (X/20)
- Current running experiment
- Estimated time remaining
- Best results so far

### Watch Live Output
```bash
tail -f gridsearch_research/bs256_epoch1_lr0p0010/experiment_log.txt
```
Replace `bs256_epoch1_lr0p0010` with current experiment name.

### Quick Status Check
```bash
cat gridsearch_research/all_experiments.json
```

---

## 📁 What Gets Created

```
gridsearch_research/
│
├── all_experiments.json          ← Tracks all 20 experiments
├── summary_report.md             ← FINAL REPORT (read this!)
│
├── bs32_epoch1_lr0p0010/        ← Experiment 1 folder
│   ├── experiment_log.txt       
│   ├── results_summary.json     
│   ├── experiment_report.md     
│   ├── plots/comprehensive_results.png
│   └── models/
│       ├── mlp_binary.keras
│       ├── cnn_binary.keras
│       ├── mlp_multi.keras
│       └── cnn_multi.keras
│
├── bs32_epoch1_lr0p0005/        ← Experiment 2 folder
├── bs32_epoch2_lr0p0010/        ← Experiment 3 folder
├── bs32_epoch2_lr0p0005/        
├── bs64_epoch1_lr0p0010/        
├── ... (continues for all 20)
```

**Every experiment folder contains:**
- ✅ Log file (complete output)
- ✅ JSON results (all metrics)
- ✅ Markdown report (formatted nicely)
- ✅ Plots (visualizations)
- ✅ Trained models (ready to use)

---

## 📊 Understanding Experiment Names

Format: `bs{BATCH}_epoch{EPOCHS}_lr{LR}`

Examples:
- `bs256_epoch1_lr0p0010` = Batch 256, 1 Epoch, LR 0.001
- `bs128_epoch2_lr0p0005` = Batch 128, 2 Epochs, LR 0.0005

**All 20 Experiments:**

| # | Name | Batch | Epochs | LR |
|---|------|-------|--------|-----|
| 1 | bs32_epoch1_lr0p0010 | 32 | 1 | 0.001 |
| 2 | bs32_epoch1_lr0p0005 | 32 | 1 | 0.0005 |
| 3 | bs32_epoch2_lr0p0010 | 32 | 2 | 0.001 |
| 4 | bs32_epoch2_lr0p0005 | 32 | 2 | 0.0005 |
| 5 | bs64_epoch1_lr0p0010 | 64 | 1 | 0.001 |
| 6 | bs64_epoch1_lr0p0005 | 64 | 1 | 0.0005 |
| 7 | bs64_epoch2_lr0p0010 | 64 | 2 | 0.001 |
| 8 | bs64_epoch2_lr0p0005 | 64 | 2 | 0.0005 |
| 9 | bs128_epoch1_lr0p0010 | 128 | 1 | 0.001 |
| 10 | bs128_epoch1_lr0p0005 | 128 | 1 | 0.0005 |
| 11 | bs128_epoch2_lr0p0010 | 128 | 2 | 0.001 |
| 12 | bs128_epoch2_lr0p0005 | 128 | 2 | 0.0005 |
| 13 | bs256_epoch1_lr0p0010 | 256 | 1 | 0.001 |
| 14 | bs256_epoch1_lr0p0005 | 256 | 1 | 0.0005 |
| 15 | bs256_epoch2_lr0p0010 | 256 | 2 | 0.001 |
| 16 | bs256_epoch2_lr0p0005 | 256 | 2 | 0.0005 |
| 17 | bs512_epoch1_lr0p0010 | 512 | 1 | 0.001 |
| 18 | bs512_epoch1_lr0p0005 | 512 | 1 | 0.0005 |
| 19 | bs512_epoch2_lr0p0010 | 512 | 2 | 0.001 |
| 20 | bs512_epoch2_lr0p0005 | 512 | 2 | 0.0005 |

---

## 🎯 After Completion - What to Do?

### 1. Read the Summary Report
```bash
cat gridsearch_research/summary_report.md
```
or
```bash
code gridsearch_research/summary_report.md  # Open in VS Code
```

**This report contains:**
- ✅ Best configuration for each model type
- ✅ Performance comparison tables
- ✅ Hyperparameter impact analysis
- ✅ Recommendations for your paper

### 2. Find the Best Model

The summary will tell you which experiment performed best. For example:

```
Best MLP Binary: bs128_epoch2_lr0p0010
  - F1-Score: 0.9876
  - Accuracy: 0.9854
```

### 3. Load and Use the Best Model

```python
from keras.models import load_model

# Load the best model
model = load_model('gridsearch_research/bs128_epoch2_lr0p0010/models/mlp_binary.keras')

# Use it for predictions
predictions = model.predict(your_test_data)
```

### 4. Extract Metrics for Your Paper

```python
import json

# Load results
with open('gridsearch_research/bs128_epoch2_lr0p0010/results_summary.json') as f:
    results = json.load(f)

# Get metrics
print(f"Accuracy: {results['binary']['MLP Binary']['accuracy']:.4f}")
print(f"F1-Score: {results['binary']['MLP Binary']['f1_score']:.4f}")
print(f"Precision: {results['binary']['MLP Binary']['precision']:.4f}")
print(f"Recall: {results['binary']['MLP Binary']['recall']:.4f}")
```

---

## 🔧 Useful Commands

```bash
# Start grid search
./start_gridsearch.sh

# Check progress any time
python check_progress.py

# View specific experiment log
cat gridsearch_research/bs256_epoch1_lr0p0010/experiment_log.txt

# Watch experiment running live
tail -f gridsearch_research/bs256_epoch1_lr0p0010/experiment_log.txt

# See all experiment statuses
cat gridsearch_research/all_experiments.json | grep status

# Read final summary
cat gridsearch_research/summary_report.md
```

---

## 🛠️ Troubleshooting

### ❌ "Virtual environment not found"
```bash
source /home/elnoersan/Skripsi/Paper/.venv/bin/activate.fish
```

### ❌ "Permission denied"
```bash
chmod +x start_gridsearch.sh run_gridsearch.py check_progress.py
```

### ❌ "Out of memory"
**Solution:** Edit `run_gridsearch.py` and reduce batch sizes:
```python
BATCH_SIZES = [32, 64, 128]  # Remove 256 and 512
```

### ❌ "Experiment failed"
1. Check error in log:
   ```bash
   tail -50 gridsearch_research/bs256_epoch1_lr0p0010/experiment_log.txt
   ```

2. Re-run specific experiment:
   ```bash
   export GRIDSEARCH_BATCH_SIZE=256
   export GRIDSEARCH_LOCAL_EPOCHS=1
   export GRIDSEARCH_LEARNING_RATE=0.001
   export GRIDSEARCH_OUTPUT_DIR="gridsearch_research/bs256_epoch1_lr0p0010"
   export GRIDSEARCH_EXP_NAME="bs256_epoch1_lr0p0010"
   python research_hypertuning_gridsearch.py
   ```

### ❌ "Too slow"
**This is normal!** Each experiment takes 15-30 minutes.
- ✅ Run overnight
- ✅ Close other applications
- ✅ Be patient - you're training 80 models!

---

## 💡 Pro Tips

1. **Run overnight** - Start before bed, check results in the morning
2. **Monitor in separate terminal** - Use `python check_progress.py` 
3. **Don't stop it** - Each experiment is independent, stopping loses progress
4. **Backup results** - Copy `gridsearch_research/` folder when done
5. **Read summary first** - `summary_report.md` has all the insights

---

## 📝 For Your Research Paper

After grid search completes, you'll have:

✅ **Performance tables** - Copy from summary_report.md  
✅ **Best hyperparameters** - Identified automatically  
✅ **Training curves** - In plots/ folders  
✅ **Comparison charts** - Ready to include  
✅ **Trained models** - For deployment  

**Perfect for methodology and results sections!**

---

## 🎓 What Makes This Special?

- ✅ Fully automated (no manual intervention)
- ✅ Comprehensive (20 experiments, 80 models)
- ✅ Well documented (logs, reports, plots)
- ✅ Production ready (saved models)
- ✅ Research ready (metrics, tables, charts)
- ✅ Reproducible (all configs saved)

---

## 📞 Quick Reference Card

| Task | Command |
|------|---------|
| Start grid search | `./start_gridsearch.sh` |
| Check progress | `python check_progress.py` |
| Watch live | `tail -f gridsearch_research/<exp>/experiment_log.txt` |
| View summary | `cat gridsearch_research/summary_report.md` |
| Load model | `load_model('gridsearch_research/<exp>/models/model.keras')` |

---

**Ready? Just run:**
```bash
./start_gridsearch.sh
```

**Then go have coffee, dinner, or sleep. The system handles everything!** ☕🍕😴

---

*Last updated: December 9, 2025*
