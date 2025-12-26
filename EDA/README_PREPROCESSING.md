# TON_IoT Preprocessing Pipeline

## Overview
Standalone preprocessing pipeline untuk TON_IoT dataset yang bisa dijalankan sekali dan hasilnya di-reuse berkali-kali.

**Time Saving:** ~5-10 menit per notebook run → **<5 detik** untuk load preprocessed data

## Files

- `preprocessing_pipeline.py` - Main preprocessing script
- `load_preprocessed_example.ipynb` - Contoh cara load preprocessed data
- `processed_artifacts/` - Output directory (akan dibuat otomatis)

## Quick Start

### 1. Run Preprocessing (Sekali saja)

```bash
cd /home/elnoersan/Skripsi/Paper/NotebookTODO/EDA

# Full preprocessing (binary + multi-class)
python preprocessing_pipeline.py --mode full

# Atau hanya binary
python preprocessing_pipeline.py --mode binary

# Atau hanya multi-class
python preprocessing_pipeline.py --mode multi
```

**Waktu eksekusi:** ~3-5 menit (tergantung RFE)

### 2. Load in Notebook

```python
import pickle

# Load binary classification data
with open('processed_artifacts/binary_preprocessed.pkl', 'rb') as f:
    binary_data = pickle.load(f)

X_train_bin = binary_data['X_train']
X_test_bin = binary_data['X_test']
y_train_bin = binary_data['y_train']
y_test_bin = binary_data['y_test']

print(f"Binary - Train: {X_train_bin.shape}, Test: {X_test_bin.shape}")
```

```python
# Load multi-class classification data
with open('processed_artifacts/multiclass_preprocessed.pkl', 'rb') as f:
    multi_data = pickle.load(f)

X_train_multi = multi_data['X_train']
X_test_multi = multi_data['X_test']
y_train_multi = multi_data['y_train']
y_test_multi = multi_data['y_test']
num_classes = multi_data['num_classes']

print(f"Multi-class - Train: {X_train_multi.shape}, Test: {X_test_multi.shape}")
print(f"Classes: {num_classes}")
```

## What's Inside?

### Preprocessing Steps

1. **Smart Preprocessing** (Protocol-aware)
   - DNS columns: Fill berdasarkan DNS traffic context
   - HTTP columns: Fill berdasarkan HTTP traffic context
   - SSL columns: Fill dengan 'none' untuk non-SSL traffic
   - Numeric: Median imputation
   - Categorical: Mode imputation

2. **Train/Test Split** (80/20, stratified)
   - Prevents data leakage
   - Encoding dilakukan SETELAH split

3. **OneHot Encoding**
   - Categorical features → One-hot vectors
   - `handle_unknown='ignore'` untuk unseen categories

4. **RFE (Recursive Feature Elimination)**
   - Binary: 30 features terbaik
   - Multi-class: 35 features terbaik
   - Estimator: RandomForestClassifier (optimized for speed)

5. **Standardization**
   - StandardScaler fit on training data
   - Transform both train & test

### Output Files

#### `binary_preprocessed.pkl`
```python
{
    'X_train': ndarray (168834, 30),
    'X_test': ndarray (42209, 30),
    'y_train': ndarray (168834,),
    'y_test': ndarray (42209,),
    'selected_features': list,
    'metadata': dict
}
```

#### `multiclass_preprocessed.pkl`
```python
{
    'X_train': ndarray (168834, 35),
    'X_test': ndarray (42209, 35),
    'y_train': ndarray (168834,),
    'y_test': ndarray (42209,),
    'num_classes': int,
    'class_names': list,
    'selected_features': list,
    'metadata': dict
}
```

#### `preprocessors.pkl`
```python
{
    'binary': {
        'encoder': ColumnTransformer,
        'rfe': RFE,
        'scaler': StandardScaler
    },
    'multiclass': {
        'label_encoder': LabelEncoder,
        'encoder': ColumnTransformer,
        'rfe': RFE,
        'scaler': StandardScaler
    }
}
```

## Integration with Existing Notebooks

### Before (5-10 menit preprocessing)
```python
# BAGIAN 3: PREPARASI DATA
df = pd.read_csv(...)
df = smart_preprocess_toniot_inplace(df)
X_train, X_test = ...
# ... 200+ lines of preprocessing code
```

### After (<5 detik load)
```python
# BAGIAN 3: LOAD PREPROCESSED DATA
import pickle

with open('processed_artifacts/binary_preprocessed.pkl', 'rb') as f:
    binary_data = pickle.load(f)

X_train_bin_scaled = binary_data['X_train']
X_test_bin_scaled = binary_data['X_test']
y_train_bin = binary_data['y_train']
y_test_bin = binary_data['y_test']

with open('processed_artifacts/multiclass_preprocessed.pkl', 'rb') as f:
    multi_data = pickle.load(f)

X_train_multi_scaled = multi_data['X_train']
X_test_multi_scaled = multi_data['X_test']
y_train_multi = multi_data['y_train']
y_test_multi = multi_data['y_test']
```

## Configuration

Edit `PreprocessingConfig` class in `preprocessing_pipeline.py`:

```python
class PreprocessingConfig:
    RAW_DATA_PATH = "/path/to/data.csv"
    OUTPUT_DIR = Path("/output/directory")
    
    TEST_SIZE = 0.2
    RANDOM_STATE = 42
    
    RFE_N_FEATURES_BINARY = 30
    RFE_N_FEATURES_MULTI = 35
    # ... dll
```

## Utility Functions

```python
from preprocessing_pipeline import load_preprocessed_data

# Load binary data
binary_data = load_preprocessed_data('binary')

# Load multi-class data
multi_data = load_preprocessed_data('multiclass')
```

## Performance Comparison

| Task | Before | After |
|------|--------|-------|
| Load data | 1-2s | 0.5s |
| Smart preprocessing | 30-60s | - |
| Train/test split | 1s | - |
| OneHot encoding | 60-90s | - |
| RFE | 180-300s | - |
| Scaling | 1-2s | - |
| **TOTAL** | **~5-10 min** | **<5s** |

## Troubleshooting

### Error: FileNotFoundError
Pastikan path ke raw data benar di `PreprocessingConfig.RAW_DATA_PATH`

### Error: Memory error during RFE
Reduce `RFE_ESTIMATOR` parameters:
```python
RFE_ESTIMATOR = RandomForestClassifier(
    n_estimators=20,  # Reduce from 50
    max_depth=3,      # Reduce from 5
    max_samples=0.2   # Reduce from 0.3
)
```

### RFE terlalu lama
Option 1: Skip RFE (comment out RFE steps, use all encoded features)
Option 2: Use SelectKBest instead of RFE

## Notes

- **Data Leakage Prevention:** Encoding fit HANYA pada training data
- **Reproducibility:** `random_state=42` di semua operasi
- **Scalability:** RFE di-optimize dengan subsampling (`max_samples`)
- **Compatibility:** Compatible dengan Flower FL framework

## Next Steps

1. ✅ Run preprocessing once
2. ✅ Verify output files exist
3. ✅ Test loading in notebook
4. Integrate into FL training notebooks
5. Update grid search scripts to use preprocessed data

## Contact

Jika ada issue atau pertanyaan, check `load_preprocessed_example.ipynb` untuk contoh lengkap.
