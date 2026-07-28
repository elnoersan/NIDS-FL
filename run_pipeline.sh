#!/usr/bin/env bash
# ==========================================================================
# NIDS-FL: Full CRISP-DM Pipeline Runner
# ==========================================================================
# Implements the complete thesis methodology (22523297 - Rian Nur Ikhsan)
# Phases: Business Understanding → Data Understanding → Data Preparation
#         → Modeling → Evaluation (Deployment excluded)
#
# Usage:
#   chmod +x run_pipeline.sh
#   ./run_pipeline.sh                     # Full run (20 rounds, all scenarios)
#   ./run_pipeline.sh --quick             # Quick test (3 rounds, binary only)
#   ./run_pipeline.sh --skip-preprocessing # Skip Phase 3 if data exists
#
# Requirements:
#   - Python 3.11 venv at ../Paper/.venv
# ==========================================================================

set -euo pipefail

# Setup TF logging
export TF_CPP_MIN_LOG_LEVEL="3"

# ─── Configuration ────────────────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PYTHON="${SCRIPT_DIR}/../Paper/.venv/bin/python"

# ─── Enable GPU (CUDA via pip) ──────────────────────────────────────────
# PyTorch automatically uses its own bundled CUDA/cuDNN libraries.
# Do not force LD_LIBRARY_PATH to avoid CUDNN_STATUS_SUBLIBRARY_VERSION_MISMATCH
RAW_DATA="${SCRIPT_DIR}/train_test_network.csv"
BINARY_PKL="${SCRIPT_DIR}/EDA/processed_artifacts/binary_preprocessed.pkl"
MULTI_PKL="${SCRIPT_DIR}/EDA/processed_artifacts/multiclass_preprocessed.pkl"
REPORT_FILE="${SCRIPT_DIR}/THESIS_EXPERIMENT_REPORT.md"
LOG_DIR="${SCRIPT_DIR}/pipeline_logs"

QUICK_MODE=false
SKIP_PREPROCESSING=false

# ─── Parse Arguments ──────────────────────────────────────────────────────
for arg in "$@"; do
    case $arg in
        --quick)         QUICK_MODE=true ;;
        --skip-preprocessing) SKIP_PREPROCESSING=true ;;
        --help|-h)
            echo "Usage: ./run_pipeline.sh [--quick] [--skip-preprocessing]"
            echo "  --quick              Run with 3 rounds (fast demo)"
            echo "  --skip-preprocessing Skip Phase 3 if preprocessed data exists"
            exit 0
            ;;
    esac
done

# ─── Utility Functions ────────────────────────────────────────────────────
BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color
BOLD='\033[1m'

phase_header() {
    local phase_num=$1
    local phase_name=$2
    echo ""
    echo -e "${BLUE}╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║  ${BOLD}FASE ${phase_num}: ${phase_name}${NC}"
    echo -e "${BLUE}╚══════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

log_success() { echo -e "  ${GREEN}✓${NC} $1"; }
log_warn()    { echo -e "  ${YELLOW}⚠${NC} $1"; }
log_error()   { echo -e "  ${RED}✗${NC} $1"; }
log_info()    { echo -e "  ${BLUE}→${NC} $1"; }

elapsed_since() {
    local start=$1
    local now
    now=$(date +%s)
    local diff=$((now - start))
    echo "${diff}s"
}

# ─── Pre-flight Checks ───────────────────────────────────────────────────
echo ""
echo -e "${BOLD}══════════════════════════════════════════════════════════════════${NC}"
echo -e "${BOLD}  NIDS-FL: CRISP-DM Full Pipeline Execution${NC}"
echo -e "${BOLD}  Skripsi: Deteksi & Klasifikasi Serangan Jaringan Smart City${NC}"
echo -e "${BOLD}           Menggunakan Federated Learning${NC}"
echo -e "${BOLD}══════════════════════════════════════════════════════════════════${NC}"
echo ""

PIPELINE_START=$(date +%s)

if [ ! -f "$VENV_PYTHON" ]; then
    log_error "Python venv not found at: $VENV_PYTHON"
    log_info "Run: python3.11 -m venv ../Paper/.venv && ../Paper/.venv/bin/pip install tensorflow flwr pandas scikit-learn matplotlib seaborn"
    exit 1
fi

log_success "Python venv: $($VENV_PYTHON --version 2>&1)"

if $QUICK_MODE; then
    log_warn "QUICK MODE: 3 rounds, binary only (for testing)"
fi

mkdir -p "$LOG_DIR"

# ══════════════════════════════════════════════════════════════════════════
# FASE 1: BUSINESS UNDERSTANDING
# ══════════════════════════════════════════════════════════════════════════
phase_header "1" "BUSINESS UNDERSTANDING"

cat << 'EOF'
  Konteks Penelitian:
  ┌─────────────────────────────────────────────────────────────┐
  │  Smart City Network terdiri dari gateway IoT heterogen      │
  │  (transportasi, kesehatan, energi, layanan publik).         │
  │                                                             │
  │  Masalah:                                                   │
  │  • NIDS terpusat berisiko melanggar privasi data            │
  │  • Pengumpulan data ke satu titik mengganggu layanan        │
  │  • Data antar gateway sangat Non-IID (heterogen)            │
  │                                                             │
  │  Solusi: Horizontal Federated Learning (HFL)                │
  │  • FedAvg vs FedProx pada data Non-IID                     │
  │  • Model MLP dan CNN-1D                                     │
  │  • Klasifikasi Binary dan Multiclass                        │
  │                                                             │
  │  Kriteria Keberhasilan:                                     │
  │  1. Efektivitas pada data heterogen (Non-IID)               │
  │  2. Stabilitas pelatihan global model                       │
  │  3. Latensi pelatihan yang feasible                         │
  └─────────────────────────────────────────────────────────────┘
EOF

log_success "Business Understanding documented."

# ══════════════════════════════════════════════════════════════════════════
# FASE 2: DATA UNDERSTANDING
# ══════════════════════════════════════════════════════════════════════════
phase_header "2" "DATA UNDERSTANDING"

PHASE2_START=$(date +%s)

if [ ! -f "$RAW_DATA" ]; then
    log_warn "Raw dataset not found at: $RAW_DATA"
    log_info "Skipping Phase 2 (data understanding). Report will use cached results if available."
else
    log_info "Running EDA analysis on ToN-IoT dataset..."
    $VENV_PYTHON "${SCRIPT_DIR}/phase2_data_understanding.py" \
        --input "$RAW_DATA" \
        2>&1 | tee "${LOG_DIR}/phase2_data_understanding.log"
    log_success "Data Understanding complete ($(elapsed_since $PHASE2_START))"
fi

# ══════════════════════════════════════════════════════════════════════════
# FASE 3: DATA PREPARATION
# ══════════════════════════════════════════════════════════════════════════
phase_header "3" "DATA PREPARATION"

PHASE3_START=$(date +%s)

if $SKIP_PREPROCESSING && [ -f "$BINARY_PKL" ]; then
    log_warn "Preprocessed data found. Skipping preprocessing (--skip-preprocessing)."
    log_info "Binary:     $BINARY_PKL"
    log_info "Multiclass: $MULTI_PKL"
else
    if [ ! -f "$RAW_DATA" ]; then
        log_error "Cannot run preprocessing: raw data not found at $RAW_DATA"
        if [ -f "$BINARY_PKL" ]; then
            log_warn "Using existing preprocessed data instead."
        else
            log_error "No preprocessed data available. Aborting."
            exit 1
        fi
    else
        log_info "Running preprocessing pipeline..."
        log_info "Steps: Protocol-Aware Cleaning → Encoding → VarianceThreshold → StandardScaler → Stratified Split"
        $VENV_PYTHON "${SCRIPT_DIR}/EDA/preprocessing_pipeline.py" \
            2>&1 | tee "${LOG_DIR}/phase3_preprocessing.log"
        log_success "Data Preparation complete ($(elapsed_since $PHASE3_START))"
    fi
fi

# Verify preprocessed data exists
if [ ! -f "$BINARY_PKL" ]; then
    log_error "Binary preprocessed data not found: $BINARY_PKL"
    exit 1
fi
log_success "Binary dataset ready: $BINARY_PKL"

if [ -f "$MULTI_PKL" ]; then
    log_success "Multiclass dataset ready: $MULTI_PKL"
else
    log_warn "Multiclass dataset not found. Multiclass scenarios will be skipped."
fi

# ══════════════════════════════════════════════════════════════════════════
# FASE 4: MODELING + FASE 5: EVALUATION
# ══════════════════════════════════════════════════════════════════════════
phase_header "4+5" "MODELING & EVALUATION (Federated Learning)"

PHASE4_START=$(date +%s)

log_info "Configuration:"
if $QUICK_MODE; then
    echo "    Mode          : QUICK (demo)"
    echo "    Rounds        : 3"
    echo "    Scenarios     : Binary only"
    BENCHMARK_ARGS="--quick"
else
    echo "    Mode          : FULL (thesis-aligned)"
    echo "    Rounds        : 20"
    echo "    Scenarios     : Binary + Multiclass"
    echo "    Models        : MLP + CNN-1D"
    echo "    Strategies    : FedAvg, FedProx (μ=0.01, μ=0.001)"
    echo "    Non-IID       : α=0.3 (extreme) + α=5.0 (IID-like)"
    echo "    Clients       : 5"
    echo "    Hyperparams   : BS=512, E=1, LR=0.0005"
    BENCHMARK_ARGS=""
fi
echo ""

log_info "Starting Federated Learning benchmark..."
log_info "This may take 15-40 minutes on Ryzen 5 3500 (CPU mode)..."
echo ""

$VENV_PYTHON "${SCRIPT_DIR}/benchmark_federated_algorithms.py" $BENCHMARK_ARGS

log_success "Modeling & Evaluation complete ($(elapsed_since $PHASE4_START))"

# ══════════════════════════════════════════════════════════════════════════
# REPORT GENERATION
# ══════════════════════════════════════════════════════════════════════════
phase_header "R" "REPORT GENERATION"

REPORT_START=$(date +%s)

log_info "Generating comprehensive CRISP-DM experiment report..."

$VENV_PYTHON "${SCRIPT_DIR}/phase5_report_generator.py" \
    --output "$REPORT_FILE" \
    2>&1 | tee "${LOG_DIR}/report_generation.log"

log_success "Report generated: $REPORT_FILE ($(elapsed_since $REPORT_START))"

# ══════════════════════════════════════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════════════════════════════════════
TOTAL_TIME=$(elapsed_since $PIPELINE_START)

echo ""
echo -e "${BOLD}══════════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}${BOLD}  ✅ PIPELINE EXECUTION COMPLETE${NC}"
echo -e "${BOLD}══════════════════════════════════════════════════════════════════${NC}"
echo ""
echo "  Total Execution Time : $TOTAL_TIME"
echo ""
echo "  Generated Artifacts:"
echo "  ├── $REPORT_FILE"
echo "  ├── thesis_benchmark_results_pytorch.json"

if [ -f "${SCRIPT_DIR}/EDA/data_understanding_report.json" ]; then
echo "  ├── EDA/data_understanding_report.json"
fi

echo "  └── pipeline_logs/"
ls -1 "$LOG_DIR"/*.log 2>/dev/null | while read -r f; do
    echo "      ├── $(basename "$f")"
done

echo ""
echo -e "  ${BLUE}Buka report:${NC} cat $REPORT_FILE"
echo ""
