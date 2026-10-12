from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
WORKBOOK = HERE / "Economics_All_Data.xlsx"
if not WORKBOOK.exists():
    WORKBOOK = HERE.parent / "Economics_All_Data.xlsx"

coverage = pd.read_excel(WORKBOOK, sheet_name="Coverage_Journal", keep_default_na=False)
coverage.to_csv(HERE / "Coverage_Journal.csv", index=False, encoding="utf-8-sig")

try:
    from IPython.display import display
    display(coverage)
except ImportError:
    pass
