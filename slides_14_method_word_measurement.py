from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
WORKBOOK = HERE / "Economics_All_Data.xlsx"
if not WORKBOOK.exists():
    WORKBOOK = HERE.parent / "Economics_All_Data.xlsx"

selected = pd.read_excel(WORKBOOK, sheet_name="Selected_Words", keep_default_na=False)
era = pd.read_excel(WORKBOOK, sheet_name="Word_Era", keep_default_na=False)
selected.to_csv(HERE / "Selected_Words.csv", index=False, encoding="utf-8-sig")
era.to_csv(HERE / "Word_Era.csv", index=False, encoding="utf-8-sig")

table = pd.DataFrame([
    ["theory / equilibrium", "Theory or equilibrium; separate counts", "Share of theoretical articles"],
    ["evidence / empirical", "Evidence or empirical; separate counts", "Share of empirical articles"],
    ["data / experiment", "Data or experiments; separate counts", "Data intensity or causal identification"],
    ["model / estimation", "Models or estimation; separate counts", "Absence of a method when unmentioned"],
], columns=["Title words", "Possible wording", "Cannot establish"])

try:
    from IPython.display import display
    display(table)
except ImportError:
    pass
