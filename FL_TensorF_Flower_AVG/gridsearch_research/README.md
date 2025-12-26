# Grid Search for Hyperparameter Tuning

All grid search files have been organized in this folder.

## Quick Start

```bash
cd gridsearch_research
./start_gridsearch.sh
```

## Files

- `run_gridsearch.py` - Main orchestrator (runs all 20 experiments)
- `research_hypertuning_gridsearch.py` - Individual experiment runner
- `start_gridsearch.sh` - Quick start script
- `check_progress.py` - Progress monitor

## Documentation

- `GRIDSEARCH_GUIDE.md` - Quick start guide (read this first!)
- `README_GRIDSEARCH.md` - Detailed documentation
- `SETUP_SUMMARY.md` - Overview of everything

## To Run

```bash
# Navigate to this folder
cd gridsearch_research

# Start grid search
./start_gridsearch.sh
```

## Results

After running, all 20 experiment results will be saved here:
- `bs32_epoch1_lr0p0010/`
- `bs32_epoch1_lr0p0005/`
- ... (18 more folders)
- `summary_report.md` (final comprehensive report)

---

**Grid Search**: 20 experiments × 4 models = 80 models total!
