from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
WORKBOOK = HERE / "Economics_All_Data.xlsx"
if not WORKBOOK.exists():
    WORKBOOK = HERE.parent / "Economics_All_Data.xlsx"

parameters = pd.read_excel(WORKBOOK, sheet_name="Parameters", keep_default_na=False)
provenance = pd.read_excel(WORKBOOK, sheet_name="Provenance", keep_default_na=False)
index = pd.read_excel(WORKBOOK, sheet_name="Slide_Index", keep_default_na=False)
parameters.to_csv(HERE / "Parameters.csv", index=False, encoding="utf-8-sig")
provenance.to_csv(HERE / "Provenance.csv", index=False, encoding="utf-8-sig")
index.to_csv(HERE / "Slide_Index.csv", index=False, encoding="utf-8-sig")

try:
    from IPython.display import display
    display(index)
except ImportError:
    pass
