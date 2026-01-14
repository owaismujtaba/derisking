# Running the India Derisking Project

## Quick Start

### 1. Install Dependencies

```bash
# Install pandas (required)
sudo apt install python3-pandas

# Or using pip in virtual environment
python3 -m venv venv
source venv/bin/activate
pip install pandas
```

### 2. Run Complete Pipeline

```bash
# Run everything (data processing + analysis)
python3 run.py
```

## Command-Line Options

### Full Pipeline
```bash
python3 run.py
```
Runs: Data extraction → Concatenation → Analysis → Report generation

### Skip ZIP Extraction
```bash
python3 run.py --skip-extraction
```
Use when CSV files are already extracted

### Analysis Only
```bash
python3 run.py --analysis-only
```
Skip data processing, run only derisking analysis

### Processing Only
```bash
python3 run.py --process-only
```
Only process data, skip analysis

## What Gets Generated

### Data Processing Output
- `data/merged/consolidated_trade_data.csv` - All trade data (755K+ rows)

### Analysis Output
- `output/derisking_analysis/analysis_report.md` - Executive summary
- `output/derisking_analysis/metrics_summary.csv` - Time series (2007-2024)
- `output/derisking_analysis/partner_diversification.csv` - Trade partners
- `output/derisking_analysis/sector_analysis.csv` - Strategic sectors
- `output/derisking_analysis/period_comparison.json` - Baseline vs intervention

### Reports
- `DERISKING_REPORT.md` - Full research report (387 lines)

## Individual Scripts

### Data Processing
```bash
python3 process_data.py
```

### Derisking Analysis
```bash
python3 analyze_derisking.py
```

### Check Year Coverage
```bash
python3 check_years.py
```

## Project Structure

```
derisking/
├── run.py                    # Main pipeline runner ⭐
├── process_data.py           # Data processing script
├── analyze_derisking.py      # Analysis script
├── check_years.py            # Year coverage checker
├── requirements.txt          # Dependencies
├── DERISKING_REPORT.md       # Full report
├── src/
│   ├── data_processor.py     # Data processing (pandas-based)
│   ├── metrics_calculator.py # 7 metrics (pandas-based)
│   └── derisking_analyzer.py # Analysis orchestrator
├── data/
│   ├── raw/                  # ZIP files (input)
│   └── merged/               # Consolidated CSV (output)
└── output/
    └── derisking_analysis/   # Analysis results
```

## Help

```bash
python3 run.py --help
```
