# %% [markdown]
# # Federated Proximal (FedProx) - Non-IID Research Notebook
# 
# ## 1. Library Imports & Configuration
# 
# **Eksperimen:** Network Intrusion Detection menggunakan FedProx pada TON_IoT Dataset  
# 
# **Distribusi Data:** Non-IID (Dirichlet) dengan Natural Class Imbalance  ---
# 
# **Framework:** Flower 1.24.0 + TensorFlow 2.20.0

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
import os
import gc
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report, accuracy_score, f1_score, 
    precision_score, recall_score, confusion_matrix
 )

import tensorflow as tf
import keras
from keras import backend as K

# Flower imports
import flwr as fl
from flwr.simulation import start_simulation
from flwr.server.strategy import FedProx

# Local imports - import directly from current directory
from task import get_model_by_type, ProximalModel
from utils import (
    split_data_non_iid_label,
    evaluate_model_metrics,
    prepare_client_configs,
    print_summary_table
)
import pickle
from tabulate import tabulate
from IPython.display import display, HTML
import warnings

# Set random seeds
np.random.seed(42)
tf.random.set_seed(42)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['PYTHONHASHSEED'] = '42'

# ============================================================================
# KONFIGURASI EKSPERIMEN - UBAH DI SINI
# ============================================================================
NUM_ROUNDS = 10            # Jumlah putaran komunikasi federated learning
NUM_CLIENTS = 5         # Jumlah klien dalam sistem
LOCAL_EPOCHS = 1           # Jumlah epoch pelatihan lokal per klien per round
BATCH_SIZE_BINARY = 512 # Ukuran batch untuk model binary (optimized)
BATCH_SIZE_MULTI = 512    # Ukuran batch untuk model multi-class (optimized)
LEARNING_RATE = 0.001       # Learning rate untuk optimizer
MU_BINARY = 0.01            # FedProx proximal term coefficient untuk binary
MU_MULTI = 0.01           # FedProx proximal term coefficient untuk multi-class (reduced 10x)
ALPHA_BINARY = 0.3         # Parameter alpha Dirichlet untuk data binary (Non-IID)
ALPHA_MULTI = 0.3         # Parameter alpha Dirichlet untuk data multi-class (Non-IID)
FRAMEWORK = "Flower (flwr)" # Framework yang digunakan
ALGORITHM = "Federated Proximal (FedProx)"  # Algoritma federated learning
DATA_DISTRIBUTION = "Non-IID (Dirichlet) - Natural Imbalance"   # Jenis distribusi data
# ============================================================================

print("=== FEDERATED PROXIMAL (FEDPROX) DENGAN FLOWER ===")
print(f"Konfigurasi: {NUM_CLIENTS} Klien, {NUM_ROUNDS} Putaran, {LOCAL_EPOCHS} Local Epochs")
print(f"Proximal Term (mu) - Binary: {MU_BINARY}, Multi-class: {MU_MULTI}")
print(f"Data Distribution: {DATA_DISTRIBUTION}")
print(f"NO SMOTE - Natural class distribution preserved for Non-IID learning")
print("Semua library berhasil diimpor.")
print(f"TensorFlow version: {tf.__version__}")
print(f"Flower version: {fl.__version__}")

# %% [markdown]
# ## 2. Data Loading (Deprecated - Commented Out)
# 
# > Lihat Section 3 untuk loading preprocessed data.
# 
# > **Note:** Raw data loading sudah tidak digunakan.  > Data sudah di-preprocess secara terpisah menggunakan GPU-optimized pipeline.  

# %%
# print("--- Memuat Dataset ---")
# try:
#     df = pd.read_csv(
#         "/home/elnoersan/Skripsi/Paper/NotebookTODO/train_test_network.csv"
#     )
#     print(f"Dataset berhasil dimuat. Shape: {df.shape}")
# except FileNotFoundError:
#     print("File dataset tidak ditemukan. Pastikan path benar.")
#     raise

# %% [markdown]
# ## 3. Data Preparation - Load Preprocessed Data
# 
# **GPU-Optimized Preprocessing Pipeline (External)**
# 
# **Preprocessing dilakukan sekali di luar notebook** menggunakan:  
# `/home/elnoersan/Skripsi/Paper/NotebookTODO/EDA/preprocessing_pipeline.py`
# 
# **Pipeline Steps:**
# 1. Smart Preprocessing (Protocol-aware missing value handling)
# 2. Train/Test Split (80/20 stratified)
# 3. OneHot Encoding (fit on train only)
# 4. Feature Selection (VarianceThreshold - GPU friendly)
# 5. Standardization (StandardScaler)
# 
# **Benefits:**
# -  **5-10 menit → <5 detik** loading time
# -  **No data leakage** (all transformers fit only on training data)
# -  **Reproducible** (same preprocessing across all experiments)
# -  **No SMOTE** (preserves natural Non-IID distribution)
# 
# - Multi-class: 35 features (VarianceThreshold selected)
# 
# **Output:**- Binary: 30 features (VarianceThreshold selected)

# %%
# # def smart_preprocess_toniot_inplace(df):
# #     """
# #     Preprocessing TON_IoT dataset yang mempertimbangkan
# #     karakteristik protocol-specific attributes.
# #     Tidak menyimpan ke file, return langsung.
# #     """
# #     print("="*70)
# #     print("SMART PREPROCESSING TON_IOT DATASET")
# #     print("="*70)
    
# #     # Copy untuk avoid modifying original
# #     df_clean = df.copy()
# #     df_clean.columns = df_clean.columns.str.strip()
    
# #     # Replace '-' dengan NaN
# #     df_clean.replace('-', np.nan, inplace=True)
# #     print(f"[1/6] Data loaded: {df_clean.shape}")
    
# #     # --- Protocol-Specific Handling ---
# #     print("[2/6] Identifying protocol types...")
    
# #     # Protocol indicators (binary flags)
# #     df_clean['has_dns'] = df_clean['dns_query'].notna().astype(int) if 'dns_query' in df_clean.columns else 0
# #     df_clean['has_http'] = df_clean['http_method'].notna().astype(int) if 'http_method' in df_clean.columns else 0
# #     df_clean['has_ssl'] = df_clean['ssl_version'].notna().astype(int) if 'ssl_version' in df_clean.columns else 0
    
# #     if 'dns_query' in df_clean.columns:
# #         print(f"  - DNS traffic: {df_clean['has_dns'].sum():,} records")
# #     if 'http_method' in df_clean.columns:
# #         print(f"  - HTTP traffic: {df_clean['has_http'].sum():,} records")
# #     if 'ssl_version' in df_clean.columns:
# #         print(f"  - SSL traffic: {df_clean['has_ssl'].sum():,} records")
    
# #     # --- Convert Numeric Columns ---
# #     print("[3/6] Converting numeric columns...")
# #     numeric_cols = {
# #         'connection': ['duration', 'src_bytes', 'dst_bytes', 'missed_bytes',
# #                       'src_pkts', 'src_ip_bytes', 'dst_pkts', 'dst_ip_bytes'],
# #         'dns': ['dns_qclass', 'dns_qtype', 'dns_rcode'],
# #         'http': ['http_trans_depth', 'http_request_body_len', 
# #                 'http_response_body_len', 'http_status_code']
# #     }
    
# #     all_numeric = numeric_cols['connection'] + numeric_cols['dns'] + numeric_cols['http']
# #     for col in all_numeric:
# #         if col in df_clean.columns:
# #             df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
    
# #     # --- Handle Missing Values (Context-Aware) ---
# #     print("[4/6] Handling missing values (context-aware)...")
    
# #     # Connection-level: fill with 0 (no transfer)
# #     for col in numeric_cols['connection']:
# #         if col in df_clean.columns:
# #             df_clean[col] = df_clean[col].fillna(0)
    
# #     # DNS-specific: fill with -1 for DNS traffic, 0 for non-DNS
# #     for col in numeric_cols['dns']:
# #         if col in df_clean.columns:
# #             mask_dns = df_clean['has_dns'] == 1
# #             df_clean.loc[mask_dns, col] = df_clean.loc[mask_dns, col].fillna(-1)
# #             df_clean[col] = df_clean[col].fillna(0)
    
# #     # HTTP-specific: fill with -1 for HTTP traffic, 0 for non-HTTP
# #     for col in numeric_cols['http']:
# #         if col in df_clean.columns:
# #             mask_http = df_clean['has_http'] == 1
# #             df_clean.loc[mask_http, col] = df_clean.loc[mask_http, col].fillna(-1)
# #             df_clean[col] = df_clean[col].fillna(0)
    
# #     # --- Handle Categorical ---
# #     print("[5/6] Handling categorical variables...")
# #     categorical_cols = ['proto', 'service', 'conn_state']
# #     for col in categorical_cols:
# #         if col in df_clean.columns:
# #             df_clean[col] = df_clean[col].fillna('unknown')
    
# #     # --- Feature Engineering ---
# #     print("[6/6] Feature engineering...")
    
# #     # Ratio features (avoid division by zero)
# #     if 'src_bytes' in df_clean.columns and 'dst_bytes' in df_clean.columns:
# #         df_clean['bytes_ratio'] = np.where(
# #             df_clean['dst_bytes'] > 0,
# #             df_clean['src_bytes'] / df_clean['dst_bytes'],
# #             0
# #         )
    
# #     if 'src_pkts' in df_clean.columns and 'dst_pkts' in df_clean.columns:
# #         df_clean['pkts_ratio'] = np.where(
# #             df_clean['dst_pkts'] > 0,
# #             df_clean['src_pkts'] / df_clean['dst_pkts'],
# #             0
# #         )
    
# #     # Rate features
# #     if 'src_bytes' in df_clean.columns and 'duration' in df_clean.columns:
# #         df_clean['src_bytes_rate'] = np.where(
# #             df_clean['duration'] > 0,
# #             df_clean['src_bytes'] / df_clean['duration'],
# #             0
# #         )
    
# #     if 'dst_bytes' in df_clean.columns and 'duration' in df_clean.columns:
# #         df_clean['dst_bytes_rate'] = np.where(
# #             df_clean['duration'] > 0,
# #             df_clean['dst_bytes'] / df_clean['duration'],
# #             0
# #         )
    
# #     print(f"\nPreprocessing completed!")
# #     print(f"  - Shape: {df_clean.shape}")
# #     print(f"  - Missing values: {df_clean.isnull().sum().sum()}")
# #     print(f"  - New features added: bytes_ratio, pkts_ratio, src_bytes_rate, dst_bytes_rate")
# #     print(f"  - Protocol indicators: has_dns, has_http, has_ssl")
# #     print("="*70)
    
# #     return df_clean

# # Apply smart preprocessing
# print("\n--- SMART PREPROCESSING ---")
# # df_preprocessed = smart_preprocess_toniot_inplace(df)
# df_preprocessed = df

# print("\n" + "="*70)
# print("PREPARASI DATA UNTUK DETEKSI BINER")
# print("="*70)
# df_binary = df_preprocessed.drop(columns=['src_ip','src_port','dst_ip','dst_port','type', 'weird_name','weird_addl','weird_notice'], errors='ignore')
# X_binary = df_binary.drop('label', axis=1)
# y_binary = df_binary['label']

# # CORRECT PIPELINE: Split FIRST, then encode (prevents data leakage)
# print("\n[Step 1] Split data train/test SEBELUM encoding...")
# X_train_bin, X_test_bin, y_train_bin, y_test_bin = train_test_split(
#     X_binary, y_binary, test_size=0.2, random_state=42, stratify=y_binary
# )
# print(f"  - Train: {X_train_bin.shape}")
# print(f"  - Test: {X_test_bin.shape}")

# # Identify categorical columns
# categorical_cols = X_train_bin.select_dtypes(include=['object']).columns.tolist()
# numeric_cols = X_train_bin.select_dtypes(exclude=['object']).columns.tolist()
# print(f"\n[Step 2] Encoding {len(categorical_cols)} categorical columns with OneHotEncoder...")
# print(f"  Categorical: {categorical_cols}")
# print(f"  Numeric (passthrough): {len(numeric_cols)} columns")

# # Debug: Check for unseen categories
# print(f"\n  DEBUG - Checking for unseen categories in test set:")
# for col in categorical_cols:
#     train_unique = set(X_train_bin[col].unique())
#     test_unique = set(X_test_bin[col].unique())
#     unseen = test_unique - train_unique
#     if unseen:
#         print(f"    - {col}: Unseen in test: {unseen} ({len(unseen)} values)")
#     else:
#         print(f"    - {col}: No unseen categories ✓")

# # OneHotEncoder with ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.compose import ColumnTransformer

# if categorical_cols:
#     # Create preprocessor with OneHotEncoder
#     preprocessor_binary = ColumnTransformer(
#         transformers=[
#             ('cat', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'), categorical_cols)
#         ],
#         remainder='passthrough'  # Keep numeric columns as-is
#     )
    
#     # Fit on training data only
#     X_train_bin_encoded = preprocessor_binary.fit_transform(X_train_bin)
#     X_test_bin_encoded = preprocessor_binary.transform(X_test_bin)
    
#     print(f"\n✓ OneHotEncoding completed without data leakage")
#     print(f"  - Encoder fit ONLY on training data")
#     print(f"  - Test data transformed using training encoder")
#     print(f"  - Unseen categories handled gracefully (ignored)")
#     print(f"  - Train shape after encoding: {X_train_bin_encoded.shape}")
#     print(f"  - Test shape after encoding: {X_test_bin_encoded.shape}")
# else:
#     X_train_bin_encoded = X_train_bin.values
#     X_test_bin_encoded = X_test_bin.values
#     preprocessor_binary = None
#     print(f"\n✓ No categorical columns, using numeric data directly")

# print("\n[Step 3] Feature selection HANYA pada data training...")
# n_features_bin = min(30, X_train_bin_encoded.shape[1])
# rfe = RFE(
#     estimator=RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=42), 
#     n_features_to_select=n_features_bin
# )
# X_train_bin_selected = rfe.fit_transform(X_train_bin_encoded, y_train_bin)
# X_test_bin_selected = rfe.transform(X_test_bin_encoded)

# print(f"  - Selected features: {n_features_bin}/{X_train_bin_encoded.shape[1]}")

# print("\n[Step 4] Scale data - fit pada train, transform pada test...")
# scaler_binary = StandardScaler()
# X_train_bin_scaled = scaler_binary.fit_transform(X_train_bin_selected)
# X_test_bin_scaled = scaler_binary.transform(X_test_bin_selected)

# print(f"\n✓ Data biner siap (NO DATA LEAKAGE):")
# print(f"  - Train: {X_train_bin_scaled.shape}")
# print(f"  - Test: {X_test_bin_scaled.shape}")
# print(f"  - All preprocessing fit ONLY on training data")
# print("="*70)

# gc.collect()

# print("\n" + "="*70)
# print("PREPARASI DATA UNTUK KLASIFIKASI MULTI-KELAS")
# print("="*70)
# df_multi = df_preprocessed.drop(columns=['src_ip','src_port','dst_ip','dst_port', 'label', 'weird_name','weird_addl','weird_notice'], errors='ignore')
# y_multi = df_multi['type']
# X_multi = df_multi.drop('type', axis=1)

# # Encode target BEFORE split (safe - just label mapping)
# le_target = LabelEncoder()
# y_multi_encoded = le_target.fit_transform(y_multi)
# num_classes = len(le_target.classes_)
# print(f"Jumlah kelas: {num_classes}")
# print(f"Nama kelas: {list(le_target.classes_)}")

# # CORRECT PIPELINE FOR NON-IID FL: Split FIRST, then encode features
# print("\n[Step 1] Split data train/test SEBELUM encoding features...")
# X_train_multi, X_test_multi, y_train_multi, y_test_multi = train_test_split(
#     X_multi, y_multi_encoded, test_size=0.2, random_state=42, stratify=y_multi_encoded
# )
# print(f"  - Train: {X_train_multi.shape}")
# print(f"  - Test: {X_test_multi.shape}")

# # Display class distribution (natural imbalance)
# print("\n✓ Distribusi kelas ASLI (Training Data - Natural Imbalance):")
# unique, counts = np.unique(y_train_multi, return_counts=True)
# class_dist = dict(zip(unique, counts))
# for class_idx, count in sorted(class_dist.items()):
#     class_name = le_target.classes_[class_idx]
#     pct = (count / len(y_train_multi)) * 100
#     print(f"   - {class_name}: {count:,} sampel ({pct:.2f}%)")
# print(f"   TOTAL: {len(y_train_multi):,} sampel")

# print("\n⚠ CATATAN: SMOTE TIDAK DIGUNAKAN untuk Federated Learning Non-IID")
# print("Alasan:")
# print("  1. SMOTE menghilangkan heterogenitas data (tujuan Non-IID)")
# print("  2. FedProx dirancang untuk data imbalanced natural")
# print("  3. Real-world: MITM jarang, model belajar dari distribusi asli")
# print("  4. Proximal term (mu) menangani heterogenitas tanpa sintetis")

# # Identify categorical columns
# categorical_cols_multi = X_train_multi.select_dtypes(include=['object']).columns.tolist()
# numeric_cols_multi = X_train_multi.select_dtypes(exclude=['object']).columns.tolist()
# print(f"\n[Step 2] Encoding {len(categorical_cols_multi)} categorical columns with OneHotEncoder...")
# print(f"  Categorical: {categorical_cols_multi}")
# print(f"  Numeric (passthrough): {len(numeric_cols_multi)} columns")

# # Debug: Check for unseen categories
# print(f"\n  DEBUG - Checking for unseen categories in test set:")
# for col in categorical_cols_multi:
#     train_unique = set(X_train_multi[col].unique())
#     test_unique = set(X_test_multi[col].unique())
#     unseen = test_unique - train_unique
#     if unseen:
#         print(f"    - {col}: Unseen in test: {unseen} ({len(unseen)} values)")
#     else:
#         print(f"    - {col}: No unseen categories ✓")

# # OneHotEncoder with ColumnTransformer
# if categorical_cols_multi:
#     # Create preprocessor with OneHotEncoder
#     preprocessor_multi = ColumnTransformer(
#         transformers=[
#             ('cat', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'), categorical_cols_multi)
#         ],
#         remainder='passthrough'  # Keep numeric columns as-is
#     )
    
#     # Fit on training data only
#     X_train_multi_encoded = preprocessor_multi.fit_transform(X_train_multi)
#     X_test_multi_encoded = preprocessor_multi.transform(X_test_multi)
    
#     print(f"\n✓ OneHotEncoding completed without data leakage")
#     print(f"  - Encoder fit ONLY on training data")
#     print(f"  - Test data transformed using training encoder")
#     print(f"  - Unseen categories handled gracefully (ignored)")
#     print(f"  - Train shape after encoding: {X_train_multi_encoded.shape}")
#     print(f"  - Test shape after encoding: {X_test_multi_encoded.shape}")
# else:
#     X_train_multi_encoded = X_train_multi.values
#     X_test_multi_encoded = X_test_multi.values
#     preprocessor_multi = None
#     print(f"\n✓ No categorical columns, using numeric data directly")

# print("\n[Step 3] Feature selection HANYA pada data training...")
# n_features_multi = min(35, X_train_multi_encoded.shape[1])
# rfe_multi = RFE(
#     estimator=RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=42), 
#     n_features_to_select=n_features_multi
# )
# X_train_multi_scaled_features = rfe_multi.fit_transform(X_train_multi_encoded, y_train_multi)
# X_test_multi_scaled_features = rfe_multi.transform(X_test_multi_encoded)

# print(f"  - Selected features: {n_features_multi}/{X_train_multi_encoded.shape[1]}")

# print("\n[Step 4] Scale data - fit pada train, transform pada test...")
# scaler_multi = StandardScaler()
# X_train_multi_scaled = scaler_multi.fit_transform(X_train_multi_scaled_features)
# X_test_multi_scaled = scaler_multi.transform(X_test_multi_scaled_features)

# print(f"\n✓ Data multi-kelas siap (NO DATA LEAKAGE):")
# print(f"  - Train: {X_train_multi_scaled.shape} (natural distribution)")
# print(f"  - Test: {X_test_multi_scaled.shape}")
# print(f"  - All preprocessing fit ONLY on training data")
# print("="*70)

# # Save preprocessors for production use (ONLY trained on training data)
# preprocessors = {
#     'binary': {
#         'preprocessor': preprocessor_binary,
#         'rfe': rfe,
#         'scaler': scaler_binary,
#         'categorical_columns': categorical_cols,
#         'numeric_columns': numeric_cols
#     },
#     'multi': {
#         'preprocessor': preprocessor_multi,
#         'target_encoder': le_target,
#         'rfe': rfe_multi,
#         'scaler': scaler_multi,
#         'categorical_columns': categorical_cols_multi,
#         'numeric_columns': numeric_cols_multi,
#         'num_classes': num_classes
#     }
# }

# with open('preprocessors.pkl', 'wb') as f:
#     pickle.dump(preprocessors, f)
# print("\n✓ Preprocessors saved to 'preprocessors.pkl'")
# print("  - All preprocessors fit ONLY on training data (no leakage)")
# print("  - OneHotEncoder handles unseen categories with 'ignore'")
# print("  - Ready for production use with unseen data handling")

# gc.collect()

# NOPE WE FOUND FAST METHOD JUST LOAD THE PICKLE using existing /home/elnoersan/Skripsi/Paper/NotebookTODO/EDA/processed_artifacts/binary_preprocessed.pkl
#/home/elnoersan/Skripsi/Paper/NotebookTODO/EDA/processed_artifacts/multiclass_preprocessed.pkl

#Let this comment exitsed i dont trust git commit

# %%
print("="*70)
print("LOAD PREPROCESSED DATA (GPU-OPTIMIZED)")
print("="*70)

# Load binary classification data
print("\n[1/2] Loading binary classification data...")
with open('/home/elnoersan/Skripsi/Paper/NotebookTODO/EDA/processed_artifacts/binary_preprocessed.pkl', 'rb') as f:
    binary_data = pickle.load(f)

X_train_bin_scaled = binary_data['X_train']
X_test_bin_scaled = binary_data['X_test']
y_train_bin = binary_data['y_train']
y_test_bin = binary_data['y_test']

print(f"✓ Binary data loaded:")
print(f"  - Train: {X_train_bin_scaled.shape}")
print(f"  - Test: {X_test_bin_scaled.shape}")
print(f"  - Features: {binary_data.get('metadata', {}).get('n_features_final', 'N/A')}")

# Load multi-class classification data
print("\n[2/2] Loading multi-class classification data...")
with open('/home/elnoersan/Skripsi/Paper/NotebookTODO/EDA/processed_artifacts/multiclass_preprocessed.pkl', 'rb') as f:
    multi_data = pickle.load(f)

X_train_multi_scaled = multi_data['X_train']
X_test_multi_scaled = multi_data['X_test']
y_train_multi = multi_data['y_train']
y_test_multi = multi_data['y_test']
num_classes = multi_data['num_classes']
class_names = multi_data['class_names']  # ✅ Load from pickle!
le_target = multi_data['target_encoder']  # ✅ Load LabelEncoder from pickle!

print(f"✓ Multi-class data loaded:")
print(f"  - Train: {X_train_multi_scaled.shape}")
print(f"  - Test: {X_test_multi_scaled.shape}")
print(f"  - Classes: {num_classes}")
print(f"  - Class names: {class_names}")
print(f"  - Features: {multi_data.get('metadata', {}).get('n_features_final', 'N/A')}")

print("\n" + "="*70)
print("DATA READY FOR TRAINING!")
print("="*70)
print("✓ No data leakage (preprocessed separately)")
print("✓ Train/test split done before encoding")
print("✓ All transformers fit only on training data")
print(f"✓ Time saved: ~5-10 minutes → <5 seconds")
print("="*70)

gc.collect()


# %% [markdown]
# ## BAGIAN 4: SPLIT DATA KE KLIEN (NON-IID)
# 
# Bagian ini akan:
# 1. Mendistribusikan data training ke klien dengan pola Non-IID
# 2. Menampilkan statistik distribusi per klien
# 3. Memvisualisasikan heterogenitas data

# %%
print("="*70)
print("DISTRIBUSI DATA KE KLIEN - NON-IID")
print("="*70)

# Split data untuk klien menggunakan konfigurasi alpha yang sudah didefinisikan
print("\n[1/2] Splitting Binary data dengan Dirichlet distribution...")
print(f"      Alpha = {ALPHA_BINARY} (lower = more heterogeneous)")
client_data_binary = split_data_non_iid_label(
    X_train_bin_scaled, 
    y_train_bin, 
    n_clients=NUM_CLIENTS, 
    alpha=ALPHA_BINARY
)

print("\n[2/2] Splitting Multi-class data dengan Dirichlet distribution...")
print(f"      Alpha = {ALPHA_MULTI} (lower = more heterogeneous)")
client_data_multi = split_data_non_iid_label(
    X_train_multi_scaled, 
    y_train_multi, 
    n_clients=NUM_CLIENTS, 
    alpha=ALPHA_MULTI
)

print("\n" + "="*70)
print("SUMMARY - DATA SPLIT COMPLETED")
print("="*70)
print(f"Binary Test Set: {X_test_bin_scaled.shape}")
print(f"Multi-class Test Set: {X_test_multi_scaled.shape}")
print(f"\nTraining data dengan NATURAL DISTRIBUTION telah didistribusikan")
print(f"  - Jumlah Klien: {NUM_CLIENTS}")
print(f"  - Distribution: Non-IID (Dirichlet)")
print(f"  - NO SMOTE: Natural heterogeneity preserved")
print(f"  - FedProx akan menangani data imbalance secara natural")
print("="*70)

# %% [markdown]
# ### 4.2 DISTRIBUSI BINARY DATA PER KLIE

# %%
print("\n" + "="*70)
print("DISTRIBUSI BINARY DATA PER KLIEN")
print("="*70)

binary_dist_data = []
total_samples = 0

for i, (X_client, y_client) in enumerate(client_data_binary):
    n_samples = len(X_client)
    n_normal = np.sum(y_client == 0)
    n_attack = np.sum(y_client == 1)
    pct_normal = (n_normal / n_samples) * 100
    pct_attack = (n_attack / n_samples) * 100
    
    binary_dist_data.append([
        f"Client {i+1}",
        f"{n_samples:,}",
        f"{n_normal:,}",
        f"{pct_normal:.1f}%",
        f"{n_attack:,}",
        f"{pct_attack:.1f}%"
    ])
    total_samples += n_samples

# Add total row
binary_dist_data.append([
    "TOTAL",
    f"{total_samples:,}",
    f"{np.sum([np.sum(y == 0) for _, y in client_data_binary]):,}",
    "-",
    f"{np.sum([np.sum(y == 1) for _, y in client_data_binary]):,}",
    "-"
])

headers = ["Client", "Total Samples", "Normal", "Normal %", "Attack", "Attack %"]
print("\n" + tabulate(binary_dist_data, headers=headers, tablefmt="grid"))

# Calculate heterogeneity metric
print("\nHETEROGENEITY METRICS:")
attack_ratios = [(np.sum(y == 1) / len(y)) for _, y in client_data_binary]
print(f"  - Attack ratio range: {min(attack_ratios):.3f} - {max(attack_ratios):.3f}")
print(f"  - Attack ratio std dev: {np.std(attack_ratios):.3f}")
print(f"  - Higher std dev = more heterogeneous (good for Non-IID)")
print("="*70)

# %% [markdown]
# ### 4.3 DISTRIBUSI MULTI-CLASS DATA PER KLIE

# %%
print("="*70)
print("DISTRIBUSI MULTI-CLASS DATA PER KLIEN")
print("="*70)

# Get class names
class_names = le_target.classes_

# Build distribution table
multi_dist_data = []
for i, (X_client, y_client) in enumerate(client_data_multi):
    row = [f"Client {i+1}", f"{len(X_client):,}"]
    
    for class_idx in range(num_classes):
        count = np.sum(y_client == class_idx)
        row.append(f"{count:,}")
    
    multi_dist_data.append(row)

# Add total row
total_row = ["TOTAL", f"{sum([len(X) for X, _ in client_data_multi]):,}"]
for class_idx in range(num_classes):
    total_count = sum([np.sum(y == class_idx) for _, y in client_data_multi])
    total_row.append(f"{total_count:,}")
multi_dist_data.append(total_row)

headers = ["Client", "Total"] + [name for name in class_names]
print("\n" + tabulate(multi_dist_data, headers=headers, tablefmt="grid"))

# Calculate per-class distribution across clients
print("\nCLASS DISTRIBUTION ANALYSIS:")
for class_idx, class_name in enumerate(class_names):
    counts_per_client = [np.sum(y == class_idx) for _, y in client_data_multi]
    print(f"\n  {class_name}:")
    print(f"    - Total: {sum(counts_per_client):,} samples")
    print(f"    - Per client: {counts_per_client}")
    print(f"    - Std dev: {np.std(counts_per_client):.1f} (higher = more heterogeneous)")

print("="*70)

# %% [markdown]
# ## BAGIAN 5: DEFINISI FUNGSI UNTUK FLOWER CLIENT DENGAN FEDPROX

# %%
class FlowerClientProx(fl.client.NumPyClient):
    """Flower client untuk federated learning dengan FedProx."""
    
    def __init__(self, client_id, X_train, y_train, X_test, y_test, 
                 model_type, input_shape, num_classes, config):
        self.client_id = client_id
        self.X_train = X_train.astype(np.float32)
        self.y_train = y_train
        self.X_test = X_test.astype(np.float32) if X_test is not None else None
        self.y_test = y_test
        self.model_type = model_type
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.config = config
        
        # Untuk CNN, reshape input
        if 'cnn' in model_type:
            self.X_train = self.X_train.reshape(-1, input_shape, 1)
            if self.X_test is not None:
                self.X_test = self.X_test.reshape(-1, input_shape, 1)
    
    def get_parameters(self, config):
        """Return model parameters."""
        K.clear_session()
        temp_model = get_model_by_type(
            self.model_type, self.input_shape, 
            self.num_classes, self.config['learning_rate']
        )
        weights = temp_model.get_weights()
        del temp_model
        K.clear_session()
        return weights
    
    def set_parameters(self, parameters):
        """Set model parameters - not used in this implementation."""
        pass
    
    def fit(self, parameters, config):
        """Train model on local data using FedProx.
        
        The server sends 'proximal_mu' in the config dictionary.
        """
        # Clear previous session state
        K.clear_session()
        
        # Get proximal_mu from server config (sent by FedProx strategy)
        proximal_mu = config.get('proximal_mu', 0.01)
        
        # Create base model and set global weights
        base_model = get_model_by_type(
            self.model_type, self.input_shape, 
            self.num_classes, self.config['learning_rate']
        )
        base_model.set_weights(parameters)
        
        # Wrap with ProximalModel (parameters are the global weights for proximal term)
        proximal_model = ProximalModel(
            base_model, 
            parameters, 
            proximal_mu  # Use mu from server config
        )
        
        # Compile proximal model
        loss_fn = 'binary_crossentropy' if self.num_classes == 1 else 'sparse_categorical_crossentropy'
        proximal_model.compile(
            optimizer=keras.optimizers.Adam(learning_rate=self.config['learning_rate']),
            loss=loss_fn,
            metrics=['accuracy']
        )
        
        # Train with proximal term
        history = proximal_model.fit(
            self.X_train, self.y_train,
            epochs=self.config['local_epochs'],
            batch_size=self.config['batch_size'],
            verbose=0
        )
        
        # Extract updated weights from the base model (not wrapper)
        updated_weights = proximal_model.model.get_weights()
        
        # Prepare metrics
        metrics = {
            "train_loss": history.history['loss'][-1],
            "train_acc": history.history['accuracy'][-1]
        }
        
        # Clean up
        del base_model
        del proximal_model
        K.clear_session()
        
        return updated_weights, len(self.X_train), metrics
    
    def evaluate(self, parameters, config):
        """Evaluate model on local test data."""
        if self.X_test is None:
            return 0.0, 0, {}
        
        # Clear session and create fresh model for evaluation
        K.clear_session()
        
        eval_model = get_model_by_type(
            self.model_type, self.input_shape, 
            self.num_classes, self.config['learning_rate']
        )
        eval_model.set_weights(parameters)
        
        loss, accuracy = eval_model.evaluate(
            self.X_test, self.y_test, 
            batch_size=self.config['batch_size'], 
            verbose=0
        )
        
        # Clean up
        del eval_model
        K.clear_session()
        
        return loss, len(self.X_test), {"eval_acc": accuracy}


def create_client_fn_prox(client_data, test_data, model_type, input_shape, num_classes, config):
    """Factory function to create Flower clients with FedProx."""
    X_test, y_test = test_data
    
    def client_fn(cid: str) -> FlowerClientProx:
        client_id = int(cid)
        X_train, y_train = client_data[client_id]
        
        return FlowerClientProx(
            client_id, X_train, y_train, X_test, y_test,
            model_type, input_shape, num_classes, config
        )
    
    return client_fn

print("✅ Flower FedProx client class dan factory function didefinisikan")

# %% [markdown]
# ## BAGIAN 6: FUNGSI PELATIHAN FEDERATED DENGAN FEDPROX

# %%
def run_federated_learning_fedprox(
    client_data,
    test_data,
    model_type,
    input_shape,
    num_classes,
    num_rounds=5,
    num_clients=3,
    local_epochs=1,
    batch_size=256,
    learning_rate=0.001,
    mu=0.01,
    fraction_fit=1.0,
    fraction_evaluate=1.0
):
    """Run federated learning using Flower simulation with FedProx.
    
    Args:
        client_data: List of (X, y) tuples for each client
        test_data: Tuple of (X_test, y_test) for evaluation
        model_type: Type of model to use
        input_shape: Number of input features
        num_classes: Number of output classes
        num_rounds: Number of federated rounds
        num_clients: Number of clients
        local_epochs: Epochs per client per round
        batch_size: Batch size for training
        learning_rate: Learning rate
        mu: FedProx proximal term coefficient
        fraction_fit: Fraction of clients for training
        fraction_evaluate: Fraction of clients for evaluation
        
    Returns:
        Tuple of (final_model, history)
    """
    print(f"\n[INFO] Starting Flower FedProx federated learning for {model_type}...")
    print(f"   Clients: {num_clients} | Rounds: {num_rounds} | Local epochs: {local_epochs}")
    print(f"   Proximal term (μ): {mu}")
    
    # Configuration
    config = {
        'local_epochs': local_epochs,
        'batch_size': batch_size,
        'learning_rate': learning_rate,
    }
    
    # Create client factory
    client_fn = create_client_fn_prox(
        client_data, test_data, model_type, 
        input_shape, num_classes, config
    )
    
    # Create initial model to get parameters
    initial_model = get_model_by_type(model_type, input_shape, num_classes, learning_rate)
    initial_parameters = fl.common.ndarrays_to_parameters(initial_model.get_weights())
    
    # Define strategy with custom aggregation
    final_weights = [None]
    history_dict = {
        'train_accuracy': [],
        'train_loss': [],
        'eval_accuracy': [],
        'eval_loss': [],
        'round_time': [],
        'total_time': 0
    }
    
    round_start_time = [time.time()]
    
    # Use FedProx strategy from Flower (imported at top-level)
    
    class FedProxWithMetrics(FedProx):
        def aggregate_fit(self, server_round, results, failures):
            round_time = time.time() - round_start_time[0]
            history_dict['round_time'].append(round_time)
            
            aggregated_result = super().aggregate_fit(server_round, results, failures)
            if aggregated_result is not None:
                final_weights[0] = aggregated_result[0]
                
                if results:
                    train_losses = [fit_res.metrics.get('train_loss', 0) for _, fit_res in results if 'train_loss' in fit_res.metrics]
                    train_accs = [fit_res.metrics.get('train_acc', 0) for _, fit_res in results if 'train_acc' in fit_res.metrics]
                    
                    if train_losses:
                        avg_loss = np.mean(train_losses)
                        history_dict['train_loss'].append(avg_loss)
                        print(f"      Round {server_round} - Avg Train Loss: {avg_loss:.4f}")
                    
                    if train_accs:
                        avg_acc = np.mean(train_accs)
                        history_dict['train_accuracy'].append(avg_acc)
                        print(f"      Round {server_round} - Avg Train Acc: {avg_acc:.4f} - Time: {round_time:.2f}s")
            
            round_start_time[0] = time.time()
            return aggregated_result
        
        def aggregate_evaluate(self, server_round, results, failures):
            aggregated_result = super().aggregate_evaluate(server_round, results, failures)
            
            if results:
                eval_losses = [eval_res.loss for _, eval_res in results]
                eval_accs = [eval_res.metrics.get('eval_acc', 0) for _, eval_res in results if 'eval_acc' in eval_res.metrics]
                
                if eval_losses:
                    avg_eval_loss = np.mean(eval_losses)
                    history_dict['eval_loss'].append(avg_eval_loss)
                
                if eval_accs:
                    avg_eval_acc = np.mean(eval_accs)
                    history_dict['eval_accuracy'].append(avg_eval_acc)
            
            return aggregated_result
    
    strategy = FedProxWithMetrics(
        fraction_fit=fraction_fit,
        fraction_evaluate=fraction_evaluate,
        min_fit_clients=max(2, int(num_clients * fraction_fit)),
        min_evaluate_clients=max(2, int(num_clients * fraction_evaluate)),
        min_available_clients=num_clients,
        initial_parameters=initial_parameters,
        proximal_mu=mu,  # FedProx-specific parameter
    )
    
    # Start simulation
    start_time = time.time()
    
    history = start_simulation(
        client_fn=client_fn,
        num_clients=num_clients,
        config=fl.server.ServerConfig(num_rounds=num_rounds),
        strategy=strategy,
    )
    
    total_time = time.time() - start_time
    history_dict['total_time'] = total_time
    
    # Get final model
    final_model = get_model_by_type(model_type, input_shape, num_classes, learning_rate)
    
    if final_weights[0] is not None:
        parameters = fl.common.parameters_to_ndarrays(final_weights[0])
        final_model.set_weights(parameters)
        print(f"   ✓ Model weights updated from FedProx training")
    else:
        print(f"   ⚠ Warning: Using initial model weights")
    
    print(f"\nFedProx federated learning completed in {total_time:.2f}s")
    print(f"   Captured {len(history_dict['train_accuracy'])} rounds of training metrics")
    print(f"   Avg time per round: {np.mean(history_dict['round_time']):.2f}s")
    
    return final_model, history_dict

print("Fungsi federated learning FedProx didefinisikan")

# %% [markdown]
# ## BAGIAN 7: PELATIHAN SEMUA MODEL DENGAN FEDPROX

# %%
print("\n" + "="*70)
print("MEMULAI PELATIHAN FEDERATED PROXIMAL (FEDPROX) DENGAN FLOWER")
print(f"Proximal Term (μ) - Binary: {MU_BINARY}, Multi-class: {MU_MULTI}")
print("="*70)

all_models = {}
all_histories = {}
all_metrics = {}

# Training Binary Models
print("\n--- PELATIHAN DETEKSI BINER DENGAN FEDPROX ---")

print("\nMelatih Model MLP Binary...")
all_models['mlp_binary'], all_histories['mlp_binary'] = run_federated_learning_fedprox(
    client_data_binary,
    (X_test_bin_scaled, y_test_bin),
    'mlp_binary',
    X_train_bin_scaled.shape[1],
    1,
    num_rounds=NUM_ROUNDS,
    num_clients=NUM_CLIENTS,
    local_epochs=LOCAL_EPOCHS,
    batch_size=BATCH_SIZE_BINARY,
    learning_rate=LEARNING_RATE,
    mu=MU_BINARY
)

print("\nMelatih Model CNN Binary...")
all_models['cnn_binary'], all_histories['cnn_binary'] = run_federated_learning_fedprox(
    client_data_binary,
    (X_test_bin_scaled, y_test_bin),
    'cnn_binary',
    X_train_bin_scaled.shape[1],
    1,
    num_rounds=NUM_ROUNDS,
    num_clients=NUM_CLIENTS,
    local_epochs=LOCAL_EPOCHS,
    batch_size=BATCH_SIZE_BINARY,
    learning_rate=LEARNING_RATE,
    mu=MU_BINARY
)

# Training Multi-class Models
print("\n--- PELATIHAN KLASIFIKASI MULTI-KELAS DENGAN FEDPROX ---")

print("\nMelatih Model MLP Multi-class...")
all_models['mlp_multi'], all_histories['mlp_multi'] = run_federated_learning_fedprox(
    client_data_multi,
    (X_test_multi_scaled, y_test_multi),
    'mlp_multi',
    X_train_multi_scaled.shape[1],
    num_classes,
    num_rounds=NUM_ROUNDS,
    num_clients=NUM_CLIENTS,
    local_epochs=LOCAL_EPOCHS,
    batch_size=BATCH_SIZE_MULTI,
    learning_rate=LEARNING_RATE,
    mu=MU_MULTI
)

print("\n Melatih Model CNN Multi-class...")
all_models['cnn_multi'], all_histories['cnn_multi'] = run_federated_learning_fedprox(
    client_data_multi,
    (X_test_multi_scaled, y_test_multi),
    'cnn_multi',
    X_train_multi_scaled.shape[1],
    num_classes,
    num_rounds=NUM_ROUNDS,
    num_clients=NUM_CLIENTS,
    local_epochs=LOCAL_EPOCHS,
    batch_size=BATCH_SIZE_MULTI,
    learning_rate=LEARNING_RATE,
    mu=MU_MULTI
)

print("\nSemua model berhasil dilatih dengan FedProx!")

# %% [markdown]
# ## BAGIAN 8: EVALUASI MODEL

# %%
# Cell baru: VERIFICATION BEFORE EVALUATION
print("="*70)
print("PRE-EVALUATION VERIFICATION")
print("="*70)

# 1. Check shapes
print(f"\n1. Feature Shapes:")
print(f"   Binary - Train: {X_train_bin_scaled.shape}")
print(f"   Binary - Test: {X_test_bin_scaled.shape}")
print(f"   Multi - Train: {X_train_multi_scaled.shape}")
print(f"   Multi - Test: {X_test_multi_scaled.shape}")

# 2. Check data quality
print(f"\n2. Data Quality (Test Set):")
print(f"   Binary - NaN: {np.isnan(X_test_bin_scaled).sum()}")
print(f"   Binary - Inf: {np.isinf(X_test_bin_scaled).sum()}")
print(f"   Multi - NaN: {np.isnan(X_test_multi_scaled).sum()}")
print(f"   Multi - Inf: {np.isinf(X_test_multi_scaled).sum()}")

# 3. Check model inputs
print(f"\n3. Model Expected Inputs:")
for name, model in all_models.items():
    print(f"   {name}: {model.input_shape}")

# 4. Test a single prediction
print(f"\n4. Quick Prediction Test:")
sample_bin = X_test_bin_scaled[:1].astype(np.float32)
try:
    pred = all_models['mlp_binary'].predict(sample_bin, verbose=0)
    print(f"   MLP Binary - Prediction: {pred[0][0]:.4f}")
except Exception as e:
    print(f"   ❌ ERROR: {e}")

print("="*70)

# %%
print("\n" + "="*70)
print("EVALUASI SEMUA MODEL")
print("="*70)

# Evaluate Binary Models
print("\n--- EVALUASI MODEL BINARY ---")

# MLP Binary
print("\n[1/4] MLP Binary...")
X_test_eval = X_test_bin_scaled.astype(np.float32)
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=DeprecationWarning)
    y_pred_prob = all_models['mlp_binary'].predict(X_test_eval, verbose=0)
y_pred = (y_pred_prob > 0.5).astype(int).flatten()
all_metrics['MLP Binary'] = evaluate_model_metrics(
    y_test_bin, y_pred, "MLP Binary (FedProx)", is_binary=True,
    target_names=['Normal', 'Attack'],
    y_pred_proba=y_pred_prob
)

# CNN Binary
print("\n[2/4] CNN Binary...")
X_test_eval_cnn = X_test_bin_scaled.reshape(-1, X_train_bin_scaled.shape[1], 1).astype(np.float32)
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=DeprecationWarning)
    y_pred_prob = all_models['cnn_binary'].predict(X_test_eval_cnn, verbose=0)
y_pred = (y_pred_prob > 0.5).astype(int).flatten()
all_metrics['CNN Binary'] = evaluate_model_metrics(
    y_test_bin, y_pred, "CNN Binary (FedProx)", is_binary=True,
    target_names=['Normal', 'Attack'],
    y_pred_proba=y_pred_prob
)

# Evaluate Multi-class Models
print("\n--- EVALUASI MODEL MULTI-CLASS ---")

# MLP Multi
print("\n[3/4] MLP Multi-class...")
X_test_eval = X_test_multi_scaled.astype(np.float32)
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=DeprecationWarning)
    y_pred_prob = all_models['mlp_multi'].predict(X_test_eval, verbose=0)
y_pred = np.argmax(y_pred_prob, axis=1)
all_metrics['MLP Multi'] = evaluate_model_metrics(
    y_test_multi, y_pred, "MLP Multi (FedProx)", is_binary=False,
    target_names=le_target.classes_,
    y_pred_proba=y_pred_prob
)

# CNN Multi
print("\n[4/4] CNN Multi-class...")
X_test_eval_cnn = X_test_multi_scaled.reshape(-1, X_train_multi_scaled.shape[1], 1).astype(np.float32)
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=DeprecationWarning)
    y_pred_prob = all_models['cnn_multi'].predict(X_test_eval_cnn, verbose=0)
y_pred = np.argmax(y_pred_prob, axis=1)
all_metrics['CNN Multi'] = evaluate_model_metrics(
    y_test_multi, y_pred, "CNN Multi (FedProx)", is_binary=False,
    target_names=le_target.classes_,
    y_pred_proba=y_pred_prob
)

print("\n" + "="*70)

# %% [markdown]
# ### 8.1 Tabel Ringkasan Performa Semua Model

# %%
# Pastikan `all_metrics` tersedia dari evaluasi sebelumnya
if 'all_metrics' not in globals():
    raise NameError('Variabel all_metrics tidak ditemukan. Jalankan sel evaluasi model terlebih dahulu.')

# Buat DataFrame ringkasan dari all_metrics
rows = []
for model_name, metrics in all_metrics.items():
    rows.append({
        'Model': model_name,
        'Accuracy': metrics.get('accuracy', 0.0),
        'Precision': metrics.get('precision', 0.0),
        'Recall': metrics.get('recall', 0.0),
        'F1-Score': metrics.get('f1_score', 0.0),
        'AUC-ROC': metrics.get('auc_roc', 0.0)
    })

df_summary = pd.DataFrame(rows).set_index('Model')
# Urutkan berdasarkan F1-Score menurun
df_summary = df_summary.sort_values(by='F1-Score', ascending=False)

# Tampilkan ringkasan sebagai HTML di notebook
try:
    html = '<h3>TABEL RINGKASAN PERFORMA SEMUA MODEL</h3>'
    html += df_summary.to_html(float_format='%.4f')
    display(HTML(html))
except Exception:
    # fallback to text output
    print(df_summary.to_string(float_format=lambda x: f"{x:.4f}"))

# Simpan ringkasan ke file pickle untuk penggunaan selanjutnya
try:
    with open('all_metrics_summary.pkl', 'wb') as f:
        pickle.dump(df_summary, f)
    print('\nSummary saved to all_metrics_summary.pkl')
except Exception as e:
    print(f'Could not save pickle: {e}')

# %% [markdown]
# ### 8.2 Analisis Best Performing Models

# %%
# Identify best models for each metric
best_models = {
    'F1-Score': max(all_metrics.items(), key=lambda x: x[1]['f1_score']),
    'AUC-ROC': max(all_metrics.items(), key=lambda x: x[1].get('auc_roc', 0)),
    'Accuracy': max(all_metrics.items(), key=lambda x: x[1]['accuracy']),
    'Recall': max(all_metrics.items(), key=lambda x: x[1]['recall']),
    'Precision': max(all_metrics.items(), key=lambda x: x[1]['precision'])
}

print("="*70)
print("BEST PERFORMING MODELS BY METRIC")
print("="*70)

best_data = []
for metric_name, (model_name, metrics) in best_models.items():
    metric_value = metrics.get(metric_name.lower().replace('-', '_'), 
                               metrics.get('f1_score' if metric_name == 'F1-Score' else 
                                         'auc_roc' if metric_name == 'AUC-ROC' else metric_name.lower()))
    best_data.append([
        metric_name,
        model_name,
        f"{metric_value:.4f}"
    ])

print(tabulate(best_data, headers=["Metric", "Best Model", "Value"], tablefmt="grid"))

# Separate analysis for Binary vs Multi-class
print("\n" + "="*70)
print("BEST MODELS BY CLASSIFICATION TYPE")
print("="*70)

binary_models = {k: v for k, v in all_metrics.items() if 'Binary' in k}
multi_models = {k: v for k, v in all_metrics.items() if 'Multi' in k}

best_binary = max(binary_models.items(), key=lambda x: (x[1]['f1_score'] + x[1].get('auc_roc', 0)) / 2)
best_multi = max(multi_models.items(), key=lambda x: (x[1]['f1_score'] + x[1].get('auc_roc', 0)) / 2)

classification_best = [
    [
        "Binary Classification",
        best_binary[0],
        f"{best_binary[1]['accuracy']:.4f}",
        f"{best_binary[1]['f1_score']:.4f}",
        f"{best_binary[1].get('auc_roc', 0):.4f}",
        f"{(best_binary[1]['f1_score'] + best_binary[1].get('auc_roc', 0)) / 2:.4f}"
    ],
    [
        "Multi-class Classification",
        best_multi[0],
        f"{best_multi[1]['accuracy']:.4f}",
        f"{best_multi[1]['f1_score']:.4f}",
        f"{best_multi[1].get('auc_roc', 0):.4f}",
        f"{(best_multi[1]['f1_score'] + best_multi[1].get('auc_roc', 0)) / 2:.4f}"
    ]
]

print(tabulate(classification_best, 
               headers=["Type", "Model", "Accuracy", "F1", "AUC-ROC", "Avg(F1+AUC)"], 
               tablefmt="grid"))

print("\nRECOMMENDATION:")
print(f"  - For Binary Detection: Use {best_binary[0]}")
print(f"    Balanced score (F1+AUC)/2: {(best_binary[1]['f1_score'] + best_binary[1].get('auc_roc', 0)) / 2:.4f}")
print(f"  - For Multi-class Attack Type: Use {best_multi[0]}")
print(f"    Balanced score (F1+AUC)/2: {(best_multi[1]['f1_score'] + best_multi[1].get('auc_roc', 0)) / 2:.4f}")
print("="*70)

# %% [markdown]
# ### 8.3 Confusion Matrix Analysis
# 
# **Detailed confusion matrices for all models**

# %%
print("="*70)
print("CONFUSION MATRIX ANALYSIS")
print("="*70)

# Create figure with 2x2 subplots for all models
fig, axes = plt.subplots(2, 2, figsize=(16, 14))
fig.suptitle('Confusion Matrices - All Models (FedProx)', fontsize=16, fontweight='bold', y=0.995)

model_configs = [
    ('MLP Binary', 'mlp_binary', y_test_bin, ['Normal', 'Attack'], axes[0, 0]),
    ('CNN Binary', 'cnn_binary', y_test_bin, ['Normal', 'Attack'], axes[0, 1]),
    ('MLP Multi', 'mlp_multi', y_test_multi, le_target.classes_, axes[1, 0]),
    ('CNN Multi', 'cnn_multi', y_test_multi, le_target.classes_, axes[1, 1])
]

for model_name, model_key, y_true, labels, ax in model_configs:
    # Get predictions
    y_pred = all_metrics[model_name]['predictions']
    
    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    
    # Plot heatmap
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax,
                xticklabels=labels, yticklabels=labels,
                cbar_kws={'label': 'Count'})
    
    # Add metrics to title
    acc = all_metrics[model_name]['accuracy']
    f1 = all_metrics[model_name]['f1_score']
    ax.set_title(f'{model_name}\nAcc: {acc:.4f} | F1: {f1:.4f}', 
                 fontsize=12, fontweight='bold')
    ax.set_ylabel('True Label', fontsize=11)
    ax.set_xlabel('Predicted Label', fontsize=11)
    
    # Rotate labels for multi-class
    if 'Multi' in model_name:
        ax.set_xticklabels(labels, rotation=45, ha='right')
        ax.set_yticklabels(labels, rotation=0)

plt.tight_layout()
plt.savefig('fedprox_confusion_matrices.png', dpi=300, bbox_inches='tight')
print("\n✓ Confusion matrices saved as 'fedprox_confusion_matrices.png'")
plt.show()

# Print detailed metrics per class for multi-class models
print("\n" + "="*70)
print("PER-CLASS PERFORMANCE ANALYSIS (Multi-class Models)")
print("="*70)

for model_name in ['MLP Multi', 'CNN Multi']:
    print(f"\n{model_name}:")
    y_pred = all_metrics[model_name]['predictions']
    
    # Classification report
    from sklearn.metrics import classification_report
    report = classification_report(y_test_multi, y_pred, 
                                   target_names=le_target.classes_,
                                   output_dict=True)
    
    # Build table
    rows = []
    for class_name in le_target.classes_:
        if class_name in report:
            rows.append([
                class_name,
                f"{report[class_name]['precision']:.4f}",
                f"{report[class_name]['recall']:.4f}",
                f"{report[class_name]['f1-score']:.4f}",
                f"{int(report[class_name]['support']):,}"
            ])
    
    print(tabulate(rows, 
                   headers=['Class', 'Precision', 'Recall', 'F1-Score', 'Support'],
                   tablefmt='grid'))

print("\n" + "="*70)

# %% [markdown]
# ## BAGIAN 9: VISUALISASI HASIL FEDPROX

# %%
print("\n" + "="*70)
print("VISUALISASI HASIL FLOWER FEDPROX")
print("="*70)

plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(4, 2, figsize=(20, 24))

model_names = ['MLP Binary', 'CNN Binary', 'MLP Multi', 'CNN Multi']
model_keys = ['mlp_binary', 'cnn_binary', 'mlp_multi', 'cnn_multi']
colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D']
markers = ['o', 's', '^', 'd']

# Plot 1: Training Accuracy per Round
axes[0, 0].set_title('Training Accuracy per Round (FedProx)', fontsize=14, fontweight='bold')
for i, (name, key) in enumerate(zip(model_names, model_keys)):
    if all_histories[key]['train_accuracy']:
        rounds = list(range(1, len(all_histories[key]['train_accuracy']) + 1))
        axes[0, 0].plot(rounds, all_histories[key]['train_accuracy'], 
                       label=name, marker=markers[i], color=colors[i], 
                       linewidth=2, markersize=8)

axes[0, 0].set_xlabel('Round', fontsize=12)
axes[0, 0].set_ylabel('Accuracy', fontsize=12)
axes[0, 0].legend(loc='lower right', fontsize=10)
axes[0, 0].grid(True, linestyle='--', alpha=0.5)
axes[0, 0].set_ylim(0, 1.1)

# Plot 2: Training Loss per Round
axes[0, 1].set_title('Training Loss per Round (FedProx)', fontsize=14, fontweight='bold')
for i, (name, key) in enumerate(zip(model_names, model_keys)):
    if all_histories[key]['train_loss']:
        rounds = list(range(1, len(all_histories[key]['train_loss']) + 1))
        axes[0, 1].plot(rounds, all_histories[key]['train_loss'], 
                       label=name, marker=markers[i], color=colors[i], 
                       linewidth=2, markersize=8)

axes[0, 1].set_xlabel('Round', fontsize=12)
axes[0, 1].set_ylabel('Loss', fontsize=12)
axes[0, 1].legend(loc='upper right', fontsize=10)
axes[0, 1].grid(True, linestyle='--', alpha=0.5)

# Plot 3: Round Time per Round
axes[1, 0].set_title('Training Time per Round (FedProx)', fontsize=14, fontweight='bold')
for i, (name, key) in enumerate(zip(model_names, model_keys)):
    if all_histories[key]['round_time']:
        rounds = list(range(1, len(all_histories[key]['round_time']) + 1))
        axes[1, 0].plot(rounds, all_histories[key]['round_time'], 
                       label=name, marker=markers[i], color=colors[i], 
                       linewidth=2, markersize=8)

axes[1, 0].set_xlabel('Round', fontsize=12)
axes[1, 0].set_ylabel('Time (seconds)', fontsize=12)
axes[1, 0].legend(loc='upper right', fontsize=10)
axes[1, 0].grid(True, linestyle='--', alpha=0.5)

# Plot 4: Total Training Time Comparison
total_times = [all_histories[key]['total_time'] for key in model_keys]
avg_round_times = [np.mean(all_histories[key]['round_time']) for key in model_keys]

x_pos = np.arange(len(model_names))
width = 0.35

bars_total = axes[1, 1].bar(x_pos - width/2, total_times, width, label='Total Time', 
                            color=colors, alpha=0.8, edgecolor='black')
bars_avg = axes[1, 1].bar(x_pos + width/2, avg_round_times, width, label='Avg Time/Round', 
                          color=colors, alpha=0.6, edgecolor='black')

axes[1, 1].set_title('Training Time Comparison (FedProx)', fontsize=14, fontweight='bold')
axes[1, 1].set_ylabel('Time (seconds)', fontsize=12)
axes[1, 1].set_xticks(x_pos)
axes[1, 1].set_xticklabels(model_names, rotation=45, ha='right')
axes[1, 1].legend()
axes[1, 1].grid(True, linestyle='--', alpha=0.3, axis='y')

for bar, t_time in zip(bars_total, total_times):
    axes[1, 1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(total_times)*0.01, 
                    f'{t_time:.1f}s', ha='center', fontsize=9, fontweight='bold')

# Plot 5: Accuracy Comparison
accuracies = [all_metrics[name]['accuracy'] for name in model_names]
f1_scores = [all_metrics[name]['f1_score'] for name in model_names]

bars1 = axes[2, 0].bar(x_pos - width/2, accuracies, width, label='Accuracy', 
                       color=colors, alpha=0.8, edgecolor='black')
bars2 = axes[2, 0].bar(x_pos + width/2, f1_scores, width, label='F1-Score', 
                       color=colors, alpha=0.6, edgecolor='black')

axes[2, 0].set_title('Perbandingan Akurasi dan F1-Score (FedProx)', fontsize=14, fontweight='bold')
axes[2, 0].set_ylabel('Skor', fontsize=12)
axes[2, 0].set_xticks(x_pos)
axes[2, 0].set_xticklabels(model_names, rotation=45, ha='right')
axes[2, 0].legend()
axes[2, 0].set_ylim(0, 1.1)

for bar, acc in zip(bars1, accuracies):
    axes[2, 0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02, 
                    f'{acc:.3f}', ha='center', fontweight='bold', fontsize=10)

# Plot 6: Precision vs Recall
precisions = [all_metrics[name]['precision'] for name in model_names]
recalls = [all_metrics[name]['recall'] for name in model_names]

bars3 = axes[2, 1].bar(x_pos - width/2, precisions, width, label='Precision', 
                       color=colors, alpha=0.8, edgecolor='black')
bars4 = axes[2, 1].bar(x_pos + width/2, recalls, width, label='Recall', 
                       color=colors, alpha=0.6, edgecolor='black')

axes[2, 1].set_title('Perbandingan Precision dan Recall (FedProx)', fontsize=14, fontweight='bold')
axes[2, 1].set_ylabel('Skor', fontsize=12)
axes[2, 1].set_xticks(x_pos)
axes[2, 1].set_xticklabels(model_names, rotation=45, ha='right')
axes[2, 1].legend()
axes[2, 1].set_ylim(0, 1.1)

# Plot 7: Confusion Matrix for Best Binary Model
best_binary = 'MLP Binary' if all_metrics['MLP Binary']['f1_score'] > all_metrics['CNN Binary']['f1_score'] else 'CNN Binary'
y_pred_best = all_metrics[best_binary]['predictions']
cm = confusion_matrix(y_test_bin, y_pred_best)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[3, 0],
            xticklabels=['Normal', 'Attack'],
            yticklabels=['Normal', 'Attack'])
axes[3, 0].set_title(f'Confusion Matrix - {best_binary} (FedProx)', fontsize=14, fontweight='bold')
axes[3, 0].set_ylabel('True Label', fontsize=12)
axes[3, 0].set_xlabel('Predicted Label', fontsize=12)

# Plot 8: Model Comparison Summary
metrics_data = []
for name in model_names:
    metrics_data.append([
        all_metrics[name]['accuracy'],
        all_metrics[name]['precision'],
        all_metrics[name]['recall'],
        all_metrics[name]['f1_score']
    ])

x_metrics = np.arange(4)
bar_width = 0.2

for i, (name, data) in enumerate(zip(model_names, metrics_data)):
    axes[3, 1].bar(x_metrics + i*bar_width, data, bar_width, 
                   label=name, color=colors[i], alpha=0.8)

axes[3, 1].set_title('Ringkasan Semua Metrik (FedProx)', fontsize=14, fontweight='bold')
axes[3, 1].set_ylabel('Skor', fontsize=12)
axes[3, 1].set_xticks(x_metrics + bar_width * 1.5)
axes[3, 1].set_xticklabels(['Accuracy', 'Precision', 'Recall', 'F1-Score'])
axes[3, 1].legend(loc='lower right', fontsize=8)
axes[3, 1].set_ylim(0, 1.1)
axes[3, 1].grid(True, linestyle='--', alpha=0.3)

plt.tight_layout(pad=3.0)
plt.savefig('fedprox_comprehensive_results.png', dpi=300, bbox_inches='tight')
print("\nVisualisasi disimpan sebagai 'fedprox_comprehensive_results.png'")
plt.show()

# %% [markdown]
# ## BAGIAN 10: LAPORAN AKHIR FEDPROX

# %%
print("\n" + "="*80)
print("LAPORAN AKHIR - FEDERATED PROXIMAL (FEDPROX) DENGAN FLOWER")
print("="*80)

print(f"\nINFORMASI EKSPERIMEN:")
print(f"   - Framework: {FRAMEWORK}")
print(f"   - Algoritma: {ALGORITHM}")
print(f"   - Proximal Term (mu) - Binary: {MU_BINARY}, Multi-class: {MU_MULTI}")
print(f"   - Jumlah Klien: {NUM_CLIENTS}")
print(f"   - Distribusi Data: {DATA_DISTRIBUTION}")
print(f"   - Alpha Binary: {ALPHA_BINARY} | Alpha Multi-class: {ALPHA_MULTI}")
print(f"   - Putaran Komunikasi: {NUM_ROUNDS}")
print(f"   - Local Epochs: {LOCAL_EPOCHS}")
print(f"   - Batch Size - Binary: {BATCH_SIZE_BINARY} | Multi-class: {BATCH_SIZE_MULTI}")
print(f"   - Learning Rate: {LEARNING_RATE}")
#print(f"   - Ukuran Dataset: {df.shape[0]:,} sampel")
print(f"   - Preprocessing: Smart protocol-aware preprocessing")
print(f"   - NO SMOTE: Natural class distribution preserved")

print(f"\nDISTRIBUSI DATA KE KLIEN:")
for i, (X_client, y_client) in enumerate(client_data_binary):
    print(f"   - Klien {i+1} (Binary): {len(X_client):,} sampel")

print(f"\nWAKTU PELATIHAN:")
model_names_keys = [
    ('MLP Binary', 'mlp_binary'),
    ('CNN Binary', 'cnn_binary'),
    ('MLP Multi', 'mlp_multi'),
    ('CNN Multi', 'cnn_multi')
]
total_training_time = sum(all_histories[key]['total_time'] for _, key in model_names_keys)

for name, key in model_names_keys:
    history = all_histories[key]
    print(f"   - {name}:")
    print(f"      - Total: {history['total_time']:.2f}s")
    print(f"      - Per Round (avg): {np.mean(history['round_time']):.2f}s")
    print(f"      - Per Round (min/max): {np.min(history['round_time']):.2f}s / {np.max(history['round_time']):.2f}s")

print(f"\n   - Total Waktu Pelatihan Semua Model: {total_training_time:.2f}s ({total_training_time/60:.2f} menit)")

print(f"\nMODEL TERBAIK:")
best_binary = max(
    [(name, metrics) for name, metrics in all_metrics.items() if 'Binary' in name],
    key=lambda x: x[1]['f1_score']
)
best_multi = max(
    [(name, metrics) for name, metrics in all_metrics.items() if 'Multi' in name],
    key=lambda x: x[1]['f1_score']
)

print(f"   Klasifikasi Binary:")
print(f"      - Terbaik: {best_binary[0]}")
print(f"      - Accuracy: {best_binary[1]['accuracy']:.4f}")
print(f"      - Precision: {best_binary[1]['precision']:.4f}")
print(f"      - Recall: {best_binary[1]['recall']:.4f}")
print(f"      - F1-Score: {best_binary[1]['f1_score']:.4f}")

print(f"\n   Klasifikasi Multi-class:")
print(f"      - Terbaik: {best_multi[0]}")
print(f"      - Accuracy: {best_multi[1]['accuracy']:.4f}")
print(f"      - Precision: {best_multi[1]['precision']:.4f}")
print(f"      - Recall: {best_multi[1]['recall']:.4f}")
print(f"      - F1-Score: {best_multi[1]['f1_score']:.4f}")

print(f"\nRINGKASAN PERFORMA SEMUA MODEL:")
for name in ['MLP Binary', 'CNN Binary', 'MLP Multi', 'CNN Multi']:
    metrics = all_metrics[name]
    print(f"   - {name}:")
    print(f"      - Accuracy: {metrics['accuracy']:.4f}")
    print(f"      - Precision: {metrics['precision']:.4f}")
    print(f"      - Recall: {metrics['recall']:.4f}")
    print(f"      - F1-Score: {metrics['f1_score']:.4f}")

print(f"\nKESIMPULAN:")
print(f"   - FedProx berhasil melatih {len(all_models)} model pada lingkungan Non-IID")
print(f"   - Proximal term (mu= Binary {MU_BINARY}, Multi {MU_MULTI}) membantu konvergensi pada data heterogen")
print(f"   - FedProx lebih stabil dibandingkan FedAvg pada data yang sangat Non-IID")
print(f"   - Smart preprocessing menjaga semantic meaning protocol-specific features")
print(f"   - Natural class distribution (tanpa SMOTE) lebih realistis untuk FL")

print(f"\nKEUNGGULAN FEDPROX:")
print(f"   - Convergence lebih stabil pada data Non-IID")
print(f"   - Mengatasi system heterogeneity (klien dengan kemampuan berbeda)")
print(f"   - Proximal term mencegah model lokal terlalu jauh dari global")
print(f"   - Hyperparameter mu dapat disesuaikan untuk berbagai skenario")
print(f"   - Implementasi sederhana dengan Flower framework")

print(f"\nPARAMETER FEDPROX:")
print(f"   - mu (mu) Binary = {MU_BINARY}: Proximal term untuk binary models")
print(f"   - mu (mu) Multi = {MU_MULTI}: Proximal term untuk multi-class")
print(f"   - Proximal term: (mu/2)||w - w_global||^2")
print(f"   - Lower mu for multi-class allows more local learning on imbalanced data")
print(f"   - Aggregation: Weighted averaging (sama dengan FedAvg)")
print(f"   - Training: Local loss + proximal term")

print(f"\nPREPROCESSING STRATEGY:")
print(f"   - Smart protocol-aware preprocessing")
print(f"   - Context-aware missing value handling")
print(f"   - Protocol indicators: has_dns, has_http, has_ssl")
print(f"   - Feature engineering: bytes_ratio, pkts_ratio, rate features")
print(f"   - Pipeline: Split -> RFE -> Scale (no data leakage)")
print(f"   - NO SMOTE: Preserves natural Non-IID characteristics")

print("\nEKSPERIMEN FEDPROX SELESAI")
print("="*80)


