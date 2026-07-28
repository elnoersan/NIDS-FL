import json
import os
import argparse
from datetime import datetime

def load_json(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Warning: Could not read {filepath}: {e}")
        return None

def format_table(headers, rows):
    header_row = "| " + " | ".join(headers) + " |"
    separator_row = "| " + " | ".join(["---"] * len(headers)) + " |"
    table = [header_row, separator_row]
    for row in rows:
        table.append("| " + " | ".join(str(cell) for cell in row) + " |")
    return "\n".join(table)

def generate_report(eda_path, benchmark_path, output_path):
    eda_data = load_json(eda_path)
    benchmark_data = load_json(benchmark_path)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # ---------------------------------------------------------
    # Helper to extract data understanding info
    # ---------------------------------------------------------
    def get_eda_section():
        if not eda_data:
            return "[EDA data not found or failed to load.]\n"
        
        shape = eda_data.get("shape", "N/A")
        
        multiclass_dist = eda_data.get("class_distribution", {}).get("Label", {})
        binary_dist = eda_data.get("class_distribution", {}).get("binary_label", {})
        
        missing = eda_data.get("missing_values_summary", {})
        duplicates = eda_data.get("duplicate_rows", 0)
        
        high_corr = eda_data.get("high_correlation_pairs", [])
        
        section = f"- **Dataset shape**: {shape}\n"
        section += f"- **Duplicate count**: {duplicates}\n\n"
        
        section += "### Class Distribution (Multiclass)\n"
        mc_headers = ["Class", "Count"]
        mc_rows = [[k, v] for k, v in multiclass_dist.items()]
        section += format_table(mc_headers, mc_rows) + "\n\n"
        
        section += "### Class Distribution (Binary)\n"
        bin_headers = ["Class", "Count"]
        bin_rows = [[k, v] for k, v in binary_dist.items()]
        section += format_table(bin_headers, bin_rows) + "\n\n"
        
        section += "### Missing Value Summary\n"
        if missing:
            section += "- Missing values are present in specific features.\n"
        else:
            section += "- No significant missing values found.\n"
            
        section += "\n### High Correlation Pairs\n"
        if high_corr:
            hc_headers = ["Feature 1", "Feature 2", "Correlation"]
            hc_rows = [[item[0], item[1], f"{item[2]:.4f}"] for item in high_corr]
            section += format_table(hc_headers, hc_rows) + "\n"
        else:
            section += "- No extremely high correlation features detected.\n"
            
        return section

    # ---------------------------------------------------------
    # Helper to extract benchmark info
    # ---------------------------------------------------------
    def get_benchmark_modeling_section():
        section = "### Federated Learning Configuration\n"
        fl_rows = [
            ["Clients", "5 (Residential, Transportation, Healthcare, Industrial, Government)"],
            ["Communication Rounds", "20 (or 3 in Quick Mode)"],
            ["Local Epochs", "1"],
            ["Batch Size", "512"],
            ["Learning Rate", "0.0005"],
            ["Optimizer", "Adam"],
            ["Loss Function", "Binary/Sparse Categorical Crossentropy"]
        ]
        section += format_table(["Parameter", "Value"], fl_rows) + "\n\n"
        
        section += "### Model Architectures\n"
        section += "- **MLP**: Multi-Layer Perceptron is utilized as the baseline.\n"
        section += "- **CNN-1D**: A 1D Convolutional Neural Network is utilized to extract sequential patterns from the network data.\n\n"
        
        section += "### Non-IID Simulation\n"
        section += "- **Method**: Dirichlet Distribution (α=0.3 for extreme Non-IID, α=5.0 for IID-like distribution).\n"
        
        return section

    def get_benchmark_evaluation_section():
        if not benchmark_data or not isinstance(benchmark_data, list):
            return "[Benchmark data not found or invalid format.]\n"
            
        section = ""
        
        # Grouping strategy
        grouped_results = {}
        for res in benchmark_data:
            task = res.get("Task", "unknown")
            alpha = res.get("Alpha", "unknown")
            key = f"Task: {task} | Alpha: {alpha}"
            if key not in grouped_results:
                grouped_results[key] = []
            grouped_results[key].append(res)
            
        for group_name, group_data in grouped_results.items():
            section += f"### {group_name}\n"
            headers = ["Model", "Strategy", "Accuracy", "Precision", "Recall", "F1", "AUC", "WS", "Time (s)"]
            rows = []
            for item in group_data:
                model = item.get("Model", "N/A")
                strategy = item.get("Strategy", "N/A")
                acc = f"{item.get('Acc', 0.0):.4f}"
                prec = f"{item.get('Prec', 0.0):.4f}"
                rec = f"{item.get('Rec', 0.0):.4f}"
                f1 = f"{item.get('F1', 0.0):.4f}"
                auc = f"{item.get('AUC', 0.0):.4f}"
                ws = f"{item.get('WS', 0.0):.4f}"
                time_val = f"{item.get('Duration_s', 0.0):.2f}"
                
                rows.append([model, strategy, acc, prec, rec, f1, auc, ws, time_val])
                
            section += format_table(headers, rows) + "\n\n"
            
        section += "### FedAvg vs FedProx Analysis\n"
        section += "- FedProx generally provides better stability under extreme Non-IID distributions (small alpha).\n"
        section += "- FedAvg can converge faster but sometimes experiences oscillations on highly imbalanced data.\n\n"
        
        section += "### Best Model Identification\n"
        section += "- Based on the F1-Score and AUC metrics, choose the combination of model and FL algorithm that provides the optimal trade-off between accuracy and stability.\n"
        
        return section

    # ---------------------------------------------------------
    # Assemble the Markdown Report
    # ---------------------------------------------------------
    report = f"""# Experiment Report: Detection and Classification of Smart City Network Attacks Using Federated Learning

**Date**: {timestamp}
**Researcher**: Rian Nur Ikhsan (22523297)
**Institution**: Universitas Islam Indonesia

---

## Phase 1: Business Understanding
This research aims to address the challenges in detecting anomalies and attacks across distributed Smart City networks. The implementation of *Federated Learning* (FL) is motivated by the critical need to preserve data privacy among entities (privacy preservation) while building robust and collaborative Intrusion Detection System (NIDS) models without centralizing raw data.

## Phase 2: Data Understanding
{get_eda_section()}

## Phase 3: Data Preparation
In this phase, data preprocessing was conducted to ensure the input quality for the FL models:
- **Protocol-aware cleaning**: Handling anomalies related to specific network protocols.
- **Categorical encoding**: Using Label Encoding for class labels and OneHot Encoding for other categorical features.
- **Variance thresholding**: Eliminating constant features or those with extremely low variance to reduce noise.
- **StandardScaler normalization**: Normalizing numerical features to reside on the same scale.
- **Stratified split**: Partitioning the dataset into 80% training data and 20% testing data proportionally.
- **No SMOTE decision**: Decided against using SMOTE to preserve the original distribution of attack data within the FL simulation.
- **Final feature count**: (Adjusted based on preprocessing output).

## Phase 4: Modeling
{get_benchmark_modeling_section()}

## Phase 5: Evaluation
{get_benchmark_evaluation_section()}

## Conclusion
The experiments demonstrate that implementing *Federated Learning* (both FedAvg and FedProx) is capable of building reasonably stable intrusion detection models using Non-IID distributed data. The CNN-1D and MLP models exhibit distinct characteristics in terms of training time and performance metrics, where hyperparameter tuning and the choice of FL methodology (FedAvg vs FedProx) play pivotal roles in balancing data privacy and attack detection efficiency in Smart City environments.
"""

    try:
        with open(output_path, 'w') as f:
            f.write(report)
        print(f"Report successfully generated at {output_path}")
    except Exception as e:
        print(f"Error writing report: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate CRISP-DM Phase 5 Report")
    parser.add_argument("--output", type=str, default="THESIS_EXPERIMENT_REPORT.md", help="Output path for the report")
    args = parser.parse_args()
    
    # Paths based on project structure
    base_dir = os.path.dirname(os.path.abspath(__file__))
    eda_path = os.path.join(base_dir, "EDA", "data_understanding_report.json")
    benchmark_path = os.path.join(base_dir, "thesis_benchmark_results_pytorch.json")
    
    output_path = os.path.join(base_dir, args.output) if not os.path.isabs(args.output) else args.output
    
    generate_report(eda_path, benchmark_path, output_path)
