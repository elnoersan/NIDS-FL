# FEDPROX HYPERPARAMETER GRID SEARCH - COMPREHENSIVE GUIDE

**Last Updated:** December 2025  
**Algorithm:** FedProx (Federated Proximal)  
**Framework:** Flower (flwr) with Ray backend

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [What is FedProx?](#what-is-fedprox)
3. [Grid Search Configuration](#grid-search-configuration)
4. [Quick Start](#quick-start)
5. [Understanding the Mu Parameter](#understanding-the-mu-parameter)
6. [Monitoring Progress](#monitoring-progress)
7. [Understanding Results](#understanding-results)
8. [Troubleshooting](#troubleshooting)
9. [File Structure](#file-structure)
10. [Advanced Usage](#advanced-usage)

---

## 🎯 Overview

This grid search infrastructure automatically tests **24 different hyperparameter combinations** for FedProx federated learning experiments on the TON_IoT dataset.

**Key Statistics:**
- **Total Experiments:** 24
- **Models per Experiment:** 4 (MLP Binary, CNN Binary, MLP Multi, CNN Multi)
- **Total Models Trained:** 96
- **Expected Runtime:** 8-12 hours
- **Dataset:** TON_IoT Network Traffic (preprocessed)
- **Data Distribution:** Non-IID (Dirichlet)

---

## 🔬 What is FedProx?

**FedProx (Federated Proximal)** is an extension of Federated Averaging (FedAvg) designed to handle **heterogeneous** (Non-IID) data and systems more effectively.

### Key Difference from FedAvg

FedProx adds a **proximal term** to the local training objective:

```
Local Loss = Original Loss + (μ/2) × ||w - w_global||²
```

Where:
- `w` = local model weights
- `w_global` = global model weights received from server
- `μ` (mu) = proximal term coefficient

### Why FedProx?

✅ **Better convergence** on Non-IID (heterogeneous) data  
✅ **Handles system heterogeneity** (clients with different computational capabilities)  
✅ **Prevents local models from drifting too far** from global model  
✅ **More robust** to data imbalance and statistical heterogeneity

### When to Use FedProx vs FedAvg?

| Scenario | Recommended Algorithm |
|----------|----------------------|
| Data is IID (identical distribution across clients) | FedAvg |
| Data is Non-IID (heterogeneous distribution) | **FedProx** |
| Large system heterogeneity | **FedProx** |
| Convergence stability issues | **FedProx** |
| Need faster convergence | FedAvg (sometimes) |

**For this project:** We use **Non-IID data** (Dirichlet distribution), so FedProx is ideal.

---

## ⚙️ Grid Search Configuration

### Hyperparameters Being Tested

```python
BATCH_SIZES = [256, 512]
LOCAL_EPOCHS = [1, 2]
LEARNING_RATES = [0.001, 0.0005]
MU_VALUES = [0.001, 0.01, 0.1]  # FedProx-specific!
```

**Total Combinations:** 2 × 2 × 2 × 3 = **24 experiments**

### Fixed Parameters

```python
NUM_ROUNDS = 20        # Federated learning rounds
NUM_CLIENTS = 5        # Number of clients
ALPHA_BINARY = 0.3     # Dirichlet alpha for binary (Non-IID level)
ALPHA_MULTI = 0.3      # Dirichlet alpha for multi-class
```

### Models Trained per Experiment

1. **MLP Binary** - Multi-Layer Perceptron for binary classification (Normal/Attack)
2. **CNN Binary** - Convolutional Neural Network for binary classification
3. **MLP Multi** - Multi-Layer Perceptron for multi-class (attack type)
4. **CNN Multi** - Convolutional Neural Network for multi-class

---

## 🚀 Quick Start

### Prerequisites

1. **Python Virtual Environment** activated
2. **Required packages** installed:
   ```bash
   pip install tensorflow flwr pandas numpy scikit-learn matplotlib seaborn
   ```
3. **Dataset** available at:
   ```
   /home/elnoersan/Skripsi/Paper/NotebookTODO/train_test_network.csv
   ```

### Running the Grid Search

**Method 1: Using the wrapper script (Recommended)**

```bash
cd gridsearch_research
chmod +x start_gridsearch.sh
./start_gridsearch.sh
```

**Method 2: Direct Python execution**

```bash
cd gridsearch_research
python3 run_gridsearch.py
```

### What Happens Next?

1. ✅ Script validates configuration
2. 📊 Shows experiment summary
3. ⏸️ Asks for confirmation (Press ENTER to continue)
4. 🔄 Runs 24 experiments sequentially
5. 💾 Saves results after each experiment
6. 📈 Generates comprehensive report at the end

---

## 📊 Understanding the Mu Parameter

**Mu (μ)** is the **most important parameter** in FedProx. It controls the strength of the proximal term.

### Mu Value Meanings

| Mu Value | Meaning | When to Use |
|----------|---------|-------------|
| **0.001** | Very weak regularization | Close to FedAvg behavior, for mild heterogeneity |
| **0.01** | Moderate regularization | **Recommended starting point** for Non-IID data |
| **0.1** | Strong regularization | For extreme heterogeneity or divergence issues |
| **1.0** | Very strong regularization | Rarely needed, can slow convergence |

### How Mu Affects Training

**Low Mu (0.001):**
- ➕ Allows more local learning
- ➕ Potentially faster convergence
- ➖ May diverge on very Non-IID data
- ➖ Less stable on imbalanced data

**High Mu (0.1):**
- ➕ More stable convergence
- ➕ Better handling of extreme Non-IID
- ➖ Slower local adaptation
- ➖ May underfit on easy data

**Medium Mu (0.01) - Recommended:**
- ✅ Balanced approach
- ✅ Good for most Non-IID scenarios
- ✅ Stable yet adaptive

### Grid Search Insight

This grid search tests **3 mu values** to find the optimal balance for your specific data distribution. Results will show which mu works best for binary vs multi-class classification.

---

## 📈 Monitoring Progress

### Real-Time Monitoring

While experiments are running, check progress anytime:

```bash
python3 check_progress.py
```

**Output includes:**
- ✅ Overall statistics (completed/failed/pending)
- 🔄 Currently running experiments
- ⏱️ Estimated time remaining
- 🏆 Best results so far
- 📊 Mu parameter analysis

### Progress Files

**Location:** `gridsearch_research/grid_search_results/`

**Files:**
- `all_experiments.json` - Detailed tracking data (auto-updated)
- `summary_report.md` - Final comprehensive report (generated at end)
- Individual experiment folders: `bs{size}_ep{epochs}_lr{rate}_mu{mu}/`

### Example Output Structure

```
grid_search_results/
├── all_experiments.json
├── summary_report.md
├── bs256_ep1_lr0p0010_mu0p0010/
│   ├── results.json
│   ├── summary.txt
│   └── experiment_log.txt
├── bs256_ep1_lr0p0010_mu0p0100/
│   ├── results.json
│   ├── summary.txt
│   └── experiment_log.txt
└── ... (22 more experiment folders)
```

---

## 📊 Understanding Results

### Results Files

Each experiment creates:

1. **results.json** - Machine-readable metrics
   ```json
   {
     "mlp_binary": {
       "accuracy": 0.9876,
       "f1_score": 0.9823,
       "precision": 0.9890,
       "recall": 0.9756,
       "auc_roc": 0.9945
     },
     ...
   }
   ```

2. **summary.txt** - Human-readable summary
   ```
   FEDPROX EXPERIMENT SUMMARY
   ==========================
   
   Hyperparameters:
     - Batch Size: 512
     - Local Epochs: 1
     - Learning Rate: 0.001
     - Mu (Proximal Term): 0.01
   
   Results:
   MLP_BINARY:
     - Accuracy: 0.9876
     - F1-Score: 0.9823
     ...
   ```

3. **experiment_log.txt** - Complete execution log (for debugging)

### Summary Report

After all experiments complete, `summary_report.md` contains:

#### 1. Experiment Statistics
- Total/completed/failed counts
- Average duration
- Success rate

#### 2. Hyperparameter Grid
- All tested combinations
- Parameter ranges

#### 3. Best Performing Configurations
- **Per model type** (MLP Binary, CNN Binary, MLP Multi, CNN Multi)
- Best hyperparameters for each
- Full metrics (F1, Accuracy, Precision, Recall, AUC-ROC)

#### 4. Mu (Proximal Term) Analysis ⭐
- **Impact of mu on performance**
- Average metrics per mu value
- Recommendations for optimal mu

#### 5. Batch Size Analysis
- Performance across batch sizes
- Optimal batch size identification

#### 6. Learning Rate Analysis
- Performance across learning rates
- Optimal LR identification

#### 7. Failed Experiments
- List of failed configurations (if any)
- Helps identify problematic combinations

#### 8. Recommendations
- **Best overall configuration**
- Separate recommendations for binary vs multi-class
- Actionable insights

---

## 🔧 Troubleshooting

### Common Issues

#### 1. Import Errors (ModuleNotFoundError)

**Error:** `ModuleNotFoundError: No module named 'task'`

**Solution:** Already handled! The script includes:
```python
sys.path.insert(0, str(Path(__file__).parent.parent))
```

And sets `PYTHONPATH` for Ray workers:
```python
env['PYTHONPATH'] = str(Path(__file__).parent.parent)
```

#### 2. Out of Memory (OOM)

**Symptoms:**
- Training crashes mid-experiment
- System freezes
- GPU out of memory errors

**Solutions:**
1. Reduce `BATCH_SIZE` in the grid (use only `[256]`)
2. Reduce `NUM_CLIENTS` in script (try 3 instead of 5)
3. Close other GPU-intensive applications
4. Add GPU memory limiting:
   ```python
   gpus = tf.config.list_physical_devices('GPU')
   tf.config.set_logical_device_configuration(
       gpus[0],
       [tf.config.LogicalDeviceConfiguration(memory_limit=4096)]
   )
   ```

#### 3. Experiments Too Slow

**Symptoms:**
- Each experiment takes > 1 hour
- Grid search projected to take > 24 hours

**Solutions:**
1. Reduce `NUM_ROUNDS` from 20 to 10 in `research_hypertuning_gridsearch.py`
2. Reduce parameter grid:
   ```python
   BATCH_SIZES = [512]  # Test only one
   MU_VALUES = [0.01, 0.1]  # Reduce from 3 to 2
   ```
3. Enable GPU if not already:
   ```bash
   nvidia-smi  # Check GPU availability
   ```

#### 4. Ray Worker Crashes

**Error:** `RaySystemError` or Ray workers fail to start

**Solutions:**
1. Ensure PYTHONPATH is set (already done in script)
2. Check Ray installation:
   ```bash
   pip install --upgrade ray
   ```
3. Reduce Ray resources in Flower simulation:
   ```python
   # In research_hypertuning_gridsearch.py
   ray_init_args = {"num_cpus": 4, "num_gpus": 0.5}
   ```

#### 5. Experiments Marked as "Running" Forever

**Symptom:** `check_progress.py` shows experiments stuck in "running" state

**Solution:**
```bash
# Reset stuck experiments
python3 -c "
import json
with open('grid_search_results/all_experiments.json', 'r') as f:
    data = json.load(f)
for exp in data['experiments']:
    if exp['status'] == 'running':
        exp['status'] = 'pending'
        data['metadata']['in_progress'] -= 1
with open('grid_search_results/all_experiments.json', 'w') as f:
    json.dump(data, f, indent=2)
"
```

Then restart:
```bash
./start_gridsearch.sh
```

---

## 📁 File Structure

```
gridsearch_research/
│
├── run_gridsearch.py              # Main orchestrator
├── research_hypertuning_gridsearch.py  # Individual experiment runner
├── check_progress.py              # Progress monitoring tool
├── start_gridsearch.sh            # Wrapper script (Fish shell)
├── GRIDSEARCH_GUIDE.md            # This file
│
└── grid_search_results/           # Created when you run experiments
    ├── all_experiments.json       # Tracking data
    ├── summary_report.md          # Final report
    └── bs{}_ep{}_lr{}_mu{}/      # Individual experiment folders
        ├── results.json
        ├── summary.txt
        └── experiment_log.txt
```

### Parent Directory Files (Required)

```
FL_TensorF_Flower_PROX/
├── task.py                        # Model definitions + ProximalModel class
├── utils.py                       # Data splitting, evaluation functions
├── research_hypertuning.py        # Original hardcoded script (reference)
└── gridsearch_research/           # Grid search folder
```

**Important:** `task.py` must contain `ProximalModel` class for FedProx to work!

---

## 🚀 Advanced Usage

### Customizing the Grid

Edit `run_gridsearch.py` at the top:

```python
# ============================================================================
# KONFIGURASI GRID SEARCH - UBAH DI SINI
# ============================================================================
BATCH_SIZES = [256, 512]           # Add more: [128, 256, 512, 1024]
LOCAL_EPOCHS = [1, 2]              # Add more: [1, 2, 3, 5]
LEARNING_RATES = [0.001, 0.0005]   # Add more: [0.01, 0.001, 0.0001]
MU_VALUES = [0.001, 0.01, 0.1]     # Add more: [0.0001, 0.001, 0.01, 0.1, 1.0]

# Advanced: Test different mu for binary vs multi-class
# Requires modifying the experiment runner to accept separate mu values
```

### Running Subset of Experiments

**Scenario:** You want to test only specific mu values

1. Modify `MU_VALUES` in `run_gridsearch.py`:
   ```python
   MU_VALUES = [0.01]  # Test only one mu
   ```

2. Run grid search as normal

### Resuming Failed Experiments

Grid search automatically **skips completed experiments** and **resumes failed ones**.

To retry only failed experiments:
```bash
# Mark failed as pending
python3 -c "
import json
with open('grid_search_results/all_experiments.json', 'r') as f:
    data = json.load(f)
for exp in data['experiments']:
    if exp['status'] == 'failed':
        exp['status'] = 'pending'
        data['metadata']['failed'] -= 1
with open('grid_search_results/all_experiments.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# Restart
./start_gridsearch.sh
```

### Parallel Execution (Experimental)

**Warning:** Resource-intensive!

Modify `run_gridsearch.py` to use multiprocessing:
```python
from multiprocessing import Pool

# In main():
with Pool(processes=2) as pool:  # Run 2 experiments at once
    pool.starmap(run_experiment, experiments_to_run)
```

**Risks:**
- High GPU memory usage (may crash)
- Ray resource conflicts
- Harder to monitor

**Recommendation:** Sequential execution is safer.

---

## 📚 Understanding FedProx vs FedAvg

### Algorithmic Comparison

| Aspect | FedAvg | FedProx |
|--------|--------|---------|
| **Local Objective** | `min L(w)` | `min L(w) + (μ/2)||w - w_global||²` |
| **Convergence** | Good on IID | **Better on Non-IID** |
| **System Heterogeneity** | Assumes homogeneity | **Handles heterogeneity** |
| **Hyperparameters** | LR, batch size, epochs | LR, batch size, epochs, **μ** |
| **Use Case** | IID data, homogeneous systems | **Non-IID data, heterogeneous systems** |

### Implementation Difference

**FedAvg Client:**
```python
def fit(self, parameters, config):
    model.set_weights(parameters)
    model.fit(X_train, y_train)  # Standard training
    return model.get_weights()
```

**FedProx Client:**
```python
def fit(self, parameters, config):
    mu = config['proximal_mu']
    proximal_model = ProximalModel(base_model, parameters, mu)
    proximal_model.fit(X_train, y_train)  # Training with proximal term
    return base_model.get_weights()
```

**Key:** `ProximalModel` wraps the base model and adds `(μ/2)||w - w_global||²` to the loss.

---

## 🎓 Expected Outcomes

### What to Expect from Results

#### 1. Mu Impact
- **Lower mu** (0.001): May have higher variance in performance
- **Higher mu** (0.1): More stable but potentially lower peak performance
- **Optimal mu** (likely 0.01): Best balance for this dataset

#### 2. Binary vs Multi-class
- **Binary models** generally achieve higher accuracy (simpler task)
- **Multi-class models** benefit more from higher mu (more heterogeneity)

#### 3. MLP vs CNN
- **MLP** may perform better (tabular data)
- **CNN** can capture patterns if data has spatial structure

#### 4. Batch Size
- **Larger batch size** (512): Faster training, more stable
- **Smaller batch size** (256): Better generalization (sometimes)

### Research Insights

This grid search will help answer:
1. **What is the optimal mu for TON_IoT Non-IID data?**
2. **Does mu need to differ for binary vs multi-class tasks?**
3. **How does mu interact with learning rate and batch size?**
4. **Is FedProx significantly better than FedAvg for this dataset?**

---

## 📞 Support

### Getting Help

1. **Check this guide** - Most answers are here
2. **Check experiment logs** - `experiment_log.txt` in each folder
3. **Use progress monitor** - `python3 check_progress.py`
4. **Review original script** - `../research_hypertuning.py` for reference

### Reporting Issues

When reporting problems, include:
- Error message from log
- Configuration that failed
- System specs (GPU/CPU/RAM)
- Python/TensorFlow/Flower versions

---

## 🎯 Success Checklist

Before running grid search, ensure:

- ✅ Python virtual environment activated
- ✅ All required packages installed
- ✅ Dataset path is correct
- ✅ GPU is available (optional but recommended)
- ✅ At least 8-12 hours available for completion
- ✅ Sufficient disk space (~5GB for results)
- ✅ `task.py` contains `ProximalModel` class
- ✅ `utils.py` contains required functions

After completion:

- ✅ Check `summary_report.md` for comprehensive analysis
- ✅ Review best configurations per model type
- ✅ Analyze mu parameter impact
- ✅ Compare with FedAvg results (if available)
- ✅ Document findings for your research

---

## 📝 Citation

If you use this grid search infrastructure in your research, please cite:

```
FedProx Grid Search for TON_IoT Dataset
Federated Learning with Non-IID Data Distribution
December 2025
```

**Original FedProx Paper:**
```
Li, T., Sahu, A. K., Zaheer, M., Sanjabi, M., Talwalkar, A., & Smith, V. (2020).
Federated optimization in heterogeneous networks.
Proceedings of Machine Learning and Systems, 2, 429-450.
```

---

## 🏁 Final Notes

- **Be patient** - Grid search takes time, but results are worth it
- **Monitor resources** - Check GPU/CPU usage periodically
- **Save results** - `git commit` or backup the results folder
- **Document findings** - Add notes to help future you understand choices
- **Compare algorithms** - Run FedAvg grid search too for comparison

**Good luck with your research! 🚀**

---

*Last updated: December 2025*  
*For questions or improvements, contact the research team.*
