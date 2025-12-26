#!/usr/bin/env python3
"""
FedProx Grid Search Environment Verification
============================================

Quick check to ensure everything is ready before running grid search.
Run this before starting your experiments.

Usage: python3 verify_setup.py
"""

import sys
import os
from pathlib import Path

def check_mark(condition, message):
    """Print check result"""
    if condition:
        print(f"✅ {message}")
        return True
    else:
        print(f"❌ {message}")
        return False

def main():
    print("="*80)
    print("FEDPROX GRID SEARCH - ENVIRONMENT VERIFICATION")
    print("="*80)
    print()
    
    all_good = True
    
    # Check Python version
    print("📋 PYTHON ENVIRONMENT")
    print("-" * 40)
    version = sys.version_info
    all_good &= check_mark(
        version.major == 3 and version.minor >= 8,
        f"Python version: {version.major}.{version.minor}.{version.micro} (Requires 3.8+)"
    )
    
    # Check virtual environment
    venv_active = os.environ.get('VIRTUAL_ENV') is not None
    check_mark(venv_active, f"Virtual environment: {'Active' if venv_active else 'Not active (recommended)'}")
    
    print()
    
    # Check required packages
    print("📦 REQUIRED PACKAGES")
    print("-" * 40)
    
    packages = {
        'tensorflow': 'tensorflow',
        'flwr': 'flwr',
        'pandas': 'pandas',
        'numpy': 'numpy',
        'sklearn': 'scikit-learn',
        'matplotlib': 'matplotlib',
        'seaborn': 'seaborn'
    }
    
    for import_name, package_name in packages.items():
        try:
            mod = __import__(import_name)
            version = getattr(mod, '__version__', 'unknown')
            check_mark(True, f"{package_name}: {version}")
        except ImportError:
            all_good &= check_mark(False, f"{package_name}: NOT INSTALLED")
    
    print()
    
    # Check files
    print("📁 REQUIRED FILES")
    print("-" * 40)
    
    script_dir = Path(__file__).parent
    parent_dir = script_dir.parent
    
    files = {
        'run_gridsearch.py': script_dir / 'run_gridsearch.py',
        'research_hypertuning_gridsearch.py': script_dir / 'research_hypertuning_gridsearch.py',
        'check_progress.py': script_dir / 'check_progress.py',
        'start_gridsearch.sh': script_dir / 'start_gridsearch.sh',
        'task.py (parent)': parent_dir / 'task.py',
        'utils.py (parent)': parent_dir / 'utils.py',
    }
    
    for name, path in files.items():
        all_good &= check_mark(path.exists(), f"{name}: {path}")
    
    print()
    
    # Check dataset
    print("💾 DATASET")
    print("-" * 40)
    
    dataset_path = Path("/home/elnoersan/Skripsi/Paper/NotebookTODO/train_test_network.csv")
    dataset_exists = dataset_path.exists()
    all_good &= check_mark(dataset_exists, f"TON_IoT dataset: {dataset_path}")
    
    if dataset_exists:
        size_mb = dataset_path.stat().st_size / (1024 * 1024)
        print(f"   └─ Size: {size_mb:.2f} MB")
    
    print()
    
    # Check ProximalModel in task.py
    print("🔬 FEDPROX REQUIREMENTS")
    print("-" * 40)
    
    task_file = parent_dir / 'task.py'
    if task_file.exists():
        content = task_file.read_text()
        has_proximal = 'class ProximalModel' in content
        all_good &= check_mark(has_proximal, "ProximalModel class in task.py (Required for FedProx)")
    else:
        all_good &= check_mark(False, "task.py not found")
    
    print()
    
    # Check disk space
    print("💿 SYSTEM RESOURCES")
    print("-" * 40)
    
    try:
        import shutil
        total, used, free = shutil.disk_usage(script_dir)
        free_gb = free / (1024 ** 3)
        check_mark(
            free_gb >= 5,
            f"Free disk space: {free_gb:.2f} GB (Requires ~5GB for results)"
        )
    except Exception:
        print("⚠️  Could not check disk space")
    
    # Check GPU
    try:
        import tensorflow as tf
        gpus = tf.config.list_physical_devices('GPU')
        if gpus:
            check_mark(True, f"GPU available: {len(gpus)} device(s) detected")
            for i, gpu in enumerate(gpus):
                print(f"   └─ GPU {i}: {gpu.name}")
        else:
            print("⚠️  No GPU detected (CPU mode - will be slower)")
    except Exception as e:
        print(f"⚠️  Could not check GPU: {e}")
    
    print()
    print("="*80)
    
    if all_good:
        print("✅ ALL CHECKS PASSED - READY TO RUN!")
        print()
        print("To start grid search:")
        print("  ./start_gridsearch.sh")
        print()
        print("Expected duration: 8-12 hours for 24 experiments")
        print("="*80)
        return 0
    else:
        print("❌ SOME CHECKS FAILED - PLEASE FIX ISSUES ABOVE")
        print()
        print("Common fixes:")
        print("  - Missing packages: pip install tensorflow flwr pandas numpy scikit-learn matplotlib seaborn")
        print("  - Missing ProximalModel: Ensure task.py contains the ProximalModel class")
        print("  - Missing dataset: Check dataset path is correct")
        print("="*80)
        return 1

if __name__ == "__main__":
    sys.exit(main())
