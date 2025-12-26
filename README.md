# Network Intrusion Detection System using Federated Learning (NIDS-FL)

## Overview
Research implementation of Network Intrusion Detection System for Smart City environments using Federated Learning on the TON-IoT dataset.

**Research Title**: Detection and Classification of Smart City Network Attacks Using Federated Learning on Network Traffic

## Project Structure

### Data Analysis & Preprocessing (`EDA/`)
- **Preprocessing Pipeline**: Automated data cleaning and feature engineering
  - Binary classification (Normal vs Attack)
  - Multi-class classification (Attack type detection)
  - Time saving: ~5-10 minutes → <5 seconds with preprocessed artifacts
- **Exploratory Data Analysis**: Comprehensive dataset analysis and visualization
- **Cleaned Dataset**: TON-IoT network traffic data (train/test split)

### Federated Learning Implementations

#### FL_TensorF_Flower_AVG (FedAvg)
- **Algorithm**: Federated Averaging (McMahan et al.)
- **Framework**: Flower + TensorFlow/Keras
- **Features**:
  - Multiple model architectures (MLP, CNN)
  - Binary and multi-class classification
  - Non-IID data distribution using Dirichlet distribution
  - Comprehensive grid search for hyperparameter optimization
- **Grid Search**: 20 hyperparameter combinations
  - Batch sizes: [256, 512, 1024]
  - Local epochs: [1, 2]
  - Learning rates: [0.001, 0.0005]
  - Alpha (Dirichlet): [0.3, 5.0] for data heterogeneity
- **Components**:
  - `client_app.py`: Client-side training logic
  - `server_app.py`: Server-side aggregation
  - `task.py`: Model definitions (MLP, CNN)
  - `utils.py`: Data partitioning and evaluation utilities

#### FL_TensorF_Flower_PROX (FedProx)
- **Algorithm**: Federated Proximal (Li et al.)
- **Key Difference**: Adds proximal term `(μ/2)||w - w^t||²` to local objective
- **Benefits**:
  - Handles system heterogeneity (varying client capabilities)
  - Improved convergence for non-IID data
  - Prevents local models from diverging too far from global model
- **Proximal Term (μ)**: [0.001, 0.01]
- **Similar grid search capabilities as FedAvg**

### Experimental Results (`ShortResult/`)
- Comprehensive training results and metrics
- Performance comparison between FedAvg and FedProx
- Various hyperparameter configurations (alpha 0.3 vs 5.0, different mu values)

## Key Features

### Model Architectures
- **MLP (Multi-Layer Perceptron)**:
  - Input layer (30 features after preprocessing)
  - Hidden layers with dropout for regularization
  - Binary output (sigmoid) or multi-class output (softmax)
- **CNN (Convolutional Neural Network)**:
  - 1D convolution for network traffic patterns
  - Max pooling and dropout layers
  - Dense layers for classification

### Data Partitioning
- **Non-IID Distribution**: Dirichlet distribution simulation
  - Alpha = 0.3: High heterogeneity (realistic scenario)
  - Alpha = 5.0: Near-IID (baseline comparison)
- **Clients**: Configurable (typically 3-5 clients)
- **Federated Rounds**: 20-50 rounds per experiment

### Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-Score
- Training/validation loss curves
- Confusion matrices

## Quick Start

### 1. Data Preprocessing
```bash
cd EDA
python preprocessing_pipeline.py --mode full
```

### 2. Run FedAvg Experiment
```bash
cd FL_TensorF_Flower_AVG
pip install -r requirements.txt
python verify_setup.py
# Run via notebook or CLI
flwr run .
```

### 3. Run FedProx Experiment
```bash
cd FL_TensorF_Flower_PROX
pip install -r requirements.txt
python verify_setup.py
# Run via notebook or CLI
flwr run . --run-config "mu=0.01"
```

### 4. Grid Search (Optional)
```bash
cd FL_TensorF_Flower_AVG/gridsearch_research
python run_gridsearch.py
```

## Requirements
- Python 3.8+
- TensorFlow >= 2.12.0
- Flower (flwr) >= 1.23.0
- pandas, scikit-learn, matplotlib, seaborn
- TON-IoT dataset (cleaned version)

## Dataset
**TON-IoT Network Dataset**: IoT/IIoT network traffic with labeled attacks
- Network features: 30 selected features after preprocessing
- Attack types: DDoS, DoS, Scanning, Backdoor, XSS, Password, Injection, Ransomware, MITM
- Binary labels: Normal (0) vs Attack (1)
- Multi-class labels: 9 attack categories + Normal

## Research Contributions
- Implementation of FedAvg and FedProx for network intrusion detection
- Comprehensive hyperparameter optimization framework
- Non-IID data distribution simulation for realistic federated scenarios
- Performance comparison across different data heterogeneity levels
- Model architecture comparison (MLP vs CNN) for network traffic analysis

## Project Status
Active research project - Thesis in progress

## License
Academic research project

## Contact
- **Author**: elnoersan (Nur Ikhsan)
