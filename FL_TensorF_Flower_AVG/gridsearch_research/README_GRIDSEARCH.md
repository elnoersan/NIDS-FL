# Hyperparameter Grid Search for Federated Learning

This directory contains a comprehensive grid search infrastructure for federated learning experiments using Flower (FedAvg).

## Overview

The grid search explores 20 combinations of hyperparameters:

- **Batch Size**: [32, 64, 128, 256, 512]
- **Local Epochs**: [1, 2]
- **Learning Rate**: [0.001, 0.0005]

**Total Combinations**: 5 × 2 × 2 = **20 experiments**

Each experiment trains 4 models:
1. MLP Binary Classification
2. CNN Binary Classification
3. MLP Multi-class Classification
4. CNN Multi-class Classification

## Quick Start

### 1. Activate Virtual Environment

```bash
source /home/elnoersan/Skripsi/Paper/.venv/bin/activate.fish
```

### 2. Run Grid Search

```bash
cd "/home/elnoersan/Skripsi/Paper/NotebookTODO/Testing Notebook/FednonIID/Avg/FL_TensorF_Flower_AVG"
python run_gridsearch.py
```

### 3. Monitor Progress

The script will:
- Display progress for each experiment
- Show estimated time remaining
- Log all outputs to individual experiment folders
- Generate a comprehensive summary report at the end

## Directory Structure

After running the grid search, the structure will be:

```
gridsearch_research/
├── all_experiments.json              # Complete experiment tracking
├── summary_report.md                 # Final comprehensive report
├── bs32_epoch1_lr0p0010/            # Example experiment folder
│   ├── experiment_log.txt           # Detailed execution log
│   ├── results_summary.json         # Metrics in JSON format
│   ├── experiment_report.md         # Individual experiment report
│   ├── plots/
│   │   └── comprehensive_results.png
│   └── models/
│       ├── mlp_binary.keras
│       ├── cnn_binary.keras
│       ├── mlp_multi.keras
│       └── cnn_multi.keras
├── bs32_epoch1_lr0p0005/
│   └── ...
├── bs32_epoch2_lr0p0010/
│   └── ...
└── ... (17 more experiment folders)
```

## Files Description

### Main Scripts

- **`run_gridsearch.py`**: Orchestrates all 20 experiments
  - Generates experiment combinations
  - Manages execution order
  - Tracks progress and timing
  - Generates final summary report

- **`research_hypertuning_gridsearch.py`**: Individual experiment runner
  - Accepts hyperparameters via environment variables
  - Trains all 4 models
  - Evaluates and saves results
  - Generates plots and reports

### Output Files (per experiment)

- **`experiment_log.txt`**: Complete console output and logs
- **`results_summary.json`**: Structured metrics data
- **`experiment_report.md`**: Markdown report with results and visualizations
- **`plots/comprehensive_results.png`**: Training curves and performance metrics
- **`models/*.keras`**: Trained model weights

### Global Files

- **`all_experiments.json`**: Tracking file for all 20 experiments
- **`summary_report.md`**: Comprehensive analysis across all experiments

## Expected Runtime

- **Per Experiment**: ~15-30 minutes (depends on hardware)
- **Total Grid Search**: ~5-10 hours (20 experiments)

The orchestrator will show:
- Current experiment progress
- Time per experiment
- Total elapsed time
- Estimated time remaining

## Results Analysis

The final `summary_report.md` will include:

1. **Executive Summary**
   - Completion statistics
   - Total time spent
   - Success/failure counts

2. **Performance Comparison Tables**
   - Binary classification results
   - Multi-class classification results
   - Sorted by F1-score

3. **Best Configurations**
   - Best hyperparameters for each model type
   - Best overall configuration

4. **Hyperparameter Impact Analysis**
   - Effect of batch size
   - Effect of local epochs
   - Effect of learning rate

5. **Recommendations**
   - Optimal configurations for production
   - Trade-offs between performance and training time

## Customization

### Modify Grid Search Parameters

Edit `run_gridsearch.py`:

```python
BATCH_SIZES = [32, 64, 128, 256, 512]    # Add/remove batch sizes
LOCAL_EPOCHS = [1, 2]                     # Add/remove epoch counts
LEARNING_RATES = [0.001, 0.0005]         # Add/remove learning rates
```

### Modify Experiment Configuration

Edit `research_hypertuning_gridsearch.py`:

```python
NUM_ROUNDS = 20        # Federated learning rounds
NUM_CLIENTS = 5        # Number of clients
ALPHA_BINARY = 0.3     # Dirichlet alpha for binary
ALPHA_MULTI = 0.3      # Dirichlet alpha for multi-class
```

## Monitoring Individual Experiments

While the grid search is running, you can monitor individual experiments:

```bash
# Watch live output
tail -f gridsearch_research/bs256_epoch1_lr0p0010/experiment_log.txt

# Check results so far
cat gridsearch_research/all_experiments.json

# View an individual report
cat gridsearch_research/bs256_epoch1_lr0p0010/experiment_report.md
```

## Resuming Failed Experiments

If an experiment fails, the tracker will log it. You can:

1. Check `all_experiments.json` for failed experiments
2. Manually re-run specific configurations by setting environment variables:

```bash
export GRIDSEARCH_BATCH_SIZE=256
export GRIDSEARCH_LOCAL_EPOCHS=1
export GRIDSEARCH_LEARNING_RATE=0.001
export GRIDSEARCH_OUTPUT_DIR="gridsearch_research/bs256_epoch1_lr0p0010"
export GRIDSEARCH_EXP_NAME="bs256_epoch1_lr0p0010"

python research_hypertuning_gridsearch.py
```

## Post-Processing

After completion, you can:

1. **Compare Results**: Review `summary_report.md`
2. **Visualize Trends**: Plot hyperparameter effects
3. **Select Best Model**: Load the best model for deployment:

```python
from keras.models import load_model

# Load best model (example)
best_model = load_model('gridsearch_research/bs128_epoch2_lr0p0010/models/cnn_binary.keras')
```

## Troubleshooting

### Out of Memory
- Reduce batch sizes
- Reduce number of clients
- Close other applications

### Slow Execution
- Reduce NUM_ROUNDS
- Use fewer model types
- Run on GPU if available

### Python Environment Issues
```bash
# Reinstall dependencies
pip install --upgrade tensorflow keras flwr scikit-learn pandas numpy matplotlib seaborn tabulate
```

## Citation

If you use this grid search infrastructure, please cite your paper and reference:

```
Federated Learning with FedAvg on TON_IoT Dataset
Framework: Flower (flwr)
Algorithm: Federated Averaging
Distribution: Non-IID (Dirichlet)
```

## Contact

For questions or issues, refer to the main project documentation.

---

**Last Updated**: December 9, 2025
