#!/usr/bin/env fish
# FEDPROX GRID SEARCH LAUNCHER
# =============================
#
# Simple wrapper script to launch the FedProx hyperparameter grid search.
# This script runs the main orchestrator which will execute 24 experiments
# testing different combinations of batch_size, local_epochs, learning_rate, and mu.
#
# Total experiments: 24 (2×2×2×3)
# Expected duration: 8-12 hours
#
# Usage:
#   ./start_gridsearch.sh
#
# Author: AI Assistant for Federated Learning Research
# Date: December 2025

echo "================================================================================"
echo "FEDPROX HYPERPARAMETER GRID SEARCH"
echo "================================================================================"
echo ""
echo "This will start 288 experiments testing different hyperparameter combinations:"
echo "  - Batch Sizes: [256, 512, 1024]"
echo "  - Local Epochs: [1, 2]"
echo "  - Learning Rates: [0.001, 0.0005]"
echo "  - Mu (Proximal Term): [0.01, 0.001]"
echo "  - Alphas (Dirichlet): [0.3, 5.0]"
echo ""
echo "Each experiment trains 4 models (MLP Binary, CNN Binary, MLP Multi, CNN Multi)"
echo "Total models to train: 1152"
echo ""
echo "Estimated time: 8-12 hours"
echo ""
echo "================================================================================"
echo ""

# Check if Python virtual environment is activated
if test -z "$VIRTUAL_ENV"
    echo "⚠️  WARNING: No Python virtual environment detected!"
    echo "   It's recommended to activate your venv first."
    echo ""
    read -P "Continue anyway? [y/N] " -n 1 response
    echo ""
    if test "$response" != "y" -a "$response" != "Y"
        echo "Cancelled by user."
        exit 0
    end
end

# Get the directory where this script is located
set SCRIPT_DIR (dirname (status --current-filename))

# Check if run_gridsearch.py exists
if not test -f "$SCRIPT_DIR/run_gridsearch.py"
    echo "❌ ERROR: run_gridsearch.py not found in $SCRIPT_DIR"
    exit 1
end

# Run the grid search
echo "🚀 Starting grid search..."
echo ""

python3 "$SCRIPT_DIR/run_gridsearch.py"

set EXIT_CODE $status

echo ""
echo "================================================================================"

if test $EXIT_CODE -eq 0
    echo "✅ Grid search completed successfully!"
    echo ""
    echo "Results are saved in: $SCRIPT_DIR/grid_search_results/"
    echo ""
    echo "Files generated:"
    echo "  - all_experiments.json : Detailed tracking data"
    echo "  - summary_report.md    : Comprehensive analysis report"
    echo "  - Individual experiment folders with results"
    echo ""
    echo "To view progress anytime, run:"
    echo "  python3 check_progress.py"
else
    echo "❌ Grid search failed with exit code: $EXIT_CODE"
    echo ""
    echo "Check the experiment logs in grid_search_results/ for details."
end

echo "================================================================================"

exit $EXIT_CODE
