#!/usr/bin/env python3
"""
FEDPROX HYPERPARAMETER GRID SEARCH ORCHESTRATOR
================================================

Automated grid search untuk FedProx (Federated Proximal) experiments.
Menguji kombinasi hyperparameters: BATCH_SIZE, LOCAL_EPOCHS, LEARNING_RATE, MU, dan ALPHA.

Parameter Grid:
- BATCH_SIZE: [256]
- LOCAL_EPOCHS: [1]
- LEARNING_RATE: [0.001, 0.0005]
- MU: [0.01] (FedProx proximal term)
- ALPHA: [0.1, 0.3, 0.5] (Dirichlet Non-IID parameter)

Total combinations calculated at runtime
Setiap eksperimen melatih 4 model (MLP Binary, CNN Binary, MLP Multi, CNN Multi)

Author: AI Assistant for Federated Learning Research
Date: December 2025
"""

import os
import sys
import json
import subprocess
import time
from pathlib import Path
from datetime import datetime
import numpy as np

# ============================================================================
# KONFIGURASI GRID SEARCH - UBAH DI SINI
# ============================================================================
BATCH_SIZES = [256, 512, 1024]
LOCAL_EPOCHS = [1, 2]
LEARNING_RATES = [0.001, 0.0005]
MU_VALUES = [0.01, 0.001]  # FedProx-specific: proximal term coefficient
ALPHAS = [0.3, 5.0]  # Dirichlet distribution parameter (heterogeneity level)

# Konfigurasi eksperimen
NUM_ROUNDS = 20  # Jumlah putaran komunikasi FL
NUM_CLIENTS = 5  # Jumlah klien dalam sistem

# Directory untuk menyimpan hasil
RESULTS_DIR = Path(__file__).parent / "grid_search_results"
RESULTS_DIR.mkdir(exist_ok=True)

# File tracking
TRACKING_FILE = RESULTS_DIR / "all_experiments.json"
SUMMARY_FILE = RESULTS_DIR / "summary_report.md"
# ============================================================================

class ExperimentTracker:
    """Tracks progress dan hasil dari semua eksperimen grid search"""
    
    def __init__(self, tracking_file):
        self.tracking_file = tracking_file
        self.experiments = self.load_experiments()
    
    def load_experiments(self):
        """Load existing experiment data"""
        if self.tracking_file.exists():
            with open(self.tracking_file, 'r') as f:
                return json.load(f)
        return {
            'metadata': {
                'created_at': datetime.now().isoformat(),
                'total_experiments': 0,
                'completed': 0,
                'failed': 0,
                'in_progress': 0
            },
            'experiments': []
        }
    
    def save_experiments(self):
        """Save experiment data to JSON"""
        with open(self.tracking_file, 'w') as f:
            json.dump(self.experiments, f, indent=2)
    
    def add_experiment(self, exp_config):
        """Add new experiment configuration"""
        exp_data = {
            'config': exp_config,
            'status': 'pending',
            'started_at': None,
            'completed_at': None,
            'duration_seconds': None,
            'results': {}
        }
        self.experiments['experiments'].append(exp_data)
        self.experiments['metadata']['total_experiments'] += 1
        self.save_experiments()
        return len(self.experiments['experiments']) - 1
    
    def update_status(self, exp_index, status, results=None):
        """Update experiment status"""
        exp = self.experiments['experiments'][exp_index]
        old_status = exp['status']
        exp['status'] = status
        
        if status == 'running':
            exp['started_at'] = datetime.now().isoformat()
            self.experiments['metadata']['in_progress'] += 1
        elif status == 'completed':
            exp['completed_at'] = datetime.now().isoformat()
            if exp['started_at']:
                started = datetime.fromisoformat(exp['started_at'])
                completed = datetime.fromisoformat(exp['completed_at'])
                exp['duration_seconds'] = (completed - started).total_seconds()
            if results:
                exp['results'] = results
            self.experiments['metadata']['completed'] += 1
            if old_status == 'running':
                self.experiments['metadata']['in_progress'] -= 1
        elif status == 'failed':
            exp['completed_at'] = datetime.now().isoformat()
            self.experiments['metadata']['failed'] += 1
            if old_status == 'running':
                self.experiments['metadata']['in_progress'] -= 1
        
        self.save_experiments()
    
    def get_best_results(self):
        """Get best performing configurations"""
        completed = [e for e in self.experiments['experiments'] 
                    if e['status'] == 'completed' and e['results']]
        
        if not completed:
            return None
        
        best = {
            'mlp_binary_f1': max(completed, key=lambda x: x['results'].get('mlp_binary', {}).get('f1_score', 0)),
            'cnn_binary_f1': max(completed, key=lambda x: x['results'].get('cnn_binary', {}).get('f1_score', 0)),
            'mlp_multi_f1': max(completed, key=lambda x: x['results'].get('mlp_multi', {}).get('f1_score', 0)),
            'cnn_multi_f1': max(completed, key=lambda x: x['results'].get('cnn_multi', {}).get('f1_score', 0)),
        }
        
        return best

def create_experiment_name(batch_size, local_epochs, learning_rate, mu, alpha):
    """Generate unique experiment name"""
    lr_str = f"{learning_rate:.4f}".replace('.', 'p')
    mu_str = f"{mu:.4f}".replace('.', 'p')
    alpha_str = f"{alpha:.1f}".replace('.', 'p')
    return f"bs{batch_size}_ep{local_epochs}_lr{lr_str}_mu{mu_str}_alpha{alpha_str}"

def run_experiment(batch_size, local_epochs, learning_rate, mu, alpha, exp_index, tracker):
    """Run single grid search experiment"""
    
    exp_name = create_experiment_name(batch_size, local_epochs, learning_rate, mu, alpha)
    exp_dir = RESULTS_DIR / exp_name
    exp_dir.mkdir(exist_ok=True)
    
    print("\n" + "="*80)
    print(f"EXPERIMENT {exp_index + 1}: {exp_name}")
    print("="*80)
    print(f"Configuration:")
    print(f"  - Batch Size: {batch_size}")
    print(f"  - Local Epochs: {local_epochs}")
    print(f"  - Learning Rate: {learning_rate}")
    print(f"  - Mu (Proximal Term): {mu}")
    print(f"  - Alpha (Dirichlet): {alpha}")
    print(f"  - Output Directory: {exp_dir}")
    print(f"  - Expected Duration: 20-30 minutes")
    print("="*80)
    
    # Update tracker
    tracker.update_status(exp_index, 'running')
    
    # Prepare environment variables
    env = os.environ.copy()
    env['GRIDSEARCH_BATCH_SIZE'] = str(batch_size)
    env['GRIDSEARCH_LOCAL_EPOCHS'] = str(local_epochs)
    env['GRIDSEARCH_LEARNING_RATE'] = str(learning_rate)
    env['GRIDSEARCH_MU'] = str(mu)  # FedProx-specific parameter
    env['GRIDSEARCH_ALPHA'] = str(alpha)  # Dirichlet parameter
    env['GRIDSEARCH_OUTPUT_DIR'] = str(exp_dir)
    env['GRIDSEARCH_EXP_NAME'] = exp_name
    
    # CRITICAL: Set PYTHONPATH for Ray workers (learned from FedAvg)
    parent_dir = str(Path(__file__).parent.parent)
    if 'PYTHONPATH' in env:
        env['PYTHONPATH'] = f"{parent_dir}{os.pathsep}{env['PYTHONPATH']}"
    else:
        env['PYTHONPATH'] = parent_dir
    
    # Run experiment script
    script_path = Path(__file__).parent / "research_hypertuning_gridsearch.py"
    log_file = exp_dir / "experiment_log.txt"
    
    start_time = time.time()
    
    try:
        with open(log_file, 'w') as f:
            result = subprocess.run(
                [sys.executable, str(script_path)],
                env=env,
                stdout=f,
                stderr=subprocess.STDOUT,
                check=True
            )
        
        duration = time.time() - start_time
        
        # Load results (check for results_summary.json which is what we actually generate)
        results_file = exp_dir / "results_summary.json"
        if results_file.exists():
            with open(results_file, 'r') as f:
                results_data = json.load(f)
            
            # Extract metrics from the nested structure
            results = {}
            for model_name, metrics in results_data.get('binary', {}).items():
                key = model_name.lower().replace(' ', '_')
                results[key] = metrics
            for model_name, metrics in results_data.get('multi', {}).items():
                key = model_name.lower().replace(' ', '_')
                results[key] = metrics
            
            tracker.update_status(exp_index, 'completed', results)
            
            print(f"\n✅ EXPERIMENT COMPLETED in {duration:.2f}s ({duration/60:.2f} min)")
            print(f"Results saved to: {exp_dir}")
            print(f"\nQuick Summary:")
            for model_type in ['mlp_binary', 'cnn_binary', 'mlp_multi', 'cnn_multi']:
                if model_type in results:
                    f1 = results[model_type].get('f1_score', 0)
                    acc = results[model_type].get('accuracy', 0)
                    print(f"  - {model_type}: F1={f1:.4f}, Acc={acc:.4f}")
        else:
            print(f"\n⚠️ EXPERIMENT COMPLETED but results_summary.json not found")
            tracker.update_status(exp_index, 'completed', {})
        
        return True
        
    except subprocess.CalledProcessError as e:
        duration = time.time() - start_time
        print(f"\n❌ EXPERIMENT FAILED after {duration:.2f}s")
        print(f"Error details in: {log_file}")
        tracker.update_status(exp_index, 'failed')
        return False
    except Exception as e:
        duration = time.time() - start_time
        print(f"\n❌ EXPERIMENT ERROR after {duration:.2f}s: {e}")
        tracker.update_status(exp_index, 'failed')
        return False

def generate_summary_report(tracker):
    """Generate comprehensive markdown summary report"""
    
    experiments = tracker.experiments['experiments']
    metadata = tracker.experiments['metadata']
    
    completed = [e for e in experiments if e['status'] == 'completed']
    failed = [e for e in experiments if e['status'] == 'failed']
    
    report = []
    report.append("# FEDPROX GRID SEARCH - COMPREHENSIVE RESULTS REPORT")
    report.append(f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("\n" + "="*80)
    
    # Overall Statistics
    report.append("\n## 1. EXPERIMENT STATISTICS")
    report.append(f"\n- **Total Experiments**: {metadata['total_experiments']}")
    report.append(f"- **Completed**: {metadata['completed']} ✅")
    report.append(f"- **Failed**: {metadata['failed']} ❌")
    report.append(f"- **Success Rate**: {metadata['completed']/metadata['total_experiments']*100:.1f}%")
    
    if completed:
        avg_duration = np.mean([e['duration_seconds'] for e in completed if e['duration_seconds']])
        total_duration = sum([e['duration_seconds'] for e in completed if e['duration_seconds']])
        report.append(f"- **Average Duration**: {avg_duration:.2f}s ({avg_duration/60:.2f} min)")
        report.append(f"- **Total Training Time**: {total_duration:.2f}s ({total_duration/3600:.2f} hours)")
    
    # Parameter Grid
    report.append("\n## 2. HYPERPARAMETER GRID")
    report.append(f"\n- **Batch Sizes**: {BATCH_SIZES}")
    report.append(f"- **Local Epochs**: {LOCAL_EPOCHS}")
    report.append(f"- **Learning Rates**: {LEARNING_RATES}")
    report.append(f"- **Mu Values (Proximal Term)**: {MU_VALUES}")
    report.append(f"- **Alphas (Dirichlet)**: {ALPHAS}")
    report.append(f"- **Total Combinations**: {len(BATCH_SIZES)} × {len(LOCAL_EPOCHS)} × {len(LEARNING_RATES)} × {len(MU_VALUES)} × {len(ALPHAS)} = {metadata['total_experiments']}")
    
    # Best Results per Model
    if completed:
        report.append("\n## 3. BEST PERFORMING CONFIGURATIONS")
        
        for model_type in ['mlp_binary', 'cnn_binary', 'mlp_multi', 'cnn_multi']:
            valid_results = [e for e in completed if model_type in e['results']]
            if valid_results:
                best = max(valid_results, key=lambda x: x['results'][model_type].get('f1_score', 0))
                config = best['config']
                results = best['results'][model_type]
                
                report.append(f"\n### {model_type.upper().replace('_', ' ')}")
                report.append(f"- **Configuration**: BS={config['batch_size']}, Epochs={config['local_epochs']}, LR={config['learning_rate']}, Mu={config['mu']}")
                report.append(f"- **F1-Score**: {results.get('f1_score', 0):.4f}")
                report.append(f"- **Accuracy**: {results.get('accuracy', 0):.4f}")
                report.append(f"- **Precision**: {results.get('precision', 0):.4f}")
                report.append(f"- **Recall**: {results.get('recall', 0):.4f}")
                if 'auc_roc' in results:
                    report.append(f"- **AUC-ROC**: {results.get('auc_roc', 0):.4f}")
        
        # Mu Analysis
        report.append("\n## 4. MU (PROXIMAL TERM) ANALYSIS")
        report.append("\nEffect of mu parameter on model performance:")
        
        for mu_val in MU_VALUES:
            mu_experiments = [e for e in completed if e['config']['mu'] == mu_val]
            if mu_experiments:
                avg_f1_binary = np.mean([e['results'].get('mlp_binary', {}).get('f1_score', 0) for e in mu_experiments if 'mlp_binary' in e['results']])
                avg_f1_multi = np.mean([e['results'].get('mlp_multi', {}).get('f1_score', 0) for e in mu_experiments if 'mlp_multi' in e['results']])
                report.append(f"\n### Mu = {mu_val}")
                report.append(f"- **Average Binary F1**: {avg_f1_binary:.4f}")
                report.append(f"- **Average Multi F1**: {avg_f1_multi:.4f}")
                report.append(f"- **Experiments with this mu**: {len(mu_experiments)}")
        
        # Alpha Analysis
        report.append("\n## 4b. ALPHA (DIRICHLET) ANALYSIS")
        for alpha_val in ALPHAS:
            alpha_experiments = [e for e in completed if e['config']['alpha'] == alpha_val]
            if alpha_experiments:
                avg_f1_binary = np.mean([e['results'].get('mlp_binary', {}).get('f1_score', 0) for e in alpha_experiments if 'mlp_binary' in e['results']])
                avg_f1_multi = np.mean([e['results'].get('mlp_multi', {}).get('f1_score', 0) for e in alpha_experiments if 'mlp_multi' in e['results']])
                report.append(f"\n### Alpha = {alpha_val}")
                report.append(f"- **Average Binary F1**: {avg_f1_binary:.4f}")
                report.append(f"- **Average Multi F1**: {avg_f1_multi:.4f}")
                report.append(f"- **Experiments with this alpha**: {len(alpha_experiments)}")
        
        # Batch Size Analysis
        report.append("\n## 5. BATCH SIZE ANALYSIS")
        for bs in BATCH_SIZES:
            bs_experiments = [e for e in completed if e['config']['batch_size'] == bs]
            if bs_experiments:
                avg_f1 = np.mean([e['results'].get('mlp_binary', {}).get('f1_score', 0) for e in bs_experiments if 'mlp_binary' in e['results']])
                report.append(f"\n- **Batch Size {bs}**: Avg Binary F1 = {avg_f1:.4f} ({len(bs_experiments)} experiments)")
        
        # Learning Rate Analysis
        report.append("\n## 6. LEARNING RATE ANALYSIS")
        for lr in LEARNING_RATES:
            lr_experiments = [e for e in completed if e['config']['learning_rate'] == lr]
            if lr_experiments:
                avg_f1 = np.mean([e['results'].get('mlp_binary', {}).get('f1_score', 0) for e in lr_experiments if 'mlp_binary' in e['results']])
                report.append(f"\n- **Learning Rate {lr}**: Avg Binary F1 = {avg_f1:.4f} ({len(lr_experiments)} experiments)")
    
    # Failed Experiments
    if failed:
        report.append("\n## 7. FAILED EXPERIMENTS")
        for e in failed:
            config = e['config']
            report.append(f"\n- BS={config['batch_size']}, Epochs={config['local_epochs']}, LR={config['learning_rate']}, Mu={config['mu']}")
    
    # Recommendations
    if completed:
        report.append("\n## 8. RECOMMENDATIONS")
        
        # Find overall best configuration (weighted average across all models)
        best_overall = max(completed, key=lambda e: np.mean([
            e['results'].get('mlp_binary', {}).get('f1_score', 0),
            e['results'].get('cnn_binary', {}).get('f1_score', 0),
            e['results'].get('mlp_multi', {}).get('f1_score', 0),
            e['results'].get('cnn_multi', {}).get('f1_score', 0)
        ]))
        
        config = best_overall['config']
        report.append(f"\n**Best Overall Configuration (Highest Average F1 across all models):**")
        report.append(f"- Batch Size: {config['batch_size']}")
        report.append(f"- Local Epochs: {config['local_epochs']}")
        report.append(f"- Learning Rate: {config['learning_rate']}")
        report.append(f"- Mu (Proximal Term): {config['mu']}")
        report.append(f"- Alpha (Dirichlet): {config['alpha']}")
        
        avg_f1 = np.mean([
            best_overall['results'].get('mlp_binary', {}).get('f1_score', 0),
            best_overall['results'].get('cnn_binary', {}).get('f1_score', 0),
            best_overall['results'].get('mlp_multi', {}).get('f1_score', 0),
            best_overall['results'].get('cnn_multi', {}).get('f1_score', 0)
        ])
        report.append(f"- Average F1-Score: {avg_f1:.4f}")
    
    report.append("\n" + "="*80)
    report.append("\n## END OF REPORT")
    
    # Write report
    with open(SUMMARY_FILE, 'w') as f:
        f.write('\n'.join(report))
    
    print(f"\n📊 Summary report generated: {SUMMARY_FILE}")

def main():
    """Main grid search execution"""
    
    print("="*80)
    print("FEDPROX HYPERPARAMETER GRID SEARCH")
    print("="*80)
    print(f"\nParameter Grid:")
    print(f"  - Batch Sizes: {BATCH_SIZES}")
    print(f"  - Local Epochs: {LOCAL_EPOCHS}")
    print(f"  - Learning Rates: {LEARNING_RATES}")
    print(f"  - Mu (Proximal Term): {MU_VALUES}")
    print(f"  - Alphas (Dirichlet): {ALPHAS}")
    print(f"\nTotal Experiments: {len(BATCH_SIZES) * len(LOCAL_EPOCHS) * len(LEARNING_RATES) * len(MU_VALUES) * len(ALPHAS)}")
    print(f"Models per Experiment: 4 (MLP Binary, CNN Binary, MLP Multi, CNN Multi)")
    print(f"Total Models to Train: {len(BATCH_SIZES) * len(LOCAL_EPOCHS) * len(LEARNING_RATES) * len(MU_VALUES) * len(ALPHAS) * 4}")
    print(f"\nEstimated Time: Varies based on configuration")
    print(f"Results Directory: {RESULTS_DIR}")
    print("="*80)
    
    # Initialize tracker
    tracker = ExperimentTracker(TRACKING_FILE)
    
    # Generate all experiment configurations
    experiments_to_run = []
    for batch_size in BATCH_SIZES:
        for local_epochs in LOCAL_EPOCHS:
            for learning_rate in LEARNING_RATES:
                for mu in MU_VALUES:
                    for alpha in ALPHAS:
                        config = {
                            'batch_size': batch_size,
                            'local_epochs': local_epochs,
                            'learning_rate': learning_rate,
                            'mu': mu,
                            'alpha': alpha
                        }
                    
                    # Check if already exists
                    existing = [i for i, e in enumerate(tracker.experiments['experiments'])
                              if e['config'] == config]
                    
                    if existing:
                        exp_index = existing[0]
                        exp = tracker.experiments['experiments'][exp_index]
                        status = exp['status']
                        if status == 'completed':
                            print(f"\n⏭️  Skipping already completed: {create_experiment_name(config['batch_size'], config['local_epochs'], config['learning_rate'], config['mu'], config['alpha'])}")
                            continue
                        if status == 'running':
                            print(f"\n⚠️  Found experiment marked as running: {create_experiment_name(config['batch_size'], config['local_epochs'], config['learning_rate'], config['mu'], config['alpha'])}")
                            print(f"   Resetting to pending...")
                            tracker.update_status(exp_index, 'pending')
                    else:
                        exp_index = tracker.add_experiment(config)
                    
                    experiments_to_run.append((config, exp_index))
    
    print(f"\n📋 Experiments to run: {len(experiments_to_run)}")
    
    if not experiments_to_run:
        print("\n✅ All experiments already completed!")
        generate_summary_report(tracker)
        return
    
    # Confirm before starting
    print("\nPress ENTER to start grid search, or Ctrl+C to cancel...")
    try:
        input()
    except KeyboardInterrupt:
        print("\n\n❌ Grid search cancelled by user")
        return
    
    # Run experiments
    start_time = time.time()
    successful = 0
    failed_count = 0
    
    for i, (config, exp_index) in enumerate(experiments_to_run):
        print(f"\n\n{'='*80}")
        print(f"PROGRESS: {i+1}/{len(experiments_to_run)} experiments")
        print(f"Time elapsed: {(time.time() - start_time)/3600:.2f} hours")
        print(f"{'='*80}")
        
        success = run_experiment(
            config['batch_size'],
            config['local_epochs'],
            config['learning_rate'],
            config['mu'],
            config['alpha'],
            exp_index,
            tracker
        )
        
        if success:
            successful += 1
        else:
            failed_count += 1
            print(f"\n⚠️  Failed experiments so far: {failed_count}")
    
    total_time = time.time() - start_time
    
    # Final summary
    print("\n\n" + "="*80)
    print("GRID SEARCH COMPLETED!")
    print("="*80)
    print(f"\nTotal Time: {total_time:.2f}s ({total_time/3600:.2f} hours)")
    print(f"Successful: {successful}")
    print(f"Failed: {failed_count}")
    print(f"Success Rate: {successful/(successful+failed_count)*100:.1f}%")
    
    # Generate final report
    generate_summary_report(tracker)
    
    print("\n✅ Grid search completed successfully!")
    print(f"📁 Results saved in: {RESULTS_DIR}")
    print(f"📊 Summary report: {SUMMARY_FILE}")
    print(f"📋 Detailed tracking: {TRACKING_FILE}")
    print("\nUse check_progress.py to view detailed results anytime.")

if __name__ == "__main__":
    main()
