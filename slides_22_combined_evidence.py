from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
WORKBOOK = HERE / "Economics_All_Data.xlsx"
if not WORKBOOK.exists():
    WORKBOOK = HERE.parent / "Economics_All_Data.xlsx"

word_changes = pd.read_excel(WORKBOOK, sheet_name="Word_Changes", keep_default_na=False)
topic_changes = pd.read_excel(WORKBOOK, sheet_name="Topic_Changes", keep_default_na=False)
distance = pd.read_excel(WORKBOOK, sheet_name="Journal_Distance", keep_default_na=False)
entropy = pd.read_excel(WORKBOOK, sheet_name="Journal_Entropy", keep_default_na=False)
word_changes.to_csv(HERE / "Word_Changes.csv", index=False, encoding="utf-8-sig")
topic_changes.to_csv(HERE / "Topic_Changes.csv", index=False, encoding="utf-8-sig")
distance.to_csv(HERE / "Journal_Distance.csv", index=False, encoding="utf-8-sig")
entropy.to_csv(HERE / "Journal_Entropy.csv", index=False, encoding="utf-8-sig")

try:
    from IPython.display import display
    display(word_changes)
except ImportError:
    pass
