from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
WORKBOOK = HERE / "Economics_All_Data.xlsx"
if not WORKBOOK.exists():
    WORKBOOK = HERE.parent / "Economics_All_Data.xlsx"

journals = ["AER", "QJE", "JPE", "Econometrica", "REStud"]
topics = ["T01", "T02", "T03", "T04", "T05"]
profiles = pd.read_excel(WORKBOOK, sheet_name="Journal_Era_Topics", keep_default_na=False)
overall = pd.read_excel(WORKBOOK, sheet_name="Journal_Topics", keep_default_na=False)
names = pd.read_excel(WORKBOOK, sheet_name="Topic_Names", keep_default_na=False)
profiles.to_csv(HERE / "Journal_Era_Topics.csv", index=False, encoding="utf-8-sig")
overall.to_csv(HERE / "Journal_Topics.csv", index=False, encoding="utf-8-sig")

labels = {topic: label.replace(", ", " / ").replace(" and ", " / ")
          for topic, label in zip(names.topic_id.astype(str), names.interpretation.astype(str))}
rows = []
for journal in journals:
    cells = []
    for era in ["Early 1970-1989", "Recent 2005-2024"]:
        values = profiles[(profiles.era == era) & (profiles.journal == journal)][topics].to_numpy()[0]
        best = topics[int(values.argmax())]
        cells.append(f"{best} {labels[best]} {100 * values.max():.1f}%")
    rows.append([journal] + cells)
table = pd.DataFrame(rows, columns=["Journal", "Early leading group (share)", "Recent leading group (share)"])

try:
    from IPython.display import display
    display(table)
except ImportError:
    pass
