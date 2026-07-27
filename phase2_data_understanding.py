import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import argparse
import pandas as pd
import numpy as np
import json
import sys

def main():
    parser = argparse.ArgumentParser(description="Phase 2: Data Understanding")
    parser.add_argument('--input', type=str, default='/home/elnoersan/Skripsi/Paper/NotebookTODO/train_test_network.csv', help='Path to the raw CSV dataset')
    parser.add_argument('--output_dir', type=str, default='EDA', help='Directory to save EDA reports')
    args = parser.parse_args()

    input_path = args.input
    output_dir = args.output_dir

    print(f"Loading dataset from: {input_path} ...")
    try:
        df = pd.read_csv(input_path)
    except FileNotFoundError:
        print(f"Error: The file {input_path} was not found.")
        print("Please provide a valid path using --input or ensure the default path exists.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while loading the dataset: {e}")
        sys.exit(1)

    print("Dataset loaded successfully.")
    
    # Analyze
    dataset_shape = list(df.shape)
    
    column_types = {col: str(dtype) for col, dtype in df.dtypes.items()}
    
    total_features = dataset_shape[1]
    numeric_features = len(df.select_dtypes(include=[np.number]).columns)
    categorical_features = total_features - numeric_features
    
    class_distribution_multiclass = {}
    if 'type' in df.columns:
        counts = df['type'].value_counts()
        total = len(df)
        for label, count in counts.items():
            class_distribution_multiclass[str(label)] = {
                'count': int(count),
                'percentage': round((count / total) * 100, 2)
            }
            
    class_distribution_binary = {}
    if 'label' in df.columns:
        counts = df['label'].value_counts()
        total = len(df)
        for label, count in counts.items():
            class_distribution_binary[str(label)] = {
                'count': int(count),
                'percentage': round((count / total) * 100, 2)
            }
            
    missing_values = {}
    null_counts = df.isnull().sum()
    total = len(df)
    for col, count in null_counts.items():
        if count > 0:
            missing_values[col] = {
                'count': int(count),
                'percentage': round((count / total) * 100, 2)
            }
            
    duplicate_rows = int(df.duplicated().sum())
    
    high_correlation_pairs = []
    numeric_df = df.select_dtypes(include=[np.number])
    if not numeric_df.empty:
        corr_matrix = numeric_df.corr().abs()
        # Get upper triangle
        upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
        
        for i, col1 in enumerate(upper.columns):
            for col2 in upper.index:
                val = upper.loc[col2, col1]
                if not pd.isna(val) and val > 0.9:
                    high_correlation_pairs.append([col2, col1, round(float(val), 4)])
                    
    report = {
        'dataset_shape': dataset_shape,
        'total_features': total_features,
        'numeric_features': numeric_features,
        'categorical_features': categorical_features,
        'column_types': column_types,
        'class_distribution_multiclass': class_distribution_multiclass,
        'class_distribution_binary': class_distribution_binary,
        'missing_values': missing_values,
        'duplicate_rows': duplicate_rows,
        'high_correlation_pairs': high_correlation_pairs
    }
    
    os.makedirs(output_dir, exist_ok=True)
    report_path = os.path.join(output_dir, 'data_understanding_report.json')
    
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=4)
        
    print("\n--- Data Understanding Summary ---")
    print(f"Shape: {dataset_shape[0]} rows, {dataset_shape[1]} columns")
    print(f"Features: {total_features} total ({numeric_features} numeric, {categorical_features} categorical)")
    print(f"Duplicate Rows: {duplicate_rows}")
    print(f"Columns with missing values: {len(missing_values)}")
    print(f"Highly correlated feature pairs (|r| > 0.9): {len(high_correlation_pairs)}")
    print(f"Analysis saved to: {report_path}")
    print("----------------------------------\n")

if __name__ == "__main__":
    main()
