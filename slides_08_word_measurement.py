from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
WORKBOOK = HERE / "Economics_All_Data.xlsx"
if not WORKBOOK.exists():
    WORKBOOK = HERE.parent / "Economics_All_Data.xlsx"

selected = pd.read_excel(WORKBOOK, sheet_name="Selected_Words", keep_default_na=False)
hits = pd.read_excel(WORKBOOK, sheet_name="Word_Hits_Records", keep_default_na=False)
selected.to_csv(HERE / "Selected_Words.csv", index=False, encoding="utf-8-sig")
hits.to_csv(HERE / "Word_Hits_Records.csv", index=False, encoding="utf-8-sig")

table = pd.DataFrame([
    ["Title hit", "evidence lemma present: 1; absent: 0", "Repeated hits count once"],
    ["Denominator", "All retained titles in that journal/period", "Includes titles without the word"],
    ["Aggregation", "Journal rates, then equal journal weights", "Limits dominance by larger journals"],
    ["Limits", "finance ≠ finance papers; theory ≠ theory papers", "Words may occur together"],
], columns=["Stage", "Rule", "Meaning"])

try:
    from IPython.display import display
    display(table)
except ImportError:
    pass
