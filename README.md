# Financial Data Parser

A Python-based financial data processing tool that normalizes, merges, analyzes, and visualizes bank statement data and customer ledger entries. It supports advanced EDA, category-wise analysis, pivot reports, and exporting clean datasets for further use.

## Folder Structure

```
financial-data-parser/
├── config/
│   └── settings.py
├── data/
│   ├── processed/
│   │   ├── cleaned_KH_Ledger.csv
│   │   ├── merged_KH_Ledger.csv
│   │   └── normalized_KH_Bank.csv
│   ├── sample/
│   │   ├── Customer_Ledger_Entries_FULL.xlsx
│   │   └── KH_Bank.XLSX
├── examples/
│   ├── advanced_parsing.py
│   ├── basic_usage.py
│   └── performance_demo.py
├── output/
│   ├── filtered_by_amount.xlsx
│   └── filtered_by_date.xlsx
├── scripts/
│   └── run_benchmarks.py
├── src/
│   └── core/
│       └── utils/
├── tests/
│   ├── __init__.py
│   ├── test_data_storage.py
│   ├── test_excel_processor.py
│   ├── test_format_parser.py
│   └── test_type_detector.py
├── category_analysis.py
├── column_types.log
├── data_type_detector.py
├── detected_column_types.csv
├── eda_analysis.py
├── format_parser.py
├── main.py
├── README.md
└── requirements.txt
```

## How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Main Script
```bash
python main.py
```

### 3. Outputs Generated
- Cleaned and merged CSVs in `data/processed/`
- Filtered Excel files in `output/`
- Visualizations in `visualizations/`
- Detected column types in `detected_column_types.csv`

## Features
- Excel Data Parsing (Bank & Ledger)
- Data Normalization & Cleanup
- Merging Bank & Ledger Datasets
- Exploratory Data Analysis (EDA)
- Filter by Date / Amount Threshold
- Category-wise Analysis
- Monthly & Category Visualizations (PNG)
- Auto Data Type Detection

## Key Files
| File                          | Purpose                                   |
|-------------------------------|-------------------------------------------|
| `main.py`                     | Main orchestration script                |
| `eda_analysis.py`              | Exploratory Data Analysis module         |
| `format_parser.py`             | Cleans and standardizes dataset formats  |
| `data_type_detector.py`        | Detects column types (Datetime, Numeric) |
| `category_analysis.py`         | Generates category summaries and pivots  |

## Test Cases
All unit tests are located in `/tests` folder:
```bash
pytest tests/
```

## Folder Outputs
| Folder                | Description                                      |
|-----------------------|--------------------------------------------------|
| `data/sample/`         | Raw sample input Excel files                    |
| `data/processed/`      | Normalized, Merged, Cleaned CSV outputs          |
| `output/`              | Filtered datasets by amount/date (Excel)         |
| `visualizations/`      | Generated summary plots (PNG)                    |

## Author
Umer Zahid — Financial Data Parser Project (Assignment)