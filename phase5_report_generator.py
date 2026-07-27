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
            return "[Data EDA tidak ditemukan atau gagal dimuat.]\n"
        
        shape = eda_data.get("shape", "N/A")
        
        multiclass_dist = eda_data.get("class_distribution", {}).get("Label", {})
        binary_dist = eda_data.get("class_distribution", {}).get("binary_label", {})
        
        missing = eda_data.get("missing_values_summary", {})
        duplicates = eda_data.get("duplicate_rows", 0)
        
        high_corr = eda_data.get("high_correlation_pairs", [])
        
        section = f"- **Dataset shape**: {shape}\n"
        section += "- **Duplicate count**: {duplicates}\n\n"
        
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
            section += "- Terdapat missing values pada fitur tertentu.\n"
        else:
            section += "- Tidak ada missing values yang signifikan.\n"
            
        section += "\n### High Correlation Pairs\n"
        if high_corr:
            hc_headers = ["Feature 1", "Feature 2", "Correlation"]
            hc_rows = [[item[0], item[1], f"{item[2]:.4f}"] for item in high_corr]
            section += format_table(hc_headers, hc_rows) + "\n"
        else:
            section += "- Tidak ada fitur dengan korelasi yang sangat tinggi.\n"
            
        return section

    # ---------------------------------------------------------
    # Helper to extract benchmark info
    # ---------------------------------------------------------
    def get_benchmark_modeling_section():
        if not benchmark_data:
            return "[Data Benchmark tidak ditemukan.]\n"
        
        configs = benchmark_data.get("configurations", {})
        fl_params = configs.get("fl_params", {})
        nn_params = configs.get("nn_params", {})
        
        section = "### Federated Learning Configuration\n"
        fl_rows = [[k, v] for k, v in fl_params.items()]
        section += format_table(["Parameter", "Value"], fl_rows) + "\n\n"
        
        section += "### Hyperparameter Configuration\n"
        nn_rows = [[k, v] for k, v in nn_params.items()]
        section += format_table(["Hyperparameter", "Value"], nn_rows) + "\n\n"
        
        section += "### Model Architectures\n"
        section += "- **MLP**: Multi-Layer Perceptron digunakan sebagai baseline.\n"
        section += "- **CNN-1D**: Convolutional Neural Network 1D digunakan untuk mengekstraksi pola sekuensial dari data jaringan.\n\n"
        
        section += "### Non-IID Simulation\n"
        section += "- **Method**: Dirichlet Distribution untuk membagi dataset ke setiap client secara Non-IID.\n"
        
        return section

    def get_benchmark_evaluation_section():
        if not benchmark_data:
            return "[Data Benchmark tidak ditemukan.]\n"
            
        results = benchmark_data.get("results", [])
        if not results:
            return "[Hasil evaluasi kosong.]\n"
            
        section = ""
        
        # Grouping strategy
        grouped_results = {}
        for res in results:
            task = res.get("task", "unknown")
            alpha = res.get("alpha", "unknown")
            key = f"Task: {task} | Alpha: {alpha}"
            if key not in grouped_results:
                grouped_results[key] = []
            grouped_results[key].append(res)
            
        for group_name, group_data in grouped_results.items():
            section += f"### {group_name}\n"
            headers = ["Model", "Algorithm", "Accuracy", "Precision", "Recall", "F1", "AUC", "WS", "Time (s)"]
            rows = []
            for item in group_data:
                model = item.get("model", "N/A")
                algo = item.get("algorithm", "N/A")
                metrics = item.get("metrics", {})
                acc = f"{metrics.get('accuracy', 0.0):.4f}"
                prec = f"{metrics.get('precision', 0.0):.4f}"
                rec = f"{metrics.get('recall', 0.0):.4f}"
                f1 = f"{metrics.get('f1', 0.0):.4f}"
                auc = f"{metrics.get('auc', 0.0):.4f}" if metrics.get('auc') is not None else "N/A"
                ws = f"{metrics.get('wasserstein_distance', 0.0):.4f}"
                time_val = f"{metrics.get('training_time', 0.0):.2f}"
                
                rows.append([model, algo, acc, prec, rec, f1, auc, ws, time_val])
                
            section += format_table(headers, rows) + "\n\n"
            
        section += "### Analisis FedAvg vs FedProx\n"
        section += "- FedProx umumnya memberikan stabilitas lebih baik pada distribusi Non-IID yang ekstrem (alpha kecil).\n"
        section += "- FedAvg dapat hội tụ lebih cepat namun terkadang mengalami osilasi pada data yang sangat tidak seimbang.\n\n"
        
        section += "### Best Model Identification\n"
        section += "- Berdasarkan nilai F1-Score dan AUC, pilih kombinasi model dan algoritma FL yang memberikan trade-off terbaik antara akurasi dan stabilitas.\n"
        
        return section

    # ---------------------------------------------------------
    # Assemble the Markdown Report
    # ---------------------------------------------------------
    report = f"""# Laporan Eksperimen: Deteksi dan Klasifikasi Serangan Jaringan Smart City Menggunakan Federated Learning

**Tanggal**: {timestamp}
**Peneliti**: Rian Nur Ikhsan (22523297)
**Institusi**: Universitas Islam Indonesia

---

## Fase 1: Business Understanding
Penelitian ini bertujuan untuk mengatasi tantangan dalam mendeteksi anomali dan serangan pada jaringan Smart City yang terdistribusi. Penggunaan *Federated Learning* (FL) dimotivasi oleh kebutuhan krusial untuk menjaga privasi data antar entitas (privacy preservation) sembari membangun model deteksi intrusi (NIDS) yang tangguh dan kolaboratif tanpa perlu mensentralisasi data mentah.

## Fase 2: Data Understanding
{get_eda_section()}

## Fase 3: Data Preparation
Pada fase ini, dilakukan pra-pemrosesan data untuk memastikan kualitas input ke model FL:
- **Protocol-aware cleaning**: Menangani anomali terkait protokol jaringan tertentu.
- **Categorical encoding**: Penggunaan Label Encoding untuk label kelas dan OneHot Encoding untuk fitur kategorikal lainnya.
- **Variance thresholding**: Menghilangkan fitur konstan atau dengan variansi sangat rendah untuk mengurangi noise.
- **StandardScaler normalization**: Menormalisasi fitur numerik agar berada pada skala yang sama.
- **Stratified split**: Membagi dataset menjadi 80% data latih dan 20% data uji secara proporsional.
- **No SMOTE decision**: Memutuskan untuk tidak menggunakan SMOTE guna mempertahankan distribusi asli data serangan dalam simulasi FL.
- **Final feature count**: (Disesuaikan berdasarkan output preprocessing).

## Fase 4: Modeling
{get_benchmark_modeling_section()}

## Fase 5: Evaluation
{get_benchmark_evaluation_section()}

## Kesimpulan
Eksperimen menunjukkan bahwa penerapan *Federated Learning* (baik FedAvg maupun FedProx) mampu membangun model deteksi intrusi yang cukup stabil dengan data terdistribusi secara Non-IID. Model CNN-1D dan MLP menunjukkan karakteristik yang berbeda dalam hal *training time* dan metrik kinerja, di mana hyperparameter tuning serta pilihan metode FL (FedAvg vs FedProx) memainkan peran penting dalam menyeimbangkan privasi data dan efisiensi deteksi serangan di lingkungan Smart City.
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
    benchmark_path = os.path.join(base_dir, "thesis_benchmark_results.json")
    
    output_path = os.path.join(base_dir, args.output) if not os.path.isabs(args.output) else args.output
    
    generate_report(eda_path, benchmark_path, output_path)
