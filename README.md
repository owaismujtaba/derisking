# India Derisking Trade Data Processing

A modular pipeline for processing India-China trade data from 2007-2025.

## Project Structure

```
derisking/
├── data/                          # Raw ZIP files and extracted CSVs
├── output/                        # Processed/consolidated data
├── src/
│   ├── __init__.py
│   └── data_processor.py         # Core DataProcessor class
├── process_data.py               # Main entry point
├── check_years.py                # Year coverage analysis
└── README.md
```

## Features

- **Modular Design**: Structured OOP approach with `DataProcessor` class
- **ZIP Extraction**: Automatically extracts all ZIP files in data directory
- **Data Concatenation**: Merges multiple CSV files into one consolidated file
- **Validation**: Header validation and error handling
- **Logging**: Detailed logging for tracking progress and debugging
- **Summary Statistics**: Automatic generation of data summaries

## Usage

### Quick Start

```bash
# Run the complete pipeline
python3 process_data.py
```

This will:
1. Extract all ZIP files in `data/` directory
2. Find all CSV files matching pattern `DataJobID-*.csv`
3. Concatenate them into a single file
4. Save to `output/consolidated_trade_data.csv`

### Using the DataProcessor Class

```python
from src.data_processor import DataProcessor

# Initialize
processor = DataProcessor(data_dir="data", output_dir="output")

# Option 1: Run complete pipeline
output_file = processor.process_all(extract=True)

# Option 2: Step-by-step processing
processor.extract_zip_files()
csv_files = processor.get_csv_files()
output_file = processor.concatenate_csv_files(csv_files)

# Get summary statistics
summary = processor.get_data_summary(output_file)
print(summary)
```

### Check Year Coverage

```bash
# Analyze which years are present/missing
python3 check_years.py
```

## Data Coverage

Current data includes **18 years** from 2007-2024:
- ✅ 2007-2024 (complete)
- ❌ 2025 (not yet available)

## Output

The consolidated file includes all trade data with columns:
- ReporterISO3, ReporterName
- PartnerISO3, PartnerName
- ProductCode, ProductDescription
- Year
- TradeFlowCode, TradeFlowName
- TradeValue in 1000 USD
- Quantity, QtyUnit
- NetWeight in KGM
- Reporter/Partner Region and Income Group
- Nomenclature

## Requirements

- Python 3.6+
- Standard library only (no external dependencies)

## Logging

Detailed logs are output to console showing:
- Files being processed
- Rows extracted from each file
- Validation warnings
- Summary statistics
