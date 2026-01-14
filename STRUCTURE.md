# Project Directory Structure

```
derisking/
│
├── 📄 run.py                          # Main pipeline runner (use this!)
├── 📄 process_data.py                 # Data processing only
├── 📄 analyze_derisking.py            # Analysis only
├── 📄 check_years.py                  # Year coverage checker
│
├── 📋 requirements.txt                # Python dependencies
├── 📋 README.md                       # Project overview
├── 📋 RUNNING.md                      # Quick start guide
├── 📋 DERISKING_REPORT.md             # Full research report (387 lines)
├── 📋 PANDAS_MIGRATION.md             # Pandas refactoring notes
│
├── 📁 src/                            # Source code
│   ├── __init__.py
│   ├── data_processor.py              # Data extraction & concatenation
│   ├── metrics_calculator.py          # 7 derisking metrics
│   └── derisking_analyzer.py          # Analysis orchestration
│
├── 📁 data/                           # Data directory
│   ├── raw/                           # Input: ZIP files (11 files, ~5MB)
│   │   ├── 3018440_*.ZIP
│   │   ├── 3018441_*.ZIP
│   │   └── ... (11 ZIP files total)
│   │
│   └── merged/                        # Output: Consolidated CSV
│       └── consolidated_trade_data.csv  # 755K rows, 40MB
│
└── 📁 output/                         # Analysis results
    └── derisking_analysis/
        ├── analysis_report.md         # Executive summary
        ├── metrics_summary.csv        # Time series (2007-2024)
        ├── partner_diversification.csv # Trade partner shares
        ├── sector_analysis.csv        # Strategic sector SSVI
        └── period_comparison.json     # Baseline vs intervention
```

## Data Flow

```
data/raw/*.ZIP
    ↓ (extract)
data/raw/*.csv (temporary)
    ↓ (concatenate)
data/merged/consolidated_trade_data.csv
    ↓ (analyze)
output/derisking_analysis/*
```

## File Sizes

- **Input**: 11 ZIP files (~5 MB total)
- **Extracted**: 11 CSV files (~15 MB total, cleaned up after processing)
- **Consolidated**: 1 CSV file (40 MB, 755,284 rows)
- **Analysis outputs**: ~25 KB (CSV + JSON + MD files)
