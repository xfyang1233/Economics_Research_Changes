from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
WORKBOOK = HERE / "Economics_All_Data.xlsx"
if not WORKBOOK.exists():
    WORKBOOK = HERE.parent / "Economics_All_Data.xlsx"

topics = ["T01", "T02", "T03", "T04", "T05"]
top_words = pd.read_excel(WORKBOOK, sheet_name="Topic_Top_Words", keep_default_na=False)
examples = pd.read_excel(WORKBOOK, sheet_name="Topic_Examples", keep_default_na=False)
probabilities = pd.read_excel(WORKBOOK, sheet_name="Topic_Word_Probabilities", keep_default_na=False)
names = pd.read_excel(WORKBOOK, sheet_name="Topic_Names", keep_default_na=False)
parameters = pd.read_excel(WORKBOOK, sheet_name="Parameters", keep_default_na=False)
for name, frame in [("Topic_Top_Words", top_words), ("Topic_Examples", examples),
                    ("Topic_Word_Probabilities", probabilities), ("Topic_Names", names),
                    ("Parameters", parameters)]:
    frame.to_csv(HERE / f"{name}.csv", index=False, encoding="utf-8-sig")

labels = dict(zip(names.topic_id.astype(str), names.interpretation.astype(str)))
rows = []
for topic in topics:
    top3 = top_words[(top_words.topic_id == topic) & (top_words["rank"] <= 3)].sort_values("rank")
    rows.append([topic, labels[topic], ", ".join(top3.term.astype(str))])
table = pd.DataFrame(rows, columns=["Topic", "Interpretive label", "Top three words"])

try:
    from IPython.display import display
    display(table)
except ImportError:
    pass
