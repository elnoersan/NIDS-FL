#!/usr/bin/env python3
"""
FEDPROX GRID SEARCH PROGRESS MONITOR
====================================

Real-time monitoring tool untuk melacak progress dari FedProx grid search experiments.
Menampilkan status, metrics, dan analisis sementara dari eksperimen yang sedang berjalan.

Usage:
    python check_progress.py

Author: AI Assistant for Federated Learning Research
Date: December 2025
"""

import json
import sys
from pathlib import Path
from datetime import datetime
import numpy as np

# Directory tracking
RESULTS_DIR = Path(__file__).parent / "grid_search_results"
TRACKING_FILE = RESULTS_DIR / "all_experiments.json"

def format_duration(seconds):
    """Format duration in human-readable format"""
    if seconds is None:
        return "N/A"
    
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    
    if hours > 0:
        return f"{hours}h {minutes}m {secs}s"
    elif minutes > 0:
        return f"{minutes}m {secs}s"
    else:
        return f"{secs}s"

def load_experiments():
    """Load experiment tracking data"""
    if not TRACKING_FILE.exists():
        print(f"❌ Tracking file not found: {TRACKING_FILE}")
        print("   No experiments have been started yet.")
        return None
    
    with open(TRACKING_FILE, 'r') as f:
        return json.load(f)

def print_overall_stats(data):
    """Print overall statistics"""
    metadata = data['metadata']
    
    print("\n" + "="*80)
    print("FEDPROX GRID SEARCH - OVERALL STATISTICS")
    print("="*80)
    
    print(f"\nCreated: {metadata['created_at']}")
    print(f"\nTotal Experiments: {metadata['total_experiments']}")
    print(f"  ✅ Completed: {metadata['completed']}")
    print(f"  🔄 In Progress: {metadata['in_progress']}")
    print(f"  ❌ Failed: {metadata['failed']}")
    print(f"  ⏳ Pending: {metadata['total_experiments'] - metadata['completed'] - metadata['failed'] - metadata['in_progress']}")
    
    if metadata['total_experiments'] > 0:
        completion_pct = (metadata['completed'] / metadata['total_experiments']) * 100
        print(f"\nCompletion: {completion_pct:.1f}%")
        
        # Progress bar
        bar_length = 50
        filled = int(bar_length * metadata['completed'] / metadata['total_experiments'])
        bar = '█' * filled + '░' * (bar_length - filled)
        print(f"[{bar}] {metadata['completed']}/{metadata['total_experiments']}")

def print_experiment_details(data):
    """Print detailed experiment information"""
    experiments = data['experiments']
    
    if not experiments:
        print("\nNo experiments found.")
        return
    
    print("\n" + "="*80)
    print("EXPERIMENT DETAILS")
    print("="*80)
    
    # Group by status
    completed = [e for e in experiments if e['status'] == 'completed']
    running = [e for e in experiments if e['status'] == 'running']
    failed = [e for e in experiments if e['status'] == 'failed']
    pending = [e for e in experiments if e['status'] == 'pending']
    
    # Running experiments
    if running:
        print("\n🔄 CURRENTLY RUNNING:")
        for exp in running:
            config = exp['config']
            print(f"\n  BS={config['batch_size']}, Epochs={config['local_epochs']}, "
                  f"LR={config['learning_rate']}, Mu={config['mu']}")
            if exp['started_at']:
                started = datetime.fromisoformat(exp['started_at'])
                elapsed = (datetime.now() - started).total_seconds()
                print(f"  Started: {started.strftime('%H:%M:%S')}, Elapsed: {format_duration(elapsed)}")
    
    # Completed experiments
    if completed:
        print(f"\n✅ COMPLETED ({len(completed)} experiments):")
        
        # Calculate average duration
        durations = [e['duration_seconds'] for e in completed if e['duration_seconds']]
        if durations:
            avg_duration = np.mean(durations)
            total_duration = sum(durations)
            print(f"\n  Average Duration: {format_duration(avg_duration)}")
            print(f"  Total Training Time: {format_duration(total_duration)}")
            
            # Estimate remaining time
            pending_count = len(pending) + len(failed)  # Assume failed will be retried
            if pending_count > 0:
                estimated_remaining = avg_duration * pending_count
                print(f"  Estimated Remaining: {format_duration(estimated_remaining)}")
        
        # Show recent completions
        recent = sorted(completed, key=lambda x: x['completed_at'] if x['completed_at'] else '', reverse=True)[:3]
        print(f"\n  Recent Completions:")
        for exp in recent:
            config = exp['config']
            results = exp.get('results', {})
            print(f"\n  • BS={config['batch_size']}, Epochs={config['local_epochs']}, "
                  f"LR={config['learning_rate']}, Mu={config['mu']}")
            print(f"    Duration: {format_duration(exp['duration_seconds'])}")
            
            # Show metrics if available
            if results:
                for model_type in ['mlp_binary', 'cnn_binary', 'mlp_multi', 'cnn_multi']:
                    if model_type in results:
                        f1 = results[model_type].get('f1_score', 0)
                        acc = results[model_type].get('accuracy', 0)
                        print(f"    {model_type}: F1={f1:.4f}, Acc={acc:.4f}")
    
    # Failed experiments
    if failed:
        print(f"\n❌ FAILED ({len(failed)} experiments):")
        for exp in failed:
            config = exp['config']
            print(f"  • BS={config['batch_size']}, Epochs={config['local_epochs']}, "
                  f"LR={config['learning_rate']}, Mu={config['mu']}")
    
    # Pending experiments
    if pending:
        print(f"\n⏳ PENDING ({len(pending)} experiments)")
        # Show first few
        for exp in pending[:3]:
            config = exp['config']
            print(f"  • BS={config['batch_size']}, Epochs={config['local_epochs']}, "
                  f"LR={config['learning_rate']}, Mu={config['mu']}")
        if len(pending) > 3:
            print(f"  ... and {len(pending) - 3} more")

def print_best_results(data):
    """Print best performing configurations so far"""
    completed = [e for e in data['experiments'] 
                if e['status'] == 'completed' and e.get('results')]
    
    if not completed:
        print("\nNo completed experiments with results yet.")
        return
    
    print("\n" + "="*80)
    print("BEST RESULTS SO FAR")
    print("="*80)
    
    # Best for each model type
    model_types = ['mlp_binary', 'cnn_binary', 'mlp_multi', 'cnn_multi']
    
    for model_type in model_types:
        valid_experiments = [e for e in completed if model_type in e['results']]
        
        if not valid_experiments:
            continue
        
        best = max(valid_experiments, key=lambda x: x['results'][model_type].get('f1_score', 0))
        config = best['config']
        results = best['results'][model_type]
        
        print(f"\n{model_type.upper().replace('_', ' ')}:")
        print(f"  Configuration: BS={config['batch_size']}, Epochs={config['local_epochs']}, "
              f"LR={config['learning_rate']}, Mu={config['mu']}")
        print(f"  F1-Score: {results.get('f1_score', 0):.4f}")
        print(f"  Accuracy: {results.get('accuracy', 0):.4f}")
        print(f"  Precision: {results.get('precision', 0):.4f}")
        print(f"  Recall: {results.get('recall', 0):.4f}")
        if 'auc_roc' in results:
            print(f"  AUC-ROC: {results.get('auc_roc', 0):.4f}")

def analyze_mu_impact(data):
    """Analyze the impact of mu parameter on performance"""
    completed = [e for e in data['experiments'] 
                if e['status'] == 'completed' and e.get('results')]
    
    if len(completed) < 3:
        return
    
    print("\n" + "="*80)
    print("MU PARAMETER ANALYSIS (FedProx-Specific)")
    print("="*80)
    
    # Group by mu value
    mu_values = sorted(set([e['config']['mu'] for e in completed]))
    
    print(f"\nMu values tested: {mu_values}")
    print("\nImpact on performance:")
    
    for mu in mu_values:
        mu_experiments = [e for e in completed if e['config']['mu'] == mu]
        
        if not mu_experiments:
            continue
        
        # Calculate average metrics
        binary_f1s = [e['results'].get('mlp_binary', {}).get('f1_score', 0) 
                     for e in mu_experiments if 'mlp_binary' in e['results']]
        multi_f1s = [e['results'].get('mlp_multi', {}).get('f1_score', 0) 
                    for e in mu_experiments if 'mlp_multi' in e['results']]
        
        print(f"\n  Mu = {mu}:")
        if binary_f1s:
            print(f"    Binary F1 (avg): {np.mean(binary_f1s):.4f} (±{np.std(binary_f1s):.4f})")
        if multi_f1s:
            print(f"    Multi F1 (avg): {np.mean(multi_f1s):.4f} (±{np.std(multi_f1s):.4f})")
        print(f"    Experiments: {len(mu_experiments)}")
    
    # Recommendation
    if binary_f1s:
        best_mu_binary = max(mu_values, key=lambda mu: np.mean([
            e['results'].get('mlp_binary', {}).get('f1_score', 0)
            for e in completed if e['config']['mu'] == mu and 'mlp_binary' in e['results']
        ]))
        print(f"\n  💡 Best mu for Binary: {best_mu_binary}")
    
    if multi_f1s:
        best_mu_multi = max(mu_values, key=lambda mu: np.mean([
            e['results'].get('mlp_multi', {}).get('f1_score', 0)
            for e in completed if e['config']['mu'] == mu and 'mlp_multi' in e['results']
        ]))
        print(f"  💡 Best mu for Multi-class: {best_mu_multi}")

def main():
    """Main monitoring function"""
    print("="*80)
    print("FEDPROX GRID SEARCH PROGRESS MONITOR")
    print("="*80)
    print(f"\nTracking file: {TRACKING_FILE}")
    
    # Load data
    data = load_experiments()
    
    if data is None:
        return
    
    # Display information
    print_overall_stats(data)
    print_experiment_details(data)
    print_best_results(data)
    analyze_mu_impact(data)
    
    print("\n" + "="*80)
    print("END OF PROGRESS REPORT")
    print("="*80)
    print("\nTip: Run this script anytime to check progress!")
    print("     For detailed results, see summary_report.md after completion.")

if __name__ == "__main__":
    main()
