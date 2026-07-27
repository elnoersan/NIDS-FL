# Perbandingan Preprocessing Pipelines: Traditional ML vs Deep Learning

## Overview

Repositori ini memiliki **2 preprocessing pipelines terpisah** dengan tujuan berbeda:

| Pipeline | Target Models | File | Philosophy |
|----------|---------------|------|------------|
| **Traditional ML** | Random Forest, XGBoost, SVM, Gradient Boosting | `preprocessing_pipeline.py` | Feature engineering maksimal, alignment dengan TON_IoT fundamentals |
| **Deep Learning** | MLP, CNN-1D | `preprocessing_pipeline_dnn.py` | Feature engineering minimal, netral untuk fair comparison |

---

## ⚖️ Mengapa Harus Terpisah?

### **Traditional ML Pipeline** (`preprocessing_pipeline.py`)
**Tujuan:** Research & alignment dengan TON_IoT dataset paper

**Karakteristik:**
- ✅ **Feature engineering ekstensif:**
  - Port categories (well_known/registered/ephemeral)
  - Temporal features (hour_of_day, day_of_week, time_bin)
  - Connection state patterns (rejected/incomplete/established)
  - Protocol indicators (DNS/HTTP/SSL flags)
  - Violation indicators
- ✅ **Mempertahankan violation features** (weird_name, weird_addl, weird_notice)
- ✅ **OneHot encoding** untuk categorical
- ✅ **VarianceThreshold** feature selection
- ✅ **Validasi komprehensif** (5-step validation)

**Output:** ~100-200 features (tergantung OneHot expansion)

**Cocok untuk:**
- Random Forest (suka banyak fitur engineered)
- XGBoost (suka fitur eksplisit)
- Traditional ML algorithms yang butuh human domain knowledge

---

### **Deep Learning Pipeline** (`preprocessing_pipeline_dnn.py`)
**Tujuan:** Fair comparison MLP vs CNN-1D pada dataset kecil

**Karakteristik:**
- ✅ **Feature engineering MINIMAL:**
  - Hanya 7 simple binary indicators:
    - `has_dns_features`, `has_http_features`, `has_ssl_features`
    - `src_is_service_port`, `dst_is_service_port`, `dst_is_web_service`
    - `is_rejected_conn`, `is_established_conn`
- ✅ **Drop AGRESIF high-cardinality strings** (dns_query, http_uri, dll)
- ✅ **Label Encoding** (bukan OneHot) untuk categorical
- ✅ **TIDAK ada** temporal features (bukan time-series model)
- ✅ **TIDAK ada** port categories engineering
- ✅ **StandardScaler MANDATORY**
- ✅ **Float32 precision** (TensorFlow optimized)

**Output:** ~20-30 features (compact, numeric only)

**Cocok untuk:**
- MLP (flat feature vector, let model learn)
- CNN-1D (local patterns from sequence)
- Small dataset (~211K rows)

---

## 📊 Perbandingan Detail

### 1. **Feature Dropping Strategy**

| Feature Type | Traditional ML | Deep Learning | Alasan |
|--------------|----------------|---------------|--------|
| `src_ip`, `dst_ip` | ✅ DROP | ✅ DROP | Per paper Moustafa (Section 6.1) |
| `src_port`, `dst_port` (raw) | ✅ DROP + Engineer categories | ✅ DROP + Simple indicator | Traditional ML: Butuh categories. DNN: Simple indicator cukup |
| `ts` (timestamp) | ✅ DROP + Engineer temporal | ✅ DROP (no temporal) | Traditional ML: Temporal patterns penting. DNN: Bukan time-series model |
| `dns_query` | ❌ KEEP + Fill | ✅ DROP | Traditional ML: Bisa di-encode. DNN: High-cardinality = disaster |
| `http_uri` | ❌ KEEP + Fill | ✅ DROP | High-cardinality strings |
| `http_user_agent` | ❌ KEEP + Fill | ✅ DROP | High-cardinality strings |
| `weird_name/addl/notice` | ❌ KEEP + Engineer | ✅ DROP | Traditional ML: Important features. DNN: High-cardinality |
| `ssl_subject/issuer` | ❌ KEEP + Fill | ✅ DROP | Text features |

### 2. **Feature Engineering**

| Engineering Type | Traditional ML | Deep Learning |
|------------------|----------------|---------------|
| **Port Categories** | ✅ 3 categories (well_known/registered/ephemeral) | ❌ Simple binary (service_port yes/no) |
| **Temporal Features** | ✅ 5 features (hour, day, weekend, night, time_bin) | ❌ TIDAK ADA (bukan time-series) |
| **Connection State** | ✅ 4 categories (rejected/incomplete/established/other) | ✅ 2 simple flags (rejected/established) |
| **Protocol Indicators** | ✅ 3 flags + validation | ✅ 3 simple flags |
| **Violation Engineering** | ✅ has_violation + is_notice | ❌ TIDAK ADA (dropped) |

### 3. **Encoding Strategy**

| Aspect | Traditional ML | Deep Learning |
|--------|----------------|---------------|
| **Categorical Encoding** | OneHot Encoding | Label Encoding |
| **Pros** | Trees suka sparse features | Compact, no dimension explosion |
| **Cons** | Dimensi bisa explode | Assumes ordinal relationship |
| **Result Dimensi** | 100-200 features | 20-30 features |

### 4. **Scaling**

| Pipeline | Scaling Method | Alasan |
|----------|----------------|--------|
| Traditional ML | StandardScaler | Optional (trees don't need, but we do it) |
| Deep Learning | StandardScaler **MANDATORY** | Gradient descent requires normalized input |

### 5. **Output Format**

| Aspect | Traditional ML | Deep Learning |
|--------|----------------|---------------|
| **File Name** | `binary_preprocessed.pkl` | `binary_dnn_preprocessed.pkl` |
| **Data Type** | `float64` (default) | `float32` (TensorFlow optimized) |
| **Shape (approx)** | (168K, 150+) | (168K, 25) |
| **Memory** | ~200 MB | ~50 MB |

---

## 🎯 Kapan Pakai Yang Mana?

### **Gunakan Traditional ML Pipeline** (`preprocessing_pipeline.py`) jika:
- ✅ Training **Random Forest, XGBoost, Gradient Boosting**
- ✅ Butuh **interpretability** tinggi (lihat feature importance)
- ✅ Ingin **alignment dengan TON_IoT dataset paper**
- ✅ Dataset cukup besar (model bisa handle banyak fitur)
- ✅ Riset paper yang fokus pada **feature engineering**

### **Gunakan Deep Learning Pipeline** (`preprocessing_pipeline_dnn.py`) jika:
- ✅ Training **MLP atau CNN-1D**
- ✅ Ingin **fair comparison** antara MLP vs CNN-1D
- ✅ Dataset kecil (~211K rows)
- ✅ Ingin **let model learn** representations sendiri
- ✅ Riset paper yang fokus pada **model architecture comparison**

---

## 📖 Usage Examples

### **Traditional ML Pipeline**

```bash
# Preprocess untuk Traditional ML
python preprocessing_pipeline.py --mode binary

# Load dalam notebook
import pickle
with open('processed_artifacts/binary_preprocessed.pkl', 'rb') as f:
    data = pickle.load(f)

X_train = data['X_train']  # Already scaled, ~150 features
X_test = data['X_test']
y_train = data['y_train']
y_test = data['y_test']

# Train Random Forest
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train, y_train)
```

### **Deep Learning Pipeline**

```bash
# Preprocess untuk Deep Learning
python preprocessing_pipeline_dnn.py --mode binary

# Load dalam notebook
import pickle
with open('processed_artifacts/binary_dnn_preprocessed.pkl', 'rb') as f:
    data = pickle.load(f)

X_train = data['X_train']  # Already scaled, ~25 features, float32
X_test = data['X_test']
y_train = data['y_train']
y_test = data['y_test']

# Train MLP
import tensorflow as tf
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)
```

---

## ⚡ Performance Impact

### **Traditional ML Pipeline:**
- ✅ **Accuracy:** Tinggi (feature engineering membantu)
- ⚠️ **Training Time:** Lebih lama (banyak fitur)
- ⚠️ **Memory:** Lebih besar (~200 MB)
- ✅ **Interpretability:** Sangat baik (bisa lihat feature importance)

### **Deep Learning Pipeline:**
- ✅ **Accuracy:** Biarkan model belajar sendiri
- ✅ **Training Time:** Lebih cepat (fitur sedikit)
- ✅ **Memory:** Lebih kecil (~50 MB)
- ⚠️ **Interpretability:** Rendah (black box)

---

## 🔍 Validation Differences

### **Traditional ML Pipeline:**
- ✅ 5-step validation (protocol consistency, temporal logic, dll)
- ✅ Comprehensive checks
- ✅ Reports warnings

### **Deep Learning Pipeline:**
- ✅ Basic integrity checks (NaN, Inf)
- ✅ Null analysis (>70% threshold)
- ⚡ Faster execution

---

## 📝 Summary Table

| Kriteria | Traditional ML | Deep Learning |
|----------|----------------|---------------|
| **Output Features** | ~150 | ~25 |
| **File Size** | ~200 MB | ~50 MB |
| **Preprocessing Time** | ~3-5 min | ~1-2 min |
| **Feature Engineering** | Ekstensif | Minimal |
| **Best For** | RF, XGBoost | MLP, CNN-1D |
| **Interpretability** | ✅ High | ⚠️ Low |
| **Paper Alignment** | ✅ TON_IoT fundamentals | ⚠️ DNN-optimized |
| **Fair Comparison** | ❌ (biased towards trees) | ✅ (neutral) |

---

## 🎓 Rekomendasi untuk Paper/Skripsi

### **Jika tujuan riset:**

1. **"Perbandingan Traditional ML vs Deep Learning"**
   - ✅ Gunakan **KEDUA pipeline**
   - Run Traditional ML pipeline → Train RF, XGBoost
   - Run DNN pipeline → Train MLP, CNN-1D
   - Compare: Traditional ML dengan feature engineering vs DNN yang belajar sendiri

2. **"Optimisasi Feature Engineering untuk NIDS"**
   - ✅ Gunakan **Traditional ML pipeline**
   - Fokus pada feature importance analysis
   - Alignment dengan TON_IoT paper

3. **"Deep Learning Architecture Comparison (MLP vs CNN-1D)"**
   - ✅ Gunakan **DNN pipeline**
   - Fair comparison (same preprocessing)
   - Focus on model architecture differences

4. **"Comprehensive NIDS Evaluation"**
   - ✅ Gunakan **KEDUA pipeline**
   - Traditional ML pipeline untuk RF/XGBoost/SVM
   - DNN pipeline untuk MLP/CNN-1D
   - Hybrid: Bisa compare hasil dari kedua preprocessing

---

## 🚀 Next Steps

1. **Test Traditional ML Pipeline:**
   ```bash
   python preprocessing_pipeline.py --mode full
   ```

2. **Test DNN Pipeline:**
   ```bash
   python preprocessing_pipeline_dnn.py --mode full
   ```

3. **Compare outputs:**
   - Check feature counts
   - Check memory usage
   - Validate preprocessing quality

4. **Train models:**
   - Traditional ML: RF, XGBoost dengan `binary_preprocessed.pkl`
   - Deep Learning: MLP, CNN-1D dengan `binary_dnn_preprocessed.pkl`

5. **Evaluate & Compare:**
   - Accuracy, Precision, Recall, F1-Score
   - Training time
   - Inference time
   - Interpretability

---

## ✅ Kesimpulan

**Kedua pipeline VALID dan PENTING:**

- **Traditional ML Pipeline:** ✅ Research-oriented, feature engineering maksimal, alignment dengan TON_IoT fundamentals
- **Deep Learning Pipeline:** ✅ DNN-optimized, minimal engineering, fair comparison untuk MLP vs CNN-1D

**Pilih yang sesuai dengan tujuan riset Anda!** 🎯
