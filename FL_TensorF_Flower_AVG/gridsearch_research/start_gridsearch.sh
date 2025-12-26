#!/usr/bin/env bash
# Quick start script for hyperparameter grid search

echo "=============================================================================="
echo "  FedAvg Hyperparameter Grid Search"
echo "=============================================================================="
echo ""
echo "This will run 96 experiments with the following combinations:"
echo "  - Batch Sizes: 256, 512, 1024"
echo "  - Local Epochs: 1, 2"
echo "  - Learning Rates: 0.001, 0.0005"
echo "  - Alphas (Dirichlet): 0.3, 5.0"
echo ""
echo "Each experiment trains 4 models (MLP Binary, CNN Binary, MLP Multi, CNN Multi)"
echo "Total models to train: 576"
echo ""
echo "Estimated total time: Varies based on configuration"
echo "Results will be saved to gridsearch_research/"
echo ""
echo "=============================================================================="
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Check if virtual environment is activated
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "⚠️  Warning: Virtual environment not detected"
    echo "Attempting to activate virtual environment..."
    
    if [[ -f "/home/elnoersan/Skripsi/Paper/.venv/bin/activate" ]]; then
        source "/home/elnoersan/Skripsi/Paper/.venv/bin/activate"
        echo "✓ Virtual environment activated"
    else
        echo "❌ Could not find virtual environment at /home/elnoersan/Skripsi/Paper/.venv"
        echo "Please activate your virtual environment manually and try again."
        exit 1
    fi
fi

# Check if required files exist
if [[ ! -f "run_gridsearch.py" ]]; then
    echo "❌ Error: run_gridsearch.py not found"
    exit 1
fi

if [[ ! -f "research_hypertuning_gridsearch.py" ]]; then
    echo "❌ Error: research_hypertuning_gridsearch.py not found"
    exit 1
fi

# Check for task.py and utils.py in parent directory
if [[ ! -f "../task.py" ]] || [[ ! -f "../utils.py" ]]; then
    echo "❌ Error: Required files (task.py, utils.py) not found in parent directory"
    echo "Expected location: $(cd .. && pwd)"
    exit 1
fi

echo "✓ All required files found"
echo ""

# Confirm before starting
read -p "Do you want to start the grid search? (yes/no): " -r
echo ""

if [[ ! $REPLY =~ ^[Yy]es$ ]] && [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Grid search cancelled."
    exit 0
fi

# Run the grid search
echo "Starting grid search..."
echo "=============================================================================="
echo ""

python run_gridsearch.py

# Check exit code
EXIT_CODE=$?

echo ""
echo "=============================================================================="

if [[ $EXIT_CODE -eq 0 ]]; then
    echo "✓ Grid search completed successfully!"
    echo ""
    echo "Results saved to: $SCRIPT_DIR/gridsearch_research/"
    echo "Summary report: $SCRIPT_DIR/gridsearch_research/summary_report.md"
else
    echo "❌ Grid search failed with exit code $EXIT_CODE"
    echo "Check the logs in gridsearch_research/ for details"
fi

echo "=============================================================================="
