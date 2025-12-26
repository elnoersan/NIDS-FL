# Federated Learning with Flower and TensorFlow (FedProx)

This project implements Federated Proximal (FedProx) using the Flower framework for the ToN-IoT network intrusion detection dataset.

## Project Structure

```
FL_TensorF_Flower_PROX/
├── __init__.py          # Package initialization
├── task.py              # Model definitions (MLP & CNN) and ProximalModel class
├── client_app.py        # Flower ClientApp with FedProx train and evaluate methods
├── server_app.py        # Flower ServerApp with aggregation strategy
├── utils.py             # Utility functions for data splitting and evaluation
├── pyproject.toml       # Project configuration and dependencies
├── requirements.txt     # Python package dependencies
└── README.md            # This file
```

## What is FedProx?

FedProx (Federated Proximal) is an extension of Federated Averaging (FedAvg) that adds a proximal term to the local objective function. This helps with:

- **Handling system heterogeneity**: Different clients may have varying computational capabilities
- **Statistical heterogeneity**: Non-IID data distribution across clients
- **Improved convergence**: The proximal term prevents local models from diverging too far from the global model

### Mathematical Formulation

In FedProx, each client minimizes:

```
h_k(w) = F_k(w) + (μ/2)||w - w^t||²
```

Where:
- `F_k(w)` is the local loss function
- `w^t` is the current global model
- `μ` is the proximal term coefficient (default: 0.01)

## Features

- **Multiple Model Architectures**: 
  - MLP and CNN for binary classification (Normal vs Attack)
  - MLP and CNN for multi-class classification (Attack type detection)
  
- **Non-IID Data Distribution**: 
  - Uses Dirichlet distribution to simulate realistic federated scenarios
  - Configurable alpha parameter for controlling data heterogeneity

- **FedProx Algorithm**: 
  - Implements proximal term during client training
  - Configurable μ parameter for proximal regularization
  - Uses weighted aggregation based on client data sizes

## Installation

```bash
# Install dependencies
pip install flwr[simulation]>=1.23.0
pip install tensorflow>=2.12.0
pip install pandas scikit-learn matplotlib seaborn
```

Or install from requirements file:

```bash
pip install -r requirements.txt
```

## Usage

### From Notebook

See the example notebooks in the parent directory for comprehensive examples that:
1. Load and preprocess the ToN-IoT dataset
2. Split data into non-IID partitions
3. Train multiple models using Flower with FedProx
4. Evaluate and compare results

### From Command Line

```bash
# Run with default configuration
flwr run .

# Override configuration (example: change mu value)
flwr run . --run-config "num-server-rounds=10 batch-size=128 mu=0.05"
```

## Configuration

Edit `pyproject.toml` to customize:

- `num-server-rounds`: Number of federated learning rounds
- `local-epochs`: Number of local training epochs per round
- `batch-size`: Batch size for training
- `learning-rate`: Learning rate for optimizer
- `mu`: FedProx proximal term coefficient (default: 0.01)
- `model-type`: One of ['mlp_binary', 'cnn_binary', 'mlp_multi', 'cnn_multi']

### FedProx-Specific Parameters

- **mu (μ)**: Controls the strength of the proximal term
  - Higher values: Keep local models closer to global model
  - Lower values: Allow more local adaptation
  - Typical range: 0.001 to 0.1
  - Default: 0.01

## Model Types

1. **mlp_binary**: Multi-layer Perceptron for binary classification
2. **cnn_binary**: Convolutional Neural Network for binary classification
3. **mlp_multi**: Multi-layer Perceptron for multi-class classification
4. **cnn_multi**: Convolutional Neural Network for multi-class classification

## Key Differences from FedAvg

| Aspect | FedAvg | FedProx |
|--------|---------|---------|
| Local Objective | Standard loss only | Loss + proximal term |
| Convergence | May struggle with heterogeneity | Better with heterogeneous data |
| Hyperparameters | Learning rate, epochs | Learning rate, epochs, μ |
| Server Aggregation | Weighted averaging | Same weighted averaging |
| Use Case | IID or mildly non-IID data | Highly non-IID data |

## Performance Metrics

The framework tracks:
- Training accuracy and loss per round (including proximal term contribution)
- Evaluation accuracy and loss
- Precision, Recall, and F1 Score
- Per-client statistics

## Implementation Details

### Client-Side (client_app.py)
- Wraps base model with `ProximalModel` class
- Adds proximal term `(μ/2)||w - w_global||²` to loss
- Trains with custom `train_step` that computes gradients including proximal term

### Server-Side (server_app.py)
- Uses standard FedAvg aggregation (weighted by client data sizes)
- Broadcasts updated global model to clients each round

### ProximalModel Class (task.py)
- Custom Keras Model that overrides `train_step`
- Maintains reference to global weights
- Computes total loss = local loss + proximal term

## Example Usage in Python

```python
from FL_TensorF_Flower_PROX import task, utils, client_app, server_app
import numpy as np

# Prepare your data
X_train, y_train = ...  # Your training data
X_test, y_test = ...    # Your test data

# Split into non-IID partitions
client_data = utils.split_data_non_iid_label(
    X_train, y_train, 
    n_clients=3, 
    alpha=0.4
)

# Configure and run (typically done through Flower's run command)
# See notebooks for complete examples
```

## References

- [FedProx Paper](https://arxiv.org/abs/1812.06127) - Li et al., "Federated Optimization in Heterogeneous Networks"
- [Flower Documentation](https://flower.ai/docs/)
- [Flower TensorFlow Tutorial](https://flower.ai/docs/framework/tutorial-quickstart-tensorflow.html)
- [FedAvg Paper](https://arxiv.org/abs/1602.05629)

## Citation

If you use this code, please cite the FedProx paper:

```bibtex
@inproceedings{li2020federated,
  title={Federated optimization in heterogeneous networks},
  author={Li, Tian and Sahu, Anit Kumar and Zaheer, Manzil and Sanjabi, Maziar and Talwalkar, Ameet and Smith, Virginia},
  booktitle={Proceedings of Machine Learning and Systems},
  volume={2},
  pages={429--450},
  year={2020}
}
```

## License

Apache-2.0

## Author

elnoersan
