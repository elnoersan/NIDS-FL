#!/usr/bin/env python3
"""
Hyperparameter Grid Search for Federated Learning
==================================================
This script orchestrates a comprehensive grid search over:
- BATCH_SIZE: [256]
- LOCAL_EPOCHS: [1]
- LEARNING_RATE: [0.001, 0.0005]
- ALPHA: [0.1, 0.3, 0.5] (Dirichlet Non-IID parameter)

Total combinations calculated at runtime
Each run will be documented in gridsearch_research/<experiment_name>/
"""

import os
import sys
import json
import time
import subprocess
from datetime import datetime
from pathlib import Path
import itertools

# ============================================================================
# GRID SEARCH CONFIGURATION
# ============================================================================
BATCH_SIZES = [256, 512, 1024]
LOCAL_EPOCHS = [1, 2]
LEARNING_RATES = [0.001, 0.0005]
ALPHAS = [0.3, 5.0]  # Dirichlet distribution parameter (heterogeneity level)

# Base directory for all experiments
BASE_DIR = Path(__file__).parent / "gridsearch_research"
BASE_DIR.mkdir(exist_ok=True)

# Main script to run
MAIN_SCRIPT = Path(__file__).parent / "research_hypertuning_gridsearch.py"

# ============================================================================
# EXPERIMENT TRACKING
# ============================================================================
class ExperimentTracker:
    """Track all experiments and their results"""
    
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.results_file = self.base_dir / "all_experiments.json"
        self.summary_file = self.base_dir / "summary_report.md"
        self.experiments = []
        
    def create_experiment_name(self, batch_size, local_epochs, learning_rate, alpha):
        """Create a unique name for the experiment"""
        lr_str = f"{learning_rate:.4f}".replace(".", "p")
        alpha_str = f"{alpha:.1f}".replace(".", "p")
        return f"bs{batch_size}_epoch{local_epochs}_lr{lr_str}_alpha{alpha_str}"
    
    def create_experiment_dir(self, exp_name):
        """Create directory for experiment"""
        exp_dir = self.base_dir / exp_name
        exp_dir.mkdir(exist_ok=True)
        return exp_dir
    
    def log_experiment_start(self, exp_name, params):
        """Log when experiment starts"""
        exp_info = {
            'name': exp_name,
            'params': params,
            'status': 'running',
            'start_time': datetime.now().isoformat(),
            'end_time': None,
            'duration': None,
            'error': None
        }
        self.experiments.append(exp_info)
        self._save_progress()
        
    def log_experiment_end(self, exp_name, success=True, error=None):
        """Log when experiment ends"""
        for exp in self.experiments:
            if exp['name'] == exp_name:
                exp['status'] = 'completed' if success else 'failed'
                exp['end_time'] = datetime.now().isoformat()
                
                # Calculate duration
                start = datetime.fromisoformat(exp['start_time'])
                end = datetime.fromisoformat(exp['end_time'])
                exp['duration'] = (end - start).total_seconds()
                
                if error:
                    exp['error'] = str(error)
                break
        
        self._save_progress()
    
    def _save_progress(self):
        """Save current progress to JSON"""
        with open(self.results_file, 'w') as f:
            json.dump(self.experiments, f, indent=2)
    
    def generate_summary_report(self):
        """Generate final markdown summary report"""
        print("\n" + "="*80)
        print("GENERATING COMPREHENSIVE SUMMARY REPORT")
        print("="*80)
        
        with open(self.summary_file, 'w') as f:
            f.write("# Federated Learning Hyperparameter Grid Search - Summary Report\n\n")
            f.write(f"**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"**Total Experiments**: {len(self.experiments)}\n\n")
            
            # Executive Summary
            f.write("## Executive Summary\n\n")
            completed = sum(1 for e in self.experiments if e['status'] == 'completed')
            failed = sum(1 for e in self.experiments if e['status'] == 'failed')
            total_time = sum(e['duration'] for e in self.experiments if e['duration'])
            
            f.write(f"- ✅ **Completed**: {completed}/{len(self.experiments)}\n")
            f.write(f"- ❌ **Failed**: {failed}/{len(self.experiments)}\n")
            f.write(f"- ⏱️ **Total Time**: {total_time/3600:.2f} hours ({total_time/60:.1f} minutes)\n")
            f.write(f"- 📊 **Avg Time per Experiment**: {total_time/len(self.experiments)/60:.1f} minutes\n\n")
            
            # Grid Search Configuration
            f.write("## Grid Search Configuration\n\n")
            f.write("```python\n")
            f.write(f"BATCH_SIZES = {BATCH_SIZES}\n")
            f.write(f"LOCAL_EPOCHS = {LOCAL_EPOCHS}\n")
            f.write(f"LEARNING_RATES = {LEARNING_RATES}\n")
            f.write(f"ALPHAS = {ALPHAS}\n")
            f.write(f"Total Combinations = {len(BATCH_SIZES) * len(LOCAL_EPOCHS) * len(LEARNING_RATES) * len(ALPHAS)}\n")
            f.write("```\n\n")
            
            # All Experiments Table
            f.write("## All Experiments\n\n")
            f.write("| # | Experiment Name | Batch Size | Epochs | Learning Rate | Alpha | Status | Duration (min) |\n")
            f.write("|---|----------------|------------|--------|---------------|-------|--------|----------------|\n")
            
            for idx, exp in enumerate(self.experiments, 1):
                params = exp['params']
                duration = f"{exp['duration']/60:.1f}" if exp['duration'] else "N/A"
                status_icon = "✅" if exp['status'] == 'completed' else "❌"
                
                f.write(f"| {idx} | `{exp['name']}` | {params['batch_size']} | {params['local_epochs']} | "
                       f"{params['learning_rate']} | {params['alpha']} | {status_icon} {exp['status']} | {duration} |\n")
            
            f.write("\n")
            
            # Results Aggregation (will be filled after loading individual results)
            f.write("## Performance Comparison\n\n")
            f.write("### Binary Classification Results\n\n")
            f.write("| Experiment | Batch Size | Epochs | LR | Alpha | MLP Acc | MLP F1 | CNN Acc | CNN F1 |\n")
            f.write("|------------|------------|--------|-----|-------|---------|--------|---------|--------|\n")
            
            # Load and aggregate results from each experiment
            results_data = []
            for exp in self.experiments:
                if exp['status'] == 'completed':
                    exp_dir = self.base_dir / exp['name']
                    results_file = exp_dir / 'results_summary.json'
                    
                    if results_file.exists():
                        with open(results_file, 'r') as rf:
                            results = json.load(rf)
                            results_data.append({
                                'name': exp['name'],
                                'params': exp['params'],
                                'results': results
                            })
                            
                            # Write to table
                            params = exp['params']
                            mlp_bin = results.get('binary', {}).get('MLP Binary', {})
                            cnn_bin = results.get('binary', {}).get('CNN Binary', {})
                            
                            f.write(f"| `{exp['name']}` | {params['batch_size']} | {params['local_epochs']} | "
                                   f"{params['learning_rate']} | {params['alpha']} | "
                                   f"{mlp_bin.get('accuracy', 0):.4f} | {mlp_bin.get('f1_score', 0):.4f} | "
                                   f"{cnn_bin.get('accuracy', 0):.4f} | {cnn_bin.get('f1_score', 0):.4f} |\n")
            
            f.write("\n### Multi-class Classification Results\n\n")
            f.write("| Experiment | Batch Size | Epochs | LR | Alpha | MLP Acc | MLP F1 | CNN Acc | CNN F1 |\n")
            f.write("|------------|------------|--------|-----|-------|---------|--------|---------|--------|\n")
            
            for data in results_data:
                params = data['params']
                results = data['results']
                mlp_multi = results.get('multi', {}).get('MLP Multi', {})
                cnn_multi = results.get('multi', {}).get('CNN Multi', {})
                
                f.write(f"| `{data['name']}` | {params['batch_size']} | {params['local_epochs']} | "
                       f"{params['learning_rate']} | {params['alpha']} | "
                       f"{mlp_multi.get('accuracy', 0):.4f} | {mlp_multi.get('f1_score', 0):.4f} | "
                       f"{cnn_multi.get('accuracy', 0):.4f} | {cnn_multi.get('f1_score', 0):.4f} |\n")
            
            # Best Configurations
            f.write("\n## Best Configurations\n\n")
            
            if results_data:
                # Find best for each metric
                best_mlp_bin_acc = max(results_data, 
                    key=lambda x: x['results'].get('binary', {}).get('MLP Binary', {}).get('accuracy', 0))
                best_cnn_bin_f1 = max(results_data, 
                    key=lambda x: x['results'].get('binary', {}).get('CNN Binary', {}).get('f1_score', 0))
                best_mlp_multi_acc = max(results_data, 
                    key=lambda x: x['results'].get('multi', {}).get('MLP Multi', {}).get('accuracy', 0))
                best_cnn_multi_f1 = max(results_data, 
                    key=lambda x: x['results'].get('multi', {}).get('CNN Multi', {}).get('f1_score', 0))
                
                f.write("### Binary Classification\n\n")
                f.write(f"**Best MLP Binary (Accuracy)**: `{best_mlp_bin_acc['name']}`\n")
                f.write(f"- Parameters: {best_mlp_bin_acc['params']}\n")
                mlp_metrics = best_mlp_bin_acc['results']['binary']['MLP Binary']
                f.write(f"- Accuracy: {mlp_metrics['accuracy']:.4f}\n")
                f.write(f"- F1-Score: {mlp_metrics['f1_score']:.4f}\n\n")
                
                f.write(f"**Best CNN Binary (F1-Score)**: `{best_cnn_bin_f1['name']}`\n")
                f.write(f"- Parameters: {best_cnn_bin_f1['params']}\n")
                cnn_metrics = best_cnn_bin_f1['results']['binary']['CNN Binary']
                f.write(f"- Accuracy: {cnn_metrics['accuracy']:.4f}\n")
                f.write(f"- F1-Score: {cnn_metrics['f1_score']:.4f}\n\n")
                
                f.write("### Multi-class Classification\n\n")
                f.write(f"**Best MLP Multi (Accuracy)**: `{best_mlp_multi_acc['name']}`\n")
                f.write(f"- Parameters: {best_mlp_multi_acc['params']}\n")
                mlp_multi_metrics = best_mlp_multi_acc['results']['multi']['MLP Multi']
                f.write(f"- Accuracy: {mlp_multi_metrics['accuracy']:.4f}\n")
                f.write(f"- F1-Score: {mlp_multi_metrics['f1_score']:.4f}\n\n")
                
                f.write(f"**Best CNN Multi (F1-Score)**: `{best_cnn_multi_f1['name']}`\n")
                f.write(f"- Parameters: {best_cnn_multi_f1['params']}\n")
                cnn_multi_metrics = best_cnn_multi_f1['results']['multi']['CNN Multi']
                f.write(f"- Accuracy: {cnn_multi_metrics['accuracy']:.4f}\n")
                f.write(f"- F1-Score: {cnn_multi_metrics['f1_score']:.4f}\n\n")
            
            # Hyperparameter Analysis
            f.write("## Hyperparameter Impact Analysis\n\n")
            f.write("### Batch Size Impact\n\n")
            f.write("Analysis of how different batch sizes affect model performance.\n\n")
            
            for bs in BATCH_SIZES:
                bs_results = [r for r in results_data if r['params']['batch_size'] == bs]
                if bs_results:
                    avg_acc = sum(r['results'].get('binary', {}).get('MLP Binary', {}).get('accuracy', 0) 
                                 for r in bs_results) / len(bs_results)
                    f.write(f"- **Batch Size {bs}**: Avg Binary Accuracy = {avg_acc:.4f} ({len(bs_results)} experiments)\n")
            
            f.write("\n### Local Epochs Impact\n\n")
            f.write("Analysis of how different local epochs affect model performance.\n\n")
            
            for epochs in LOCAL_EPOCHS:
                epoch_results = [r for r in results_data if r['params']['local_epochs'] == epochs]
                if epoch_results:
                    avg_acc = sum(r['results'].get('binary', {}).get('MLP Binary', {}).get('accuracy', 0) 
                                 for r in epoch_results) / len(epoch_results)
                    f.write(f"- **{epochs} Epoch(s)**: Avg Binary Accuracy = {avg_acc:.4f} ({len(epoch_results)} experiments)\n")
            
            f.write("\n### Learning Rate Impact\n\n")
            f.write("Analysis of how different learning rates affect model performance.\n\n")
            
            for lr in LEARNING_RATES:
                lr_results = [r for r in results_data if r['params']['learning_rate'] == lr]
                if lr_results:
                    avg_acc = sum(r['results'].get('binary', {}).get('MLP Binary', {}).get('accuracy', 0) 
                                 for r in lr_results) / len(lr_results)
                    f.write(f"- **Learning Rate {lr}**: Avg Binary Accuracy = {avg_acc:.4f} ({len(lr_results)} experiments)\n")
            
            # Recommendations
            f.write("\n## Recommendations\n\n")
            f.write("Based on the grid search results:\n\n")
            f.write("1. **Optimal Configuration for Binary Classification**:\n")
            if results_data:
                f.write(f"   - Use configuration from: `{best_cnn_bin_f1['name']}`\n")
                f.write(f"   - Parameters: {best_cnn_bin_f1['params']}\n\n")
            
            f.write("2. **Optimal Configuration for Multi-class Classification**:\n")
            if results_data:
                f.write(f"   - Use configuration from: `{best_cnn_multi_f1['name']}`\n")
                f.write(f"   - Parameters: {best_cnn_multi_f1['params']}\n\n")
            
            f.write("3. **Training Time vs Performance Trade-off**:\n")
            f.write("   - Review the duration column to balance accuracy with training time\n")
            f.write("   - Consider faster configurations if performance difference is minimal\n\n")
            
            # File Structure
            f.write("## Experiment Directory Structure\n\n")
            f.write("```\n")
            f.write("gridsearch_research/\n")
            f.write("├── all_experiments.json          # Complete experiment tracking\n")
            f.write("├── summary_report.md             # This file\n")
            for exp in self.experiments[:3]:  # Show first 3 as example
                f.write(f"├── {exp['name']}/\n")
                f.write("│   ├── experiment_log.txt        # Detailed execution log\n")
                f.write("│   ├── results_summary.json      # Metrics and results\n")
                f.write("│   ├── experiment_report.md      # Individual report\n")
                f.write("│   ├── plots/                    # Visualization plots\n")
                f.write("│   └── models/                   # Saved models\n")
            f.write("└── ...\n")
            f.write("```\n\n")
            
            f.write("## Conclusion\n\n")
            f.write(f"Grid search completed with {completed} successful experiments out of {len(self.experiments)} total.\n")
            f.write("Review individual experiment reports in each subdirectory for detailed analysis.\n\n")
            f.write("---\n")
            f.write(f"*Report generated on {datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}*\n")
        
        print(f"✅ Summary report saved to: {self.summary_file}")
        return self.summary_file


def run_experiment(batch_size, local_epochs, learning_rate, alpha, exp_dir, exp_name):
    """Run a single experiment with given hyperparameters"""
    
    # Create log file
    log_file = exp_dir / "experiment_log.txt"
    
    # Prepare environment variables
    env = os.environ.copy()
    env['GRIDSEARCH_BATCH_SIZE'] = str(batch_size)
    env['GRIDSEARCH_LOCAL_EPOCHS'] = str(local_epochs)
    env['GRIDSEARCH_LEARNING_RATE'] = str(learning_rate)
    env['GRIDSEARCH_ALPHA'] = str(alpha)
    env['GRIDSEARCH_OUTPUT_DIR'] = str(exp_dir)
    env['GRIDSEARCH_EXP_NAME'] = exp_name
    
    print(f"\n{'='*80}")
    print(f"RUNNING EXPERIMENT: {exp_name}")
    print(f"{'='*80}")
    print(f"Parameters:")
    print(f"  - Batch Size: {batch_size}")
    print(f"  - Local Epochs: {local_epochs}")
    print(f"  - Learning Rate: {learning_rate}")
    print(f"  - Alpha (Dirichlet): {alpha}")
    print(f"  - Output Directory: {exp_dir}")
    print(f"{'='*80}\n")
    
    # Run the experiment
    try:
        with open(log_file, 'w') as log:
            log.write(f"Experiment: {exp_name}\n")
            log.write(f"Start Time: {datetime.now().isoformat()}\n")
            log.write(f"Parameters: BS={batch_size}, Epochs={local_epochs}, LR={learning_rate}, Alpha={alpha}\n")
            log.write("="*80 + "\n\n")
            
            process = subprocess.Popen(
                [sys.executable, str(MAIN_SCRIPT)],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                env=env,
                text=True,
                bufsize=1
            )
            
            # Stream output to both console and log file
            for line in process.stdout:
                print(line, end='')
                log.write(line)
            
            process.wait()
            
            log.write(f"\n{'='*80}\n")
            log.write(f"End Time: {datetime.now().isoformat()}\n")
            log.write(f"Exit Code: {process.returncode}\n")
            
            if process.returncode != 0:
                raise subprocess.CalledProcessError(process.returncode, MAIN_SCRIPT)
        
        print(f"\n✅ Experiment {exp_name} completed successfully!")
        return True, None
        
    except Exception as e:
        error_msg = f"❌ Experiment {exp_name} failed: {str(e)}"
        print(f"\n{error_msg}")
        
        with open(log_file, 'a') as log:
            log.write(f"\n\nERROR: {str(e)}\n")
        
        return False, str(e)


def main():
    """Main grid search orchestration"""
    
    print("\n" + "="*80)
    print("FEDERATED LEARNING HYPERPARAMETER GRID SEARCH")
    print("="*80)
    print(f"\nConfiguration:")
    print(f"  - Batch Sizes: {BATCH_SIZES}")
    print(f"  - Local Epochs: {LOCAL_EPOCHS}")
    print(f"  - Learning Rates: {LEARNING_RATES}")
    print(f"  - Alphas (Dirichlet): {ALPHAS}")
    
    # Generate all combinations
    combinations = list(itertools.product(BATCH_SIZES, LOCAL_EPOCHS, LEARNING_RATES, ALPHAS))
    print(f"\n  - Total Experiments: {len(combinations)}")
    print(f"  - Output Directory: {BASE_DIR}")
    print("="*80 + "\n")
    
    # Confirm before starting
    response = input("Start grid search? (yes/no): ").strip().lower()
    if response not in ['yes', 'y']:
        print("Grid search cancelled.")
        return
    
    # Initialize tracker
    tracker = ExperimentTracker(BASE_DIR)
    
    # Track overall time
    overall_start = time.time()
    
    # Run all experiments
    for idx, (batch_size, local_epochs, learning_rate, alpha) in enumerate(combinations, 1):
        exp_name = tracker.create_experiment_name(batch_size, local_epochs, learning_rate, alpha)
        exp_dir = tracker.create_experiment_dir(exp_name)
        
        params = {
            'batch_size': batch_size,
            'local_epochs': local_epochs,
            'learning_rate': learning_rate,
            'alpha': alpha
        }
        
        print(f"\n{'#'*80}")
        print(f"# EXPERIMENT {idx}/{len(combinations)}")
        print(f"{'#'*80}\n")
        
        # Log start
        tracker.log_experiment_start(exp_name, params)
        
        # Run experiment
        success, error = run_experiment(batch_size, local_epochs, learning_rate, alpha, exp_dir, exp_name)
        
        # Log end
        tracker.log_experiment_end(exp_name, success, error)
        
        # Progress update
        elapsed = time.time() - overall_start
        avg_time = elapsed / idx
        remaining = avg_time * (len(combinations) - idx)
        
        print(f"\n{'='*80}")
        print(f"PROGRESS: {idx}/{len(combinations)} experiments completed")
        print(f"Elapsed: {elapsed/60:.1f} min | Estimated remaining: {remaining/60:.1f} min")
        print(f"{'='*80}\n")
    
    # Generate final summary
    total_time = time.time() - overall_start
    
    print("\n" + "="*80)
    print("GRID SEARCH COMPLETED!")
    print("="*80)
    print(f"Total time: {total_time/3600:.2f} hours ({total_time/60:.1f} minutes)")
    print(f"Experiments completed: {len(combinations)}")
    print("="*80 + "\n")
    
    # Generate summary report
    summary_file = tracker.generate_summary_report()
    
    print("\n" + "="*80)
    print(f"📊 Summary report: {summary_file}")
    print(f"📁 All results: {BASE_DIR}")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
