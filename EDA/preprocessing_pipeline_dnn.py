"""
Preprocessing Pipeline for TON_IoT Dataset - Deep Learning Optimized
Designed for Fair Comparison: MLP vs CNN-1D

This pipeline creates a NEUTRAL preprocessing strategy that allows fair 
comparison between Multi-Layer Perceptron (MLP) and 1D Convolutional Neural 
Network (CNN-1D) architectures.

KEY DIFFERENCES FROM TRADITIONAL ML PIPELINE:
==============================================

1. AGGRESSIVE DROPPING (Technical Requirements, NOT Bias):
   - High-cardinality strings (dns_query, http_uri, etc.) → MUST drop for DNN
   - Text features → Cannot be used without embedding (out of scope)
   - Identifiers (IPs, raw ports, timestamp) → As per Moustafa paper

2. MINIMAL FEATURE ENGINEERING (Fair for Both Models):
   - Keep simple numeric indicators (protocol flags, port service indicators)
   - Drop complex engineered features (temporal bins, connection state categories)
   - Let models learn representations from raw numeric features

3. ENCODING STRATEGY:
   - Categorical features → Label Encoding (NOT OneHot) to prevent dimension explosion
   - Keeps input compact and fair for both MLP and CNN-1D

4. MANDATORY SCALING:
   - StandardScaler → Essential for gradient descent convergence
   - Prevents features with large ranges from dominating

FAIRNESS PRINCIPLES:
====================
✓ Both models get SAME preprocessed data
✓ No architecture-specific feature engineering
✓ Minimal human intervention → let models learn
✓ Focus on network traffic statistics (core TON_IoT features)

TARGET USE CASE:
================
- Small dataset (~211K rows)
- Binary & Multiclass classification
- Model comparison: MLP vs CNN-1D
- Research paper evaluation

Usage:
    python preprocessing_pipeline_dnn.py --mode full
    python preprocessing_pipeline_dnn.py --mode binary
    python preprocessing_pipeline_dnn.py --mode multi

References:
    [1] TON_Network_dataset.md - Dataset documentation
    [2] Moustafa, N. (2021) - TON_IoT dataset paper
    [3] Deep Learning best practices for NIDS
"""

import pandas as pd
import numpy as np
import pickle
import argparse
import time
from pathlib import Path
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

# TensorFlow GPU check
try:
    import tensorflow as tf
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        print(f"🚀 TensorFlow GPU: {len(gpus)} device(s) available")
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
except Exception as e:
    print(f"⚠️  TensorFlow GPU not available: {e}")


class DNNPreprocessingConfig:
    """
    Configuration for Deep Learning preprocessing pipeline
    
    Optimized for fair comparison between MLP and CNN-1D on small dataset.
    """
    
    # Paths
    RAW_DATA_PATH = "/home/elnoersan/Skripsi/Paper/NotebookTODO/train_test_network.csv"
    OUTPUT_DIR = Path("/home/elnoersan/Skripsi/Paper/NotebookTODO/EDA/processed_artifacts")
    
    # Split config
    TEST_SIZE = 0.2
    RANDOM_STATE = 42
    
    # AGGRESSIVE DROP LIST (Required for DNN, not bias)
    # ===================================================
    # 1. Identifiers (per Moustafa paper Section 6.1)
    DROP_IDENTIFIERS = [
        'ts',           # Timestamp (not time-series model)
        'src_ip',       # Source IP
        'dst_ip',       # Destination IP
        'src_port',     # Raw source port (will create indicator instead)
        'dst_port',     # Raw destination port (will create indicator instead)
    ]
    
    # 2. High-Cardinality Strings (Technical requirement - cannot use in DNN)
    DROP_HIGH_CARDINALITY = [
        'dns_query',              # DNS queries (unlimited variations)
        'http_uri',               # HTTP URIs (unlimited variations)
        'http_user_agent',        # User agents (thousands of variations)
        'http_orig_mime_types',   # MIME types
        'http_resp_mime_types',   # Response MIME types
        'ssl_subject',            # SSL subjects (text)
        'ssl_issuer',             # SSL issuers (text)
        'weird_name',             # Violation names (high cardinality)
        'weird_addl',             # Additional violation info
        'weird_notice',           # Violation notices
    ]
    
    # 3. Sparse/Mostly Null Features (will check dynamically)
    NULL_THRESHOLD = 0.70  # Drop if >70% null
    
    # KEEP: Low-cardinality categorical (will be Label Encoded)
    CATEGORICAL_TO_ENCODE = ['proto', 'service', 'conn_state']
    
    # KEEP: All numeric features (network statistics)
    # These are the CORE features for intrusion detection


class DNNPreprocessor:
    """Deep Learning preprocessing class"""
    
    def __init__(self, config: DNNPreprocessingConfig):
        self.config = config
        self.config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        
    def load_data(self):
        """Load raw dataset"""
        print("="*70)
        print("LOADING RAW DATA (DNN Pipeline)")
        print("="*70)
        start = time.time()
        
        df = pd.read_csv(self.config.RAW_DATA_PATH)
        print(f"✓ Loaded: {df.shape}")
        print(f"  Time: {time.time() - start:.2f}s")
        return df
    
    def analyze_nulls(self, df):
        """Analyze null percentages to identify sparse columns"""
        print("\n" + "="*70)
        print("NULL ANALYSIS")
        print("="*70)
        
        null_pct = (df.isnull().sum() / len(df)) * 100
        high_null_cols = null_pct[null_pct > self.config.NULL_THRESHOLD * 100].sort_values(ascending=False)
        
        if len(high_null_cols) > 0:
            print(f"Columns with >{self.config.NULL_THRESHOLD*100}% nulls:")
            for col, pct in high_null_cols.items():
                print(f"  - {col}: {pct:.2f}%")
        else:
            print(f"✓ No columns with >{self.config.NULL_THRESHOLD*100}% nulls")
        
        return high_null_cols.index.tolist()
    
    def basic_preprocessing(self, df):
        """
        Basic preprocessing: Fill nulls with simple strategy
        
        For DNN: Simple is better. Let model learn patterns.
        """
        print("\n" + "="*70)
        print("BASIC PREPROCESSING")
        print("="*70)
        
        # Fill numeric nulls with median
        print("[1/2] Filling numeric nulls with median...")
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            if df[col].isnull().sum() > 0:
                df[col] = df[col].fillna(df[col].median())
        
        # Fill categorical nulls with mode or 'unknown'
        print("[2/2] Filling categorical nulls with mode...")
        cat_cols = df.select_dtypes(include=['object']).columns
        for col in cat_cols:
            if df[col].isnull().sum() > 0:
                mode_val = df[col].mode()
                fill_val = mode_val[0] if len(mode_val) > 0 else 'unknown'
                df[col] = df[col].fillna(fill_val)
        
        remaining_nan = df.isnull().sum().sum()
        print(f"✓ Preprocessing complete. Remaining NaN: {remaining_nan}")
        
        return df
    
    def create_minimal_features(self, df):
        """
        Create MINIMAL feature engineering (fair for both MLP and CNN-1D)
        
        Only simple binary indicators - no complex engineering
        """
        print("\n" + "="*70)
        print("MINIMAL FEATURE ENGINEERING (Neutral)")
        print("="*70)
        
        # Protocol indicators (simple binary flags from existing data)
        print("[1/3] Creating protocol indicators...")
        if 'dns_query' in df.columns:
            df['has_dns_features'] = df['dns_query'].notna().astype(int)
        if 'http_method' in df.columns:
            df['has_http_features'] = df['http_method'].notna().astype(int)
        if 'ssl_version' in df.columns:
            df['has_ssl_features'] = df['ssl_version'].notna().astype(int)
        
        # Port service indicators (simple binary - is it a common service port?)
        print("[2/3] Creating port service indicators...")
        if 'src_port' in df.columns:
            df['src_is_service_port'] = (df['src_port'] <= 1024).astype(int)
        if 'dst_port' in df.columns:
            df['dst_is_service_port'] = (df['dst_port'] <= 1024).astype(int)
            df['dst_is_web_service'] = df['dst_port'].isin([80, 443, 8080, 8443]).astype(int)
        
        # Connection indicators (simple binary from conn_state)
        print("[3/3] Creating connection indicators...")
        if 'conn_state' in df.columns:
            df['is_rejected_conn'] = df['conn_state'].isin(['REJ', 'RSTO', 'RSTOS0']).astype(int)
            df['is_established_conn'] = (df['conn_state'] == 'SF').astype(int)
        
        print("✓ Minimal features created (7 simple indicators)")
        
        return df
    
    def prepare_for_dnn(self, df, target_col='label'):
        """
        Prepare data for DNN training (both MLP and CNN-1D)
        
        Steps:
        1. Analyze and drop sparse columns
        2. Drop identifiers and high-cardinality strings
        3. Create minimal indicators
        4. Label encode categorical features
        5. Keep all numeric features
        6. StandardScaler (MANDATORY for DNN)
        """
        print("\n" + "="*70)
        print(f"PREPARING FOR DNN - TARGET: {target_col}")
        print("="*70)
        
        df = df.copy()
        
        # 1. Analyze nulls
        sparse_cols = self.analyze_nulls(df)
        
        # 2. Basic preprocessing (fill nulls)
        df = self.basic_preprocessing(df)
        
        # 3. Create minimal features BEFORE dropping
        df = self.create_minimal_features(df)
        
        # 4. Build comprehensive drop list
        print("\n[STEP 1/6] Building drop list...")
        all_drops = (
            self.config.DROP_IDENTIFIERS +
            self.config.DROP_HIGH_CARDINALITY +
            sparse_cols
        )
        
        # Add opposite target column
        if target_col == 'label':
            all_drops.append('type')
        else:
            all_drops.append('label')
        
        # Remove duplicates and only drop what exists
        all_drops = list(set([col for col in all_drops if col in df.columns]))
        
        print(f"  Dropping {len(all_drops)} columns:")
        print(f"  - Identifiers: {len([c for c in self.config.DROP_IDENTIFIERS if c in all_drops])}")
        print(f"  - High-cardinality: {len([c for c in self.config.DROP_HIGH_CARDINALITY if c in all_drops])}")
        print(f"  - Sparse (>{self.config.NULL_THRESHOLD*100}% null): {len([c for c in sparse_cols if c in all_drops])}")
        
        # 5. Separate features and target
        print("\n[STEP 2/6] Separating features and target...")
        y = df[target_col].copy()
        df_features = df.drop(columns=[target_col] + all_drops, errors='ignore')
        
        print(f"  Features shape after drop: {df_features.shape}")
        print(f"  Target shape: {y.shape}")
        
        # 6. Identify categorical columns to encode
        print("\n[STEP 3/6] Identifying feature types...")
        categorical_cols = [col for col in self.config.CATEGORICAL_TO_ENCODE if col in df_features.columns]
        numeric_cols = df_features.select_dtypes(include=[np.number]).columns.tolist()
        
        print(f"  Categorical (will Label Encode): {len(categorical_cols)} → {categorical_cols}")
        print(f"  Numeric (keep as-is): {len(numeric_cols)}")
        
        # 7. Label encode categorical features
        print("\n[STEP 4/6] Label encoding categorical features...")
        label_encoders = {}
        
        for col in categorical_cols:
            le = LabelEncoder()
            df_features[col] = le.fit_transform(df_features[col].astype(str))
            label_encoders[col] = le
            print(f"  - {col}: {len(le.classes_)} unique values → [0, {len(le.classes_)-1}]")
        
        # 7.5. Handle any remaining non-numeric columns (convert string values like '-' to numeric)
        print("\n[STEP 4.5/6] Cleaning remaining non-numeric values...")
        for col in df_features.columns:
            if df_features[col].dtype == 'object':
                # Try to convert to numeric, replacing invalid values with NaN
                df_features[col] = pd.to_numeric(df_features[col], errors='coerce')
                # Fill NaN with median or 0
                if df_features[col].isna().any():
                    fill_value = df_features[col].median() if not df_features[col].isna().all() else 0
                    df_features[col].fillna(fill_value, inplace=True)
                    print(f"  - {col}: Converted to numeric, filled {df_features[col].isna().sum()} invalid values")
        
        # 8. All features are now numeric
        X = df_features.values.astype(np.float32)
        feature_names = df_features.columns.tolist()
        
        print(f"\n[STEP 5/6] Final feature matrix: {X.shape}")
        print(f"  Data type: {X.dtype}")
        print(f"  Feature names: {len(feature_names)}")
        
        # 9. Verify no NaN or Inf
        print("\n[STEP 6/6] Data integrity check...")
        nan_count = np.isnan(X).sum()
        inf_count = np.isinf(X).sum()
        
        if nan_count > 0:
            print(f"  ⚠ WARNING: {nan_count} NaN values found!")
        else:
            print(f"  ✓ No NaN values")
        
        if inf_count > 0:
            print(f"  ⚠ WARNING: {inf_count} Inf values found!")
        else:
            print(f"  ✓ No Inf values")
        
        return X, y, feature_names, label_encoders
    
    def prepare_binary_classification(self, df):
        """Prepare data for binary classification (Normal vs Attack)"""
        print("\n" + "="*70)
        print("BINARY CLASSIFICATION PIPELINE (DNN)")
        print("="*70)
        
        # Prepare features
        X, y, feature_names, label_encoders = self.prepare_for_dnn(df, target_col='label')
        
        # Train/test split
        print("\n[SPLIT] Train/Test split (stratified)...")
        X_train, X_test, y_train, y_test = train_test_split(
            X, y.values,
            test_size=self.config.TEST_SIZE,
            random_state=self.config.RANDOM_STATE,
            stratify=y
        )
        print(f"  Train: {X_train.shape}, Test: {X_test.shape}")
        print(f"  Class distribution (train): {np.bincount(y_train)}")
        
        # StandardScaler (MANDATORY for DNN)
        print("\n[SCALE] StandardScaler (MANDATORY for DNN convergence)...")
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        print(f"  ✓ Scaled to mean=0, std=1")
        print(f"  Train - mean: {X_train_scaled.mean():.6f}, std: {X_train_scaled.std():.6f}")
        print(f"  Test - mean: {X_test_scaled.mean():.6f}, std: {X_test_scaled.std():.6f}")
        
        # Package artifacts
        artifacts = {
            'X_train': X_train_scaled.astype(np.float32),
            'X_test': X_test_scaled.astype(np.float32),
            'y_train': y_train.astype(np.int32),
            'y_test': y_test.astype(np.int32),
            'scaler': scaler,
            'label_encoders': label_encoders,
            'feature_names': feature_names,
            'metadata': {
                'n_samples_train': len(X_train_scaled),
                'n_samples_test': len(X_test_scaled),
                'n_features': X_train_scaled.shape[1],
                'feature_names': feature_names,
                'test_size': self.config.TEST_SIZE,
                'random_state': self.config.RANDOM_STATE,
                'preprocessing': 'DNN-optimized (MLP/CNN-1D)',
                'encoding': 'Label Encoding',
                'scaling': 'StandardScaler',
                'class_balance_train': {
                    'normal': int(np.sum(y_train == 0)),
                    'attack': int(np.sum(y_train == 1))
                }
            }
        }
        
        print(f"\n✓ Binary preprocessing completed for DNN")
        print(f"  Final shape: {X_train_scaled.shape}")
        print(f"  Data type: {X_train_scaled.dtype} (optimized for TensorFlow)")
        
        return artifacts
    
    def prepare_multiclass_classification(self, df):
        """Prepare data for multi-class classification (Attack types)"""
        print("\n" + "="*70)
        print("MULTI-CLASS CLASSIFICATION PIPELINE (DNN)")
        print("="*70)
        
        # Prepare features
        X, y, feature_names, label_encoders = self.prepare_for_dnn(df, target_col='type')
        
        # Encode target labels
        print("\n[TARGET] Encoding target labels...")
        le_target = LabelEncoder()
        y_encoded = le_target.fit_transform(y)
        num_classes = len(le_target.classes_)
        
        print(f"  Classes: {num_classes}")
        print(f"  Class names: {list(le_target.classes_)}")
        
        # Train/test split
        print("\n[SPLIT] Train/Test split (stratified)...")
        X_train, X_test, y_train, y_test = train_test_split(
            X, y_encoded,
            test_size=self.config.TEST_SIZE,
            random_state=self.config.RANDOM_STATE,
            stratify=y_encoded
        )
        print(f"  Train: {X_train.shape}, Test: {X_test.shape}")
        
        # StandardScaler (MANDATORY for DNN)
        print("\n[SCALE] StandardScaler (MANDATORY for DNN convergence)...")
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        print(f"  ✓ Scaled to mean=0, std=1")
        
        # Package artifacts
        artifacts = {
            'X_train': X_train_scaled.astype(np.float32),
            'X_test': X_test_scaled.astype(np.float32),
            'y_train': y_train.astype(np.int32),
            'y_test': y_test.astype(np.int32),
            'scaler': scaler,
            'target_encoder': le_target,
            'label_encoders': label_encoders,
            'feature_names': feature_names,
            'num_classes': num_classes,
            'class_names': list(le_target.classes_),
            'metadata': {
                'n_samples_train': len(X_train_scaled),
                'n_samples_test': len(X_test_scaled),
                'n_features': X_train_scaled.shape[1],
                'feature_names': feature_names,
                'num_classes': num_classes,
                'test_size': self.config.TEST_SIZE,
                'random_state': self.config.RANDOM_STATE,
                'preprocessing': 'DNN-optimized (MLP/CNN-1D)',
                'encoding': 'Label Encoding',
                'scaling': 'StandardScaler',
                'class_distribution_train': {
                    name: int(np.sum(y_train == i))
                    for i, name in enumerate(le_target.classes_)
                }
            }
        }
        
        print(f"\n✓ Multi-class preprocessing completed for DNN")
        print(f"  Final shape: {X_train_scaled.shape}")
        print(f"  Data type: {X_train_scaled.dtype} (optimized for TensorFlow)")
        
        return artifacts
    
    def save_artifacts(self, artifacts, filename):
        """Save preprocessed artifacts to disk"""
        filepath = self.config.OUTPUT_DIR / filename
        with open(filepath, 'wb') as f:
            pickle.dump(artifacts, f, protocol=pickle.HIGHEST_PROTOCOL)
        
        size_mb = filepath.stat().st_size / (1024 * 1024)
        print(f"\n💾 Saved: {filepath}")
        print(f"   Size: {size_mb:.2f} MB")
        
        return filepath
    
    def run(self, mode='full'):
        """Run DNN preprocessing pipeline"""
        print("\n" + "="*70)
        print("DNN PREPROCESSING PIPELINE - MLP/CNN-1D Optimized")
        print("="*70)
        print(f"Mode: {mode}")
        print(f"Output: {self.config.OUTPUT_DIR}")
        print(f"\n⚡ Optimizations:")
        print(f"  - Aggressive dropping of high-cardinality strings")
        print(f"  - Label Encoding (not OneHot) for categorical")
        print(f"  - Minimal feature engineering (fair comparison)")
        print(f"  - StandardScaler mandatory")
        print(f"  - Float32 precision (TensorFlow optimized)")
        
        total_start = time.time()
        
        # Load data
        df = self.load_data()
        
        results = {}
        
        # Binary classification
        if mode in ['full', 'binary']:
            print("\n" + "🔵 PROCESSING BINARY CLASSIFICATION (DNN)...")
            binary_artifacts = self.prepare_binary_classification(df)
            binary_path = self.save_artifacts(binary_artifacts, 'binary_dnn_preprocessed.pkl')
            results['binary'] = binary_path
        
        # Multi-class classification
        if mode in ['full', 'multi']:
            print("\n" + "🟢 PROCESSING MULTI-CLASS CLASSIFICATION (DNN)...")
            multi_artifacts = self.prepare_multiclass_classification(df)
            multi_path = self.save_artifacts(multi_artifacts, 'multiclass_dnn_preprocessed.pkl')
            results['multi'] = multi_path
        
        total_time = time.time() - total_start
        
        print("\n" + "="*70)
        print("✅ DNN PREPROCESSING COMPLETED")
        print("="*70)
        print(f"Total time: {total_time:.2f}s ({total_time/60:.2f} minutes)")
        print(f"\nSaved artifacts:")
        for key, path in results.items():
            print(f"  - {key}: {path}")
        
        print("\n📖 Usage in notebooks (MLP/CNN-1D):")
        print("  >>> import pickle")
        print("  >>> with open('processed_artifacts/binary_dnn_preprocessed.pkl', 'rb') as f:")
        print("  >>>     artifacts = pickle.load(f)")
        print("  >>> X_train = artifacts['X_train']  # Already scaled!")
        print("  >>> X_test = artifacts['X_test']")
        print("  >>> y_train = artifacts['y_train']")
        print("  >>> y_test = artifacts['y_test']")
        print("  >>> # Ready for model.fit(X_train, y_train)")
        
        return results


def load_dnn_preprocessed_data(artifact_type='binary'):
    """
    Utility function to load DNN-preprocessed data in notebooks
    
    Args:
        artifact_type: 'binary' or 'multiclass'
    
    Returns:
        dict: Preprocessed artifacts ready for MLP/CNN-1D
    """
    base_path = Path("/home/elnoersan/Skripsi/Paper/NotebookTODO/EDA/processed_artifacts")
    filepath = base_path / f"{artifact_type}_dnn_preprocessed.pkl"
    
    if not filepath.exists():
        raise FileNotFoundError(
            f"Artifact not found: {filepath}\n"
            "Run DNN preprocessing pipeline first:\n"
            "  python preprocessing_pipeline_dnn.py --mode binary"
        )
    
    with open(filepath, 'rb') as f:
        artifacts = pickle.load(f)
    
    print(f"✓ Loaded {artifact_type} DNN artifacts from {filepath}")
    print(f"  Train samples: {artifacts['metadata']['n_samples_train']:,}")
    print(f"  Test samples: {artifacts['metadata']['n_samples_test']:,}")
    print(f"  Features: {artifacts['metadata']['n_features']}")
    print(f"  Data type: {artifacts['X_train'].dtype}")
    print(f"  Preprocessing: {artifacts['metadata']['preprocessing']}")
    
    return artifacts


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Preprocess TON_IoT dataset for Deep Learning (MLP/CNN-1D)"
    )
    parser.add_argument(
        '--mode',
        type=str,
        choices=['full', 'binary', 'multi'],
        default='full',
        help="Preprocessing mode: 'full' (both), 'binary', or 'multi'"
    )
    
    args = parser.parse_args()
    
    # Run DNN preprocessing
    config = DNNPreprocessingConfig()
    preprocessor = DNNPreprocessor(config)
    preprocessor.run(mode=args.mode)
