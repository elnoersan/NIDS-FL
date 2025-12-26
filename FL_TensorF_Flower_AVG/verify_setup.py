#!/usr/bin/env python3
"""
Verification script for FL_TensorF_Flower installation and setup.

Run this script to verify that all dependencies are installed correctly
and the project structure is set up properly.
"""

import sys
import importlib.util

def check_import(module_name, display_name=None):
    """Check if a module can be imported."""
    if display_name is None:
        display_name = module_name
    
    try:
        spec = importlib.util.find_spec(module_name)
        if spec is not None:
            module = importlib.import_module(module_name)
            version = getattr(module, '__version__', 'unknown')
            print(f"✅ {display_name}: {version}")
            return True
        else:
            print(f"❌ {display_name}: NOT FOUND")
            return False
    except Exception as e:
        print(f"❌ {display_name}: ERROR - {str(e)}")
        return False

def check_file_exists(filepath):
    """Check if a file exists."""
    import os
    if os.path.exists(filepath):
        print(f"✅ {filepath}")
        return True
    else:
        print(f"❌ {filepath} - NOT FOUND")
        return False

def main():
    """Main verification function."""
    print("="*70)
    print("FL_TensorF_Flower - Installation Verification")
    print("="*70)
    
    print("\n📦 Checking Python version...")
    print(f"   Python {sys.version}")
    
    print("\n📦 Checking required packages...")
    packages_ok = True
    packages_ok &= check_import('flwr', 'Flower')
    packages_ok &= check_import('tensorflow', 'TensorFlow')
    packages_ok &= check_import('numpy', 'NumPy')
    packages_ok &= check_import('pandas', 'Pandas')
    packages_ok &= check_import('sklearn', 'scikit-learn')
    packages_ok &= check_import('matplotlib', 'Matplotlib')
    packages_ok &= check_import('seaborn', 'Seaborn')
    
    print("\n📁 Checking project files...")
    files_ok = True
    files_ok &= check_file_exists('task.py')
    files_ok &= check_file_exists('client_app.py')
    files_ok &= check_file_exists('server_app.py')
    files_ok &= check_file_exists('utils.py')
    files_ok &= check_file_exists('pyproject.toml')
    files_ok &= check_file_exists('requirements.txt')
    files_ok &= check_file_exists('main_notebook.ipynb')
    
    print("\n🔧 Checking module imports...")
    imports_ok = True
    try:
        from task import get_model_by_type
        print("✅ task.get_model_by_type")
    except Exception as e:
        print(f"❌ task.get_model_by_type - {str(e)}")
        imports_ok = False
    
    try:
        from utils import split_data_non_iid_label
        print("✅ utils.split_data_non_iid_label")
    except Exception as e:
        print(f"❌ utils.split_data_non_iid_label - {str(e)}")
        imports_ok = False
    
    print("\n" + "="*70)
    
    if packages_ok and files_ok and imports_ok:
        print("✅ ALL CHECKS PASSED!")
        print("\nYou're ready to run the federated learning experiments.")
        print("\nNext steps:")
        print("  1. Open main_notebook.ipynb in Jupyter")
        print("  2. Run all cells to start training")
        print("  3. Check the generated visualizations")
        return 0
    else:
        print("❌ SOME CHECKS FAILED!")
        print("\nPlease fix the issues above before proceeding.")
        print("\nCommon solutions:")
        print("  • Install missing packages: pip install -r requirements.txt")
        print("  • Make sure you're in the FL_TensorF_Flower directory")
        print("  • Check that all files are present")
        return 1

if __name__ == "__main__":
    sys.exit(main())
