#!/usr/bin/env python3
"""
Grid Search Progress Monitor
=============================
Monitor the progress of ongoing grid search experiments
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from tabulate import tabulate

def format_duration(seconds):
    """Format duration in human-readable format"""
    if seconds is None:
        return "N/A"
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    if hours > 0:
        return f"{int(hours)}h {int(minutes)}m {int(secs)}s"
    elif minutes > 0:
        return f"{int(minutes)}m {int(secs)}s"
    else:
        return f"{int(secs)}s"

def check_progress():
    """Check and display progress of grid search"""
    
    base_dir = Path(__file__).parent
    results_file = base_dir / "all_experiments.json"
    
    if not results_file.exists():
        print("❌ No grid search in progress or not started yet.")
        print(f"Expected file: {results_file}")
        return
    
    # Load experiment data
    with open(results_file, 'r') as f:
        experiments = json.load(f)
    
    if not experiments:
        print("No experiments found.")
        return
    
    # Calculate statistics
    total = len(experiments)
    completed = sum(1 for e in experiments if e['status'] == 'completed')
    failed = sum(1 for e in experiments if e['status'] == 'failed')
    running = sum(1 for e in experiments if e['status'] == 'running')
    
    # Calculate timing
    total_time = sum(e.get('duration', 0) for e in experiments if e.get('duration'))
    completed_count = sum(1 for e in experiments if e.get('duration'))
    avg_time = total_time / completed_count if completed_count > 0 else 0
    remaining_count = total - completed - failed
    estimated_remaining = avg_time * remaining_count
    
    # Print summary
    print("\n" + "="*80)
    print("GRID SEARCH PROGRESS MONITOR")
    print("="*80)
    print(f"\n📊 Overall Progress: {completed + failed}/{total} experiments completed")
    print(f"   ✅ Completed: {completed}")
    print(f"   ❌ Failed: {failed}")
    print(f"   🔄 Running: {running}")
    print(f"   ⏳ Pending: {total - completed - failed - running}")
    
    if completed_count > 0:
        print(f"\n⏱️  Timing:")
        print(f"   Total time spent: {format_duration(total_time)}")
        print(f"   Average per experiment: {format_duration(avg_time)}")
        print(f"   Estimated remaining: {format_duration(estimated_remaining)}")
    
    # Progress bar
    progress = (completed + failed) / total
    bar_length = 50
    filled = int(bar_length * progress)
    bar = "█" * filled + "░" * (bar_length - filled)
    print(f"\n   [{bar}] {progress*100:.1f}%")
    
    # Detailed experiment list
    print("\n" + "="*80)
    print("EXPERIMENT DETAILS")
    print("="*80 + "\n")
    
    table_data = []
    for idx, exp in enumerate(experiments, 1):
        params = exp['params']
        status = exp['status']
        
        # Status icon
        if status == 'completed':
            status_icon = "✅"
        elif status == 'failed':
            status_icon = "❌"
        elif status == 'running':
            status_icon = "🔄"
        else:
            status_icon = "⏳"
        
        duration = format_duration(exp.get('duration'))
        
        table_data.append([
            idx,
            exp['name'],
            params['batch_size'],
            params['local_epochs'],
            params['learning_rate'],
            f"{status_icon} {status}",
            duration
        ])
    
    headers = ["#", "Experiment", "Batch Size", "Epochs", "LR", "Status", "Duration"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    
    # Show running experiment details
    running_exps = [e for e in experiments if e['status'] == 'running']
    if running_exps:
        print("\n" + "="*80)
        print("CURRENTLY RUNNING")
        print("="*80)
        for exp in running_exps:
            print(f"\n🔄 {exp['name']}")
            print(f"   Started: {exp['start_time']}")
            
            # Check if log file exists
            log_file = base_dir / exp['name'] / "experiment_log.txt"
            if log_file.exists():
                print(f"   Log file: {log_file}")
                print(f"   Monitor: tail -f {log_file}")
    
    # Show failed experiments
    failed_exps = [e for e in experiments if e['status'] == 'failed']
    if failed_exps:
        print("\n" + "="*80)
        print("FAILED EXPERIMENTS")
        print("="*80)
        for exp in failed_exps:
            print(f"\n❌ {exp['name']}")
            if exp.get('error'):
                print(f"   Error: {exp['error']}")
            log_file = base_dir / exp['name'] / "experiment_log.txt"
            if log_file.exists():
                print(f"   Check log: {log_file}")
    
    # Best results so far
    completed_exps = [e for e in experiments if e['status'] == 'completed']
    if completed_exps:
        print("\n" + "="*80)
        print("BEST RESULTS SO FAR")
        print("="*80)
        
        best_results = []
        for exp in completed_exps:
            results_file = base_dir / exp['name'] / 'results_summary.json'
            if results_file.exists():
                with open(results_file, 'r') as f:
                    results = json.load(f)
                    
                    # Get MLP Binary F1
                    mlp_bin_f1 = results.get('binary', {}).get('MLP Binary', {}).get('f1_score', 0)
                    cnn_bin_f1 = results.get('binary', {}).get('CNN Binary', {}).get('f1_score', 0)
                    mlp_multi_f1 = results.get('multi', {}).get('MLP Multi', {}).get('f1_score', 0)
                    cnn_multi_f1 = results.get('multi', {}).get('CNN Multi', {}).get('f1_score', 0)
                    
                    best_results.append({
                        'name': exp['name'],
                        'params': exp['params'],
                        'mlp_bin_f1': mlp_bin_f1,
                        'cnn_bin_f1': cnn_bin_f1,
                        'mlp_multi_f1': mlp_multi_f1,
                        'cnn_multi_f1': cnn_multi_f1
                    })
        
        if best_results:
            # Find best for each
            best_mlp_bin = max(best_results, key=lambda x: x['mlp_bin_f1'])
            best_cnn_bin = max(best_results, key=lambda x: x['cnn_bin_f1'])
            best_mlp_multi = max(best_results, key=lambda x: x['mlp_multi_f1'])
            best_cnn_multi = max(best_results, key=lambda x: x['cnn_multi_f1'])
            
            print(f"\n🏆 Best MLP Binary (F1={best_mlp_bin['mlp_bin_f1']:.4f})")
            print(f"   Experiment: {best_mlp_bin['name']}")
            print(f"   Params: {best_mlp_bin['params']}")
            
            print(f"\n🏆 Best CNN Binary (F1={best_cnn_bin['cnn_bin_f1']:.4f})")
            print(f"   Experiment: {best_cnn_bin['name']}")
            print(f"   Params: {best_cnn_bin['params']}")
            
            print(f"\n🏆 Best MLP Multi (F1={best_mlp_multi['mlp_multi_f1']:.4f})")
            print(f"   Experiment: {best_mlp_multi['name']}")
            print(f"   Params: {best_mlp_multi['params']}")
            
            print(f"\n🏆 Best CNN Multi (F1={best_cnn_multi['cnn_multi_f1']:.4f})")
            print(f"   Experiment: {best_cnn_multi['name']}")
            print(f"   Params: {best_cnn_multi['params']}")
    
    print("\n" + "="*80)
    print(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80 + "\n")

if __name__ == "__main__":
    try:
        check_progress()
    except KeyboardInterrupt:
        print("\n\nMonitoring stopped.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
