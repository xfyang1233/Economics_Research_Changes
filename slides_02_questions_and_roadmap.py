from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
WORKBOOK = HERE / "Economics_All_Data.xlsx"
if not WORKBOOK.exists():
    WORKBOOK = HERE.parent / "Economics_All_Data.xlsx"

index = pd.read_excel(WORKBOOK, sheet_name="Slide_Index", keep_default_na=False)
index.to_csv(HERE / "Slide_Index.csv", index=False, encoding="utf-8-sig")

try:
    from IPython.display import display
    display(index)
except ImportError:
    pass
