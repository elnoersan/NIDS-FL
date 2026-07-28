# Network Intrusion Detection System using Federated Learning (NIDS-FL)

**Research Title**: Detection and Classification of Smart City Network Attacks Using Federated Learning on Network Traffic  
**Author**: Rian Nur Ikhsan (22523297)  
**Full Thesis Document**: [Download PDF](https://dspace.uii.ac.id/bitstream/handle/123456789/63052/22523297.pdf?sequence=1&isAllowed=y)

## Overview
This repository contains the full CRISP-DM implementation for the thesis research on Federated Learning (FL) applied to Smart City Intrusion Detection Systems (NIDS) using the TON-IoT dataset.

To ensure robustness, solve Out-Of-Memory (OOM) leaks, and guarantee accurate apples-to-apples comparisons, the entire pipeline is orchestrated via a unified Bash script (`run_pipeline.sh`) and the Federated Learning backend has been completely **migrated to PyTorch**.

## Project Structure

- **`run_pipeline.sh`**: The master orchestrator script. Runs the entire CRISP-DM pipeline from data ingestion to Markdown report generation.
- **`benchmark_federated_algorithms.py`**: The core PyTorch FL simulation engine. Replaces the old TensorFlow/Flower implementation. Features aggressive VRAM garbage collection (`torch.cuda.empty_cache()`) to prevent OOM errors across thousands of training rounds.
- **`phase2_data_understanding.py`**: Performs EDA and outputs statistical distribution of the raw network data.
- **`phase5_report_generator.py`**: Automatically parses JSON results and generates the final English academic report (`THESIS_EXPERIMENT_REPORT.md`).
- **`EDA/preprocessing_pipeline.py`**: The data cleaning script that generates lightweight `.pkl` artifacts.
- **`Research_Notebooks/`**: Contains all historical Jupyter Notebooks (`.ipynb`) used for past EDA, Flower tests, and TensorFlow grid searches.
- **`train_test_network.csv`**: The raw TON-IoT network dataset (must be placed in the project root).

## Key Features

1. **PyTorch Engine**: Fully hardware-aware (`.to(device)`) PyTorch implementation that maximally utilizes NVIDIA GPUs without crashing.
2. **Apples-to-Apples Evaluation**: Uses a seeded Dirichlet distribution logic to ensure `FedAvg` and `FedProx` are evaluated on the exact same Non-IID data splits.
3. **Automated CRISP-DM**: The pipeline handles Phase 1 to Phase 5 autonomously.
4. **Custom FedProx**: Exact mathematical implementation of the proximal term $\frac{\mu}{2} ||w - w^t||^2$ injected directly into the PyTorch `loss.backward()` gradient calculation.

## How to Run (Quick Start)

The entire experiment is designed to be executed with a single command. 

### 1. Setup Environment
Ensure your Python virtual environment has PyTorch installed with CUDA support.
```bash
source ../Paper/.venv/bin/activate
pip install torch torchvision torchaudio pandas numpy scikit-learn
```

### 2. Prepare Dataset
Ensure `train_test_network.csv` is located in the root of this repository (`NIDS-FL/`).

### 3. Run the Full Pipeline
To run the full thesis experiment (Preprocessing -> EDA -> FL Benchmark -> Report):
```bash
./run_pipeline.sh
```

### 4. Run Benchmark Only (Skip Preprocessing)
If you have already generated the `.pkl` files and only want to re-run the PyTorch Federated Learning benchmark:
```bash
./run_pipeline.sh --skip-preprocessing
```

## Experimental Scenarios

The `benchmark_federated_algorithms.py` script automatically runs 24 thesis-aligned scenarios:
- **Tasks**: Binary Classification vs Multiclass Classification
- **Models**: MLP vs CNN-1D
- **Algorithms**: FedAvg vs FedProx (μ=0.01, μ=0.001)
- **Data Heterogeneity (Non-IID)**: Dirichlet Alpha = 0.3 (extreme) vs 5.0 (IID-like)
- **Settings**: 5 Clients, 20 Communication Rounds, Batch Size = 512.

## Output Artifacts

Upon completion, the pipeline automatically generates:
1. `THESIS_EXPERIMENT_REPORT.md`: A comprehensive, formatted English academic report ready to be attached to your thesis.
2. `thesis_benchmark_results_pytorch.json`: Raw benchmark metrics for plotting and evaluation.
3. `EDA/data_understanding_report.json`: Data statistics.
