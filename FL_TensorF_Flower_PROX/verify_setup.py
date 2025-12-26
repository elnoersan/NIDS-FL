#!/usr/bin/env python3
"""Setup verification script for FL_TensorF_Flower_PROX.

This script checks if all dependencies and files are properly installed.
"""

import sys
import os
from pathlib import Path

# ANSI color codes for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'


def check_package(package_name, import_name=None):
    """Check if a Python package is installed."""
    if import_name is None:
        import_name = package_name
    
    try:
        __import__(import_name)
        print(f"{GREEN}✓{RESET} {package_name}")
        return True
    except ImportError:
        print(f"{RED}✗{RESET} {package_name} - NOT INSTALLED")
        return False


def check_file(filepath, description):
    """Check if a file exists."""
    if Path(filepath).exists():
        print(f"{GREEN}✓{RESET} {description}: {filepath}")
        return True
    else:
        print(f"{RED}✗{RESET} {description}: {filepath} - NOT FOUND")
        return False


def main():
    """Run all verification checks."""
    print(f"\n{BLUE}{'='*70}{RESET}")
    print(f"{BLUE}FL_TensorF_Flower_PROX - Setup Verification{RESET}")
    print(f"{BLUE}{'='*70}{RESET}\n")
    
    all_passed = True
    
    # Check Python version
    print(f"{YELLOW}Checking Python version...{RESET}")
    py_version = sys.version_info
    if py_version.major == 3 and py_version.minor >= 8:
        print(f"{GREEN}✓{RESET} Python {py_version.major}.{py_version.minor}.{py_version.micro}")
    else:
        print(f"{RED}✗{RESET} Python version should be 3.8 or higher")
        all_passed = False
    
    # Check required packages
    print(f"\n{YELLOW}Checking required packages...{RESET}")
    packages = [
        ('flwr', 'flwr'),
        ('tensorflow', 'tensorflow'),
        ('numpy', 'numpy'),
        ('pandas', 'pandas'),
        ('scikit-learn', 'sklearn'),
        ('matplotlib', 'matplotlib'),
        ('seaborn', 'seaborn'),
        ('jupyter', 'jupyter'),
    ]
    
    for package_name, import_name in packages:
        if not check_package(package_name, import_name):
            all_passed = False
    
    # Check project files
    print(f"\n{YELLOW}Checking project files...{RESET}")
    files = [
        ('__init__.py', 'Package initialization'),
        ('task.py', 'Model definitions'),
        ('client_app.py', 'Client application'),
        ('server_app.py', 'Server application'),
        ('utils.py', 'Utility functions'),
        ('pyproject.toml', 'Project configuration'),
        ('requirements.txt', 'Dependencies list'),
        ('README.md', 'README documentation'),
    ]
    
    for filename, description in files:
        if not check_file(filename, description):
            all_passed = False
    
    # Check if modules can be imported
    print(f"\n{YELLOW}Checking module imports...{RESET}")
    try:
        from task import get_model_by_type, ProximalModel
        print(f"{GREEN}✓{RESET} Can import from task.py")
    except ImportError as e:
        print(f"{RED}✗{RESET} Cannot import from task.py: {e}")
        all_passed = False
    
    try:
        from utils import split_data_non_iid_label, evaluate_model_metrics
        print(f"{GREEN}✓{RESET} Can import from utils.py")
    except ImportError as e:
        print(f"{RED}✗{RESET} Cannot import from utils.py: {e}")
        all_passed = False
    
    # Final result
    print(f"\n{BLUE}{'='*70}{RESET}")
    if all_passed:
        print(f"{GREEN}✓ All checks passed! You're ready to start.{RESET}")
        print(f"\n{YELLOW}Next steps:{RESET}")
        print(f"  1. Read QUICKSTART.md for usage instructions")
        print(f"  2. Open main_notebook.ipynb to run experiments")
        print(f"  3. Or use: flwr run . (for CLI usage)")
    else:
        print(f"{RED}✗ Some checks failed. Please install missing dependencies.{RESET}")
        print(f"\n{YELLOW}To install dependencies:{RESET}")
        print(f"  pip install -r requirements.txt")
        return 1
    
    print(f"{BLUE}{'='*70}{RESET}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
