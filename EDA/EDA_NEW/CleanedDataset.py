import pandas as pd
import numpy as np
import time

def smart_preprocess_toniot(input_filepath, output_filepath):
    """
    Preprocessing TON_IoT dataset yang mempertimbangkan
    karakteristik protocol-specific attributes.
    """
    print("Memulai preprocessing TON_IoT dataset...")
    start_time = time.time()
    
    # Load data
    df = pd.read_csv(input_filepath)
    df.columns = df.columns.str.strip()
    print(f"[1/7] Data dimuat: {df.shape}")
    
    # Replace '-' dengan NaN
    df.replace('-', np.nan, inplace=True)
    
    # --- Protocol-Specific Handling ---
    print("[2/7] Mengidentifikasi protocol types...")
    
    # Buat protocol indicators
    df['has_dns'] = df['dns_query'].notna().astype(int)
    df['has_http'] = df['http_method'].notna().astype(int)
    df['has_ssl'] = df['ssl_version'].notna().astype(int)
    
    print(f"  - DNS traffic: {df['has_dns'].sum()} records")
    print(f"  - HTTP traffic: {df['has_http'].sum()} records")
    print(f"  - SSL traffic: {df['has_ssl'].sum()} records")
    
    # --- Convert Numeric Columns ---
    print("[3/7] Konversi tipe data numerik...")
    numeric_cols = {
        'connection': ['duration', 'src_bytes', 'dst_bytes', 'missed_bytes',
                      'src_pkts', 'src_ip_bytes', 'dst_pkts', 'dst_ip_bytes',
                      'src_port', 'dst_port'],
        'dns': ['dns_qclass', 'dns_qtype', 'dns_rcode'],
        'http': ['http_trans_depth', 'http_request_body_len', 
                'http_response_body_len', 'http_status_code']
    }
    
    all_numeric = numeric_cols['connection'] + numeric_cols['dns'] + numeric_cols['http']
    for col in all_numeric:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # --- Handle Missing Values (Context-Aware) ---
    print("[4/7] Handle missing values dengan context...")
    
    # Connection-level: isi dengan 0 (berarti tidak ada transfer)
    for col in numeric_cols['connection']:
        if col in df.columns:
            df[col].fillna(0, inplace=True)
    
    # DNS-specific: isi dengan -1 HANYA untuk DNS traffic
    for col in numeric_cols['dns']:
        if col in df.columns:
            # Untuk DNS traffic yang missing, isi dengan -1
            mask_dns = df['has_dns'] == 1
            df.loc[mask_dns, col] = df.loc[mask_dns, col].fillna(-1)
            # Non-DNS tetap NaN (akan diisi 0 nanti untuk model compatibility)
            df[col].fillna(0, inplace=True)
    
    # HTTP-specific: isi dengan -1 HANYA untuk HTTP traffic
    for col in numeric_cols['http']:
        if col in df.columns:
            mask_http = df['has_http'] == 1
            df.loc[mask_http, col] = df.loc[mask_http, col].fillna(-1)
            df[col].fillna(0, inplace=True)
    
    # --- Handle Categorical ---
    print("[5/7] Handle categorical variables...")
    categorical_cols = ['proto', 'service', 'conn_state']
    for col in categorical_cols:
        if col in df.columns:
            df[col].fillna('unknown', inplace=True)
    
    # --- Feature Engineering ---
    print("[6/7] Feature engineering...")
    
    # Ratio features
    df['bytes_ratio'] = np.where(
        df['dst_bytes'] > 0,
        df['src_bytes'] / df['dst_bytes'],
        0
    )
    
    df['pkts_ratio'] = np.where(
        df['dst_pkts'] > 0,
        df['src_pkts'] / df['dst_pkts'],
        0
    )
    
    # Rate features
    df['src_bytes_rate'] = np.where(
        df['duration'] > 0,
        df['src_bytes'] / df['duration'],
        0
    )
    
    # --- Label Encoding ---
    print("[7/7] Lewati label encoding sesuai permintaan user...")
    
    # --- Save ---
    df.to_csv(output_filepath, index=False)
    
    duration = time.time() - start_time
    print(f"\n✅ Preprocessing selesai dalam {duration:.2f} detik")
    print(f"Shape akhir: {df.shape}")
    print(f"Missing values: {df.isnull().sum().sum()}")
    print(f"File disimpan: {output_filepath}")
    
    return df

if __name__ == "__main__":
    raw_file = "/home/elnoersan/Skripsi/Paper/NotebookTODO/train_test_network.csv"
    output_file = "preprocessed_train_test_network.csv"
    
    df_clean = smart_preprocess_toniot(raw_file, output_file)
    
    # Summary statistics
    print("\n📊 Summary Statistics:")
    print(df_clean.describe())
    print("\n🏷️ Label distribution:")
    if 'label' in df_clean.columns:
        print(df_clean['label'].value_counts())