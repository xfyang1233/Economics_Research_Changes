from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
WORKBOOK = HERE / "Economics_All_Data.xlsx"
if not WORKBOOK.exists():
    WORKBOOK = HERE.parent / "Economics_All_Data.xlsx"

checks = pd.read_excel(WORKBOOK, sheet_name="LDA_Parameter_Checks", keep_default_na=False)
sensitivity = pd.read_excel(WORKBOOK, sheet_name="AER_Sensitivity", keep_default_na=False)
checks.to_csv(HERE / "LDA_Parameter_Checks.csv", index=False, encoding="utf-8-sig")
sensitivity.to_csv(HERE / "AER_Sensitivity.csv", index=False, encoding="utf-8-sig")

table = pd.DataFrame([[f"K={int(row.k)}, seed={int(row.seed)}",
                       f"{row.early_distance:.4f}",
                       f"{row.recent_distance:.4f}",
                       f"{row.distance_change:.4f}"] for _, row in checks.iterrows()],
                     columns=["gensim LDA settings", "Early distance", "Recent distance", "Change"])

try:
    from IPython.display import display
    display(table)
except ImportError:
    pass
