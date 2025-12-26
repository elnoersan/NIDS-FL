# 🚀 Quick Start Guide - FL_TensorF_Flower_PROX

Get started with Federated Proximal (FedProx) using Flower in just a few minutes!

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Basic understanding of federated learning
- ToN-IoT dataset (cleaned version)

## Step 1: Installation

### Option A: Install from requirements.txt (Recommended)

```bash
cd FL_TensorF_Flower_PROX
pip install -r requirements.txt
```

### Option B: Install packages manually

```bash
pip install flwr[simulation]>=1.23.0
pip install tensorflow>=2.12.0
pip install pandas scikit-learn matplotlib seaborn
pip install jupyter ipykernel
```

### Step 1.5: Verify Installation

```bash
python verify_setup.py
```

This script will check:
- ✅ All required packages are installed
- ✅ All project files exist
- ✅ Modules can be imported
- ✅ System is ready for experiments

## Step 2: Run Your First Experiment

### Option A: Using Jupyter Notebook (Recommended for beginners)

1. Start Jupyter:
```bash
jupyter notebook
```

2. Open `main_notebook.ipynb`

3. Update the dataset path in cell 4:
```python
df = pd.read_csv("path/to/your/cleaned_train_test_network.csv")
```

4. Run all cells (Cell → Run All)

5. Wait for training to complete (~5-10 minutes)

6. View results and visualizations

### Option B: Using Flower CLI (Advanced)

```bash
# Run with default configuration
flwr run .

# Override configuration
flwr run . --run-config "num-server-rounds=10 mu=0.05 batch-size=128"
```

### Option C: Programmatic Usage

```python
from FL_TensorF_Flower_PROX import task, utils
import numpy as np

# Load your data
X_train, y_train = ...  # Your training data
X_test, y_test = ...    # Your test data

# Split into non-IID partitions
client_data = utils.split_data_non_iid_label(
    X_train, y_train, 
    n_clients=3, 
    alpha=0.4
)

# Create model
model = task.get_model_by_type('mlp_binary', input_shape=30, num_classes=1)

# Use Flower simulation (see main_notebook.ipynb for complete example)
```

## Step 3: Customize Configuration

Edit `pyproject.toml` to change settings:

```toml
[tool.flwr.app.config]
num-server-rounds = 10        # Number of FL rounds
local-epochs = 2              # Epochs per client per round
batch-size = 128              # Batch size
learning-rate = 0.001         # Learning rate
mu = 0.01                     # FedProx proximal term coefficient
model-type = "mlp_binary"     # Model architecture
```

## Configuration Options

| Parameter | Default | Description | Typical Range |
|-----------|---------|-------------|---------------|
| `num-server-rounds` | 5 | Federated learning rounds | 5-50 |
| `local-epochs` | 1 | Training epochs per round | 1-5 |
| `batch-size` | 256 | Batch size for training | 32-512 |
| `learning-rate` | 0.001 | Adam optimizer learning rate | 0.0001-0.01 |
| `mu` | 0.01 | Proximal term coefficient | 0.001-0.1 |
| `model-type` | mlp_binary | Model architecture | mlp_binary, cnn_binary, mlp_multi, cnn_multi |
| `input-shape` | 30 | Number of input features | Dataset dependent |
| `num-classes` | 1 | Number of output classes | 1 (binary) or N (multi-class) |

## Understanding FedProx Parameter (μ)

The **mu (μ)** parameter controls the proximal term strength:

- **μ = 0.001** (Low): More local adaptation, potentially faster convergence
- **μ = 0.01** (Default): Balanced between local and global
- **μ = 0.1** (High): Stronger constraint to global model, more stable

**When to increase μ:**
- High data heterogeneity (very non-IID)
- Unstable training
- Client drift issues

**When to decrease μ:**
- Low data heterogeneity
- Need faster local adaptation
- Struggling with convergence

## Expected Output

When running the notebook or CLI, you should see:

```
=== FEDERATED PROXIMAL (FEDPROX) DENGAN FLOWER ===
Konfigurasi: 3 Klien, 5 Putaran, Flower FedProx Algorithm

[INFO] Splitting data for 3 clients with Non-IID (alpha=0.4)...
    Client 1: 1234 samples, distribution: {0: 800, 1: 434}
    Client 2: 2345 samples, distribution: {0: 1200, 1: 1145}
    Client 3: 1789 samples, distribution: {0: 600, 1: 1189}

[INFO] Starting Flower federated learning for mlp_binary...
   Clients: 3 | Rounds: 5 | Local epochs: 1

--- Round 1/5 ---
      Round 1 - Avg Train Loss: 0.3234
      Round 1 - Avg Train Acc: 0.8567 - Time: 12.34s

--- Round 2/5 ---
      Round 2 - Avg Train Loss: 0.2145
      Round 2 - Avg Train Acc: 0.9123 - Time: 11.89s

...

📊 Federated Learning with FedProx completed for mlp_binary
   Total rounds: 5
   Proximal term coefficient (mu): 0.01

📊 EVALUATION METRICS - MLP Binary:
   • Accuracy: 0.9456
   • Precision: 0.9234
   • Recall: 0.9567
   • F1 Score: 0.9398
```

## Troubleshooting

### Issue: ModuleNotFoundError
**Solution:** Install missing packages
```bash
pip install -r requirements.txt
```

### Issue: CUDA/GPU errors
**Solution:** Use CPU version of TensorFlow
```bash
pip install tensorflow-cpu>=2.12.0
```

### Issue: Out of memory
**Solution:** Reduce batch size in configuration
```python
batch_size = 64  # Instead of 256
```

### Issue: Dataset not found
**Solution:** Update path in notebook
```python
df = pd.read_csv("your/actual/path/to/cleaned_train_test_network.csv")
```

### Issue: Flower simulation fails
**Solution:** Check Flower version
```bash
pip install --upgrade "flwr[simulation]>=1.23.0"
```

## FedProx vs FedAvg

| Aspect | FedAvg | FedProx |
|--------|---------|---------|
| **Local Loss** | Standard loss only | Loss + proximal term |
| **Convergence** | May diverge with heterogeneity | More stable |
| **Best For** | IID or mildly non-IID data | Highly non-IID data |
| **Hyperparameters** | Learning rate, epochs | Learning rate, epochs, **μ** |
| **Implementation** | Simple | Slightly more complex |

**Use FedProx when:**
- ✅ Data is highly non-IID across clients
- ✅ Clients have different computational capabilities
- ✅ You need more stable convergence
- ✅ FedAvg shows divergence or instability

## Next Steps

1. **Experiment with μ values:**
   - Try μ ∈ {0.001, 0.01, 0.05, 0.1}
   - Compare convergence and performance

2. **Test different data distributions:**
   - Change alpha parameter (0.1 to 1.0)
   - Observe impact on training

3. **Try different models:**
   - Compare MLP vs CNN
   - Binary vs Multi-class classification

4. **Scale up:**
   - Increase number of clients (5, 10, 20)
   - More communication rounds (10, 20, 50)

5. **Deploy to production:**
   - See Flower deployment documentation
   - Configure real distributed setup

## Useful Resources

- 📚 [FedProx Paper](https://arxiv.org/abs/1812.06127)
- 📘 [Flower Documentation](https://flower.ai/docs/)
- 💻 [Flower GitHub Examples](https://github.com/adap/flower/tree/main/examples)
- 🎓 [Flower TensorFlow Tutorial](https://flower.ai/docs/framework/tutorial-quickstart-tensorflow.html)

## Getting Help

- Check `README.md` for detailed project information
- Review `MIGRATION_GUIDE.md` for migration from FedAvg
- Consult `main_notebook.ipynb` for complete examples
- Visit [Flower Community](https://flower.ai/community)

---

**Ready to start?** Run `python verify_setup.py` now! 🚀
