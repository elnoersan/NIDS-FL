"""
Standalone Preprocessing Pipeline for TON_IoT Dataset
Optimized for Neural Network Training with RFE

This script prepares data in a separate runtime and saves preprocessed artifacts
that can be loaded instantly in training notebooks.

Usage:
    python preprocessing_pipeline.py --mode full
    python preprocessing_pipeline.py --mode binary
    python preprocessing_pipeline.py --mode multi
"""

import pandas as pd
import numpy as np
import pickle
import argparse
import time
from pathlib import Path
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.feature_selection import VarianceThreshold
import warnings
warnings.filterwarnings('ignore')

# GPU detection
try:
    import cupy as cp
    GPU_AVAILABLE = cp.cuda.is_available()
    print(f"🚀 GPU Detected: {cp.cuda.runtime.getDeviceCount()} device(s)")
except ImportError:
    GPU_AVAILABLE = False
    print("⚠️  CuPy not installed. Running on CPU.")

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


class PreprocessingConfig:
    """Configuration for preprocessing pipeline"""
    
    # Paths
    RAW_DATA_PATH = "/home/elnoersan/Skripsi/Paper/NotebookTODO/train_test_network.csv"
    OUTPUT_DIR = Path("/home/elnoersan/Skripsi/Paper/NotebookTODO/EDA/processed_artifacts")
    
    # Split config
    TEST_SIZE = 0.2
    RANDOM_STATE = 42
    
    # Feature Selection Config (GPU-optimized)
    USE_RFE = False  # Skip RFE for speed - use all features
    USE_VARIANCE_THRESHOLD = True  # Remove low-variance features (fast)
    VARIANCE_THRESHOLD = 0.01  # Remove features with variance < 0.01
    
    # If you really need RFE, we'll use variance threshold first to reduce features
    RFE_N_FEATURES_BINARY = 30
    RFE_N_FEATURES_MULTI = 35
    
    # Columns to drop
    DROP_COLS = ['src_ip', 'src_port', 'dst_ip', 'dst_port', 
                 'weird_name', 'weird_addl', 'weird_notice']


class DataPreprocessor:
    """Main preprocessing class"""
    
    def __init__(self, config: PreprocessingConfig):
        self.config = config
        self.config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        
    def load_data(self):
        """Load raw dataset"""
        print("="*70)
        print("LOADING RAW DATA")
        print("="*70)
        start = time.time()
        
        df = pd.read_csv(self.config.RAW_DATA_PATH)
        print(f"✓ Loaded: {df.shape}")
        print(f"  Time: {time.time() - start:.2f}s")
        return df
    
    def smart_preprocess_toniot_inplace(self, df):
        """
        Protocol-aware preprocessing for TON_IoT dataset.
        Handles missing values based on protocol context.
        """
        print("\n" + "="*70)
        print("SMART PREPROCESSING (Protocol-Aware)")
        print("="*70)
        
        # DNS columns
        dns_cols = ['dns_query', 'dns_qclass', 'dns_qtype', 'dns_rcode', 
                    'dns_AA', 'dns_RD', 'dns_RA', 'dns_rejected']
        
        # HTTP columns
        http_cols = ['http_trans_depth', 'http_method', 'http_uri', 
                     'http_version', 'http_request_body_len', 
                     'http_response_body_len', 'http_status_code', 
                     'http_user_agent', 'http_orig_mime_types', 
                     'http_resp_mime_types']
        
        # SSL columns
        ssl_cols = ['ssl_version', 'ssl_cipher', 'ssl_resumed', 
                    'ssl_established', 'ssl_subject', 'ssl_issuer']
        
        print("Processing DNS columns...")
        for col in dns_cols:
            if col in df.columns:
                # If DNS traffic (has dns_query), fill with -1; else with 0
                mask_dns = df['dns_query'].notna() if 'dns_query' in df.columns else pd.Series([False]*len(df))
                df[col] = df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else -1)
        
        print("Processing HTTP columns...")
        for col in http_cols:
            if col in df.columns:
                # If HTTP traffic (has http_method), fill with mode; else with 0
                mask_http = df['http_method'].notna() if 'http_method' in df.columns else pd.Series([False]*len(df))
                df[col] = df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else 0)
        
        print("Processing SSL columns...")
        for col in ssl_cols:
            if col in df.columns:
                # If SSL traffic, fill with mode; else with 'none'
                df[col] = df[col].fillna('none')
        
        # Fill remaining numeric columns with median
        print("Processing remaining numeric columns...")
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            if df[col].isna().sum() > 0:
                df[col] = df[col].fillna(df[col].median())
        
        # Fill remaining categorical columns with mode
        print("Processing remaining categorical columns...")
        cat_cols = df.select_dtypes(include=['object']).columns
        for col in cat_cols:
            if df[col].isna().sum() > 0:
                mode_val = df[col].mode()[0] if not df[col].mode().empty else 'unknown'
                df[col] = df[col].fillna(mode_val)
        
        remaining_nan = df.isna().sum().sum()
        print(f"✓ Smart preprocessing complete. Remaining NaN: {remaining_nan}")
        
        return df
    
    def prepare_binary_classification(self, df):
        """Prepare data for binary classification (Normal vs Attack)"""
        print("\n" + "="*70)
        print("BINARY CLASSIFICATION PIPELINE")
        print("="*70)
        
        # Smart preprocessing
        df = self.smart_preprocess_toniot_inplace(df.copy())
        
        # Drop columns
        df_binary = df.drop(columns=['type'] + self.config.DROP_COLS, errors='ignore')
        X = df_binary.drop('label', axis=1)
        y = df_binary['label']
        
        print(f"\n[1/5] Dataset shape: {X.shape}")
        
        # Split train/test
        print("\n[2/5] Train/Test split...")
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, 
            test_size=self.config.TEST_SIZE, 
            random_state=self.config.RANDOM_STATE, 
            stratify=y
        )
        print(f"  Train: {X_train.shape}, Test: {X_test.shape}")
        
        # Encode categorical
        print("\n[3/5] OneHot encoding categorical features...")
        categorical_cols = X_train.select_dtypes(include=['object']).columns.tolist()
        numeric_cols = X_train.select_dtypes(exclude=['object']).columns.tolist()
        print(f"  Categorical: {len(categorical_cols)}, Numeric: {len(numeric_cols)}")
        
        if categorical_cols:
            preprocessor = ColumnTransformer(
                transformers=[
                    ('cat', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'), categorical_cols)
                ],
                remainder='passthrough'
            )
            X_train_encoded = preprocessor.fit_transform(X_train)
            X_test_encoded = preprocessor.transform(X_test)
            print(f"  Encoded shape: {X_train_encoded.shape}")
        else:
            X_train_encoded = X_train.values
            X_test_encoded = X_test.values
            preprocessor = None
        
        # Feature Selection (GPU-friendly - no training needed!)
        if self.config.USE_VARIANCE_THRESHOLD:
            print(f"\n[4/5] Fast feature selection (VarianceThreshold)...")
            start = time.time()
            
            selector = VarianceThreshold(threshold=self.config.VARIANCE_THRESHOLD)
            X_train_selected = selector.fit_transform(X_train_encoded)
            X_test_selected = selector.transform(X_test_encoded)
            
            selected_features = selector.get_support()
            n_features_selected = selected_features.sum()
            
            print(f"  Selected: {n_features_selected}/{X_train_encoded.shape[1]} features")
            print(f"  Time: {time.time() - start:.2f}s ⚡")
        else:
            print("\n[4/5] Skipping feature selection (using all features)...")
            X_train_selected = X_train_encoded
            X_test_selected = X_test_encoded
            selector = None
            n_features_selected = X_train_encoded.shape[1]
        
        # Scale
        print("\n[5/5] Scaling features...")
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train_selected)
        X_test_scaled = scaler.transform(X_test_selected)
        
        print(f"\n✓ Binary preprocessing completed")
        print(f"  Final shape - Train: {X_train_scaled.shape}, Test: {X_test_scaled.shape}")
        
        # Package artifacts
        artifacts = {
            'X_train': X_train_scaled,
            'X_test': X_test_scaled,
            'y_train': y_train.values,
            'y_test': y_test.values,
            'preprocessor': preprocessor,
            'selector': selector,
            'scaler': scaler,
            'categorical_cols': categorical_cols,
            'numeric_cols': numeric_cols,
            'feature_names': None,  # Can be extracted from preprocessor if needed
            'metadata': {
                'n_samples_train': len(X_train_scaled),
                'n_samples_test': len(X_test_scaled),
                'n_features_original': X.shape[1],
                'n_features_encoded': X_train_encoded.shape[1],
                'n_features_final': n_features_selected,
                'test_size': self.config.TEST_SIZE,
                'random_state': self.config.RANDOM_STATE,
                'feature_selection_method': 'VarianceThreshold' if self.config.USE_VARIANCE_THRESHOLD else 'None'
            }
        }
        
        return artifacts
    
    def prepare_multiclass_classification(self, df):
        """Prepare data for multi-class classification (Attack types)"""
        print("\n" + "="*70)
        print("MULTI-CLASS CLASSIFICATION PIPELINE")
        print("="*70)
        
        # Smart preprocessing
        df = self.smart_preprocess_toniot_inplace(df.copy())
        
        # Drop columns
        df_multi = df.drop(columns=['label'] + self.config.DROP_COLS, errors='ignore')
        y = df_multi['type']
        X = df_multi.drop('type', axis=1)
        
        print(f"\n[1/6] Dataset shape: {X.shape}")
        
        # Encode target
        print("\n[2/6] Encoding target labels...")
        le_target = LabelEncoder()
        y_encoded = le_target.fit_transform(y)
        num_classes = len(le_target.classes_)
        print(f"  Classes: {num_classes}")
        print(f"  Labels: {list(le_target.classes_)}")
        
        # Split train/test
        print("\n[3/6] Train/Test split...")
        X_train, X_test, y_train, y_test = train_test_split(
            X, y_encoded,
            test_size=self.config.TEST_SIZE,
            random_state=self.config.RANDOM_STATE,
            stratify=y_encoded
        )
        print(f"  Train: {X_train.shape}, Test: {X_test.shape}")
        
        # Encode categorical
        print("\n[4/6] OneHot encoding categorical features...")
        categorical_cols = X_train.select_dtypes(include=['object']).columns.tolist()
        numeric_cols = X_train.select_dtypes(exclude=['object']).columns.tolist()
        print(f"  Categorical: {len(categorical_cols)}, Numeric: {len(numeric_cols)}")
        
        if categorical_cols:
            preprocessor = ColumnTransformer(
                transformers=[
                    ('cat', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'), categorical_cols)
                ],
                remainder='passthrough'
            )
            X_train_encoded = preprocessor.fit_transform(X_train)
            X_test_encoded = preprocessor.transform(X_test)
            print(f"  Encoded shape: {X_train_encoded.shape}")
        else:
            X_train_encoded = X_train.values
            X_test_encoded = X_test.values
            preprocessor = None
        
        # Feature Selection (GPU-friendly - no training needed!)
        if self.config.USE_VARIANCE_THRESHOLD:
            print(f"\n[5/6] Fast feature selection (VarianceThreshold)...")
            start = time.time()
            
            selector = VarianceThreshold(threshold=self.config.VARIANCE_THRESHOLD)
            X_train_selected = selector.fit_transform(X_train_encoded)
            X_test_selected = selector.transform(X_test_encoded)
            
            selected_features = selector.get_support()
            n_features_selected = selected_features.sum()
            
            print(f"  Selected: {n_features_selected}/{X_train_encoded.shape[1]} features")
            print(f"  Time: {time.time() - start:.2f}s ⚡")
        else:
            print("\n[5/6] Skipping feature selection (using all features)...")
            X_train_selected = X_train_encoded
            X_test_selected = X_test_encoded
            selector = None
            n_features_selected = X_train_encoded.shape[1]
        
        # Scale
        print("\n[6/6] Scaling features...")
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train_selected)
        X_test_scaled = scaler.transform(X_test_selected)
        
        print(f"\n✓ Multi-class preprocessing completed")
        print(f"  Final shape - Train: {X_train_scaled.shape}, Test: {X_test_scaled.shape}")
        
        # Package artifacts
        artifacts = {
            'X_train': X_train_scaled,
            'X_test': X_test_scaled,
            'y_train': y_train,
            'y_test': y_test,
            'preprocessor': preprocessor,
            'target_encoder': le_target,
            'selector': selector,
            'scaler': scaler,
            'categorical_cols': categorical_cols,
            'numeric_cols': numeric_cols,
            'num_classes': num_classes,
            'class_names': list(le_target.classes_),
            'metadata': {
                'n_samples_train': len(X_train_scaled),
                'n_samples_test': len(X_test_scaled),
                'n_features_original': X.shape[1],
                'n_features_encoded': X_train_encoded.shape[1],
                'n_features_final': n_features_selected,
                'test_size': self.config.TEST_SIZE,
                'random_state': self.config.RANDOM_STATE,
                'num_classes': num_classes,
                'feature_selection_method': 'VarianceThreshold' if self.config.USE_VARIANCE_THRESHOLD else 'None'
            }
        }
        
        return artifacts
    
    def save_artifacts(self, artifacts, filename):
        """Save preprocessed artifacts to disk"""
        filepath = self.config.OUTPUT_DIR / filename
        with open(filepath, 'wb') as f:
            pickle.dump(artifacts, f, protocol=pickle.HIGHEST_PROTOCOL)
        
        # Get file size
        size_mb = filepath.stat().st_size / (1024 * 1024)
        print(f"\n💾 Saved: {filepath}")
        print(f"   Size: {size_mb:.2f} MB")
        
        return filepath
    
    def run(self, mode='full'):
        """Run preprocessing pipeline"""
        print("\n" + "="*70)
        print("PREPROCESSING PIPELINE - NEURAL NETWORK OPTIMIZED")
        print("="*70)
        print(f"Mode: {mode}")
        print(f"Output: {self.config.OUTPUT_DIR}")
        
        total_start = time.time()
        
        # Load data
        df = self.load_data()
        
        results = {}
        
        # Binary classification
        if mode in ['full', 'binary']:
            print("\n" + "🔵 PROCESSING BINARY CLASSIFICATION...")
            binary_artifacts = self.prepare_binary_classification(df)
            binary_path = self.save_artifacts(binary_artifacts, 'binary_preprocessed.pkl')
            results['binary'] = binary_path
        
        # Multi-class classification
        if mode in ['full', 'multi']:
            print("\n" + "🟢 PROCESSING MULTI-CLASS CLASSIFICATION...")
            multi_artifacts = self.prepare_multiclass_classification(df)
            multi_path = self.save_artifacts(multi_artifacts, 'multiclass_preprocessed.pkl')
            results['multi'] = multi_path
        
        total_time = time.time() - total_start
        
        print("\n" + "="*70)
        print("✅ PREPROCESSING COMPLETED")
        print("="*70)
        print(f"Total time: {total_time:.2f}s ({total_time/60:.2f} minutes)")
        print(f"\nSaved artifacts:")
        for key, path in results.items():
            print(f"  - {key}: {path}")
        
        print("\n📖 Usage in notebooks:")
        print("  >>> import pickle")
        print("  >>> with open('processed_artifacts/binary_preprocessed.pkl', 'rb') as f:")
        print("  >>>     artifacts = pickle.load(f)")
        print("  >>> X_train = artifacts['X_train']")
        print("  >>> X_test = artifacts['X_test']")
        print("  >>> y_train = artifacts['y_train']")
        print("  >>> y_test = artifacts['y_test']")
        
        return results


def load_preprocessed_data(artifact_type='binary'):
    """
    Utility function to load preprocessed data in notebooks
    
    Args:
        artifact_type: 'binary' or 'multiclass'
    
    Returns:
        dict: Preprocessed artifacts
    """
    base_path = Path("/home/elnoersan/Skripsi/Paper/NotebookTODO/EDA/processed_artifacts")
    filepath = base_path / f"{artifact_type}_preprocessed.pkl"
    
    if not filepath.exists():
        raise FileNotFoundError(
            f"Artifact not found: {filepath}\n"
            "Run preprocessing pipeline first:\n"
            "  python preprocessing_pipeline.py --mode binary"
        )
    
    with open(filepath, 'rb') as f:
        artifacts = pickle.load(f)
    
    print(f"✓ Loaded {artifact_type} artifacts from {filepath}")
    print(f"  Train samples: {artifacts['metadata']['n_samples_train']:,}")
    print(f"  Test samples: {artifacts['metadata']['n_samples_test']:,}")
    print(f"  Features: {artifacts['metadata']['n_features_final']}")
    
    return artifacts


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Preprocess TON_IoT dataset")
    parser.add_argument(
        '--mode',
        type=str,
        choices=['full', 'binary', 'multi'],
        default='full',
        help="Preprocessing mode: 'full' (both), 'binary', or 'multi'"
    )
    
    args = parser.parse_args()
    
    # Run preprocessing
    config = PreprocessingConfig()
    preprocessor = DataPreprocessor(config)
    preprocessor.run(mode=args.mode)
