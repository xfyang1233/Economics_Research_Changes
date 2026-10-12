from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
WORKBOOK = HERE / "Economics_All_Data.xlsx"
if not WORKBOOK.exists():
    WORKBOOK = HERE.parent / "Economics_All_Data.xlsx"

eras = ["Early 1970-1989", "Middle 1990-2004", "Recent 2005-2024"]
words = ["evidence", "theory", "data", "inequality", "policy"]
profiles = pd.read_excel(WORKBOOK, sheet_name="Historical_Profiles", keep_default_na=False)
era = pd.read_excel(WORKBOOK, sheet_name="Word_Era", keep_default_na=False)
topics = pd.read_excel(WORKBOOK, sheet_name="Topic_Period", keep_default_na=False)
profiles.to_csv(HERE / "Historical_Profiles.csv", index=False, encoding="utf-8-sig")
era.to_csv(HERE / "Word_Era.csv", index=False, encoding="utf-8-sig")
topics.to_csv(HERE / "Topic_Period.csv", index=False, encoding="utf-8-sig")

profiles = profiles.set_index("era")
table = pd.DataFrame([[word] + [f"{100 * profiles.loc[e, word]:.1f}%" for e in eras] for word in words],
                     columns=["Word occurrence rate", "1970–1989", "1990–2004", "2005–2024"])

try:
    from IPython.display import display
    display(table)
except ImportError:
    pass
