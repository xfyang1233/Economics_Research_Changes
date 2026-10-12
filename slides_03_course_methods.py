from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
WORKBOOK = HERE / "Economics_All_Data.xlsx"
if not WORKBOOK.exists():
    WORKBOOK = HERE.parent / "Economics_All_Data.xlsx"

evidence = pd.read_excel(WORKBOOK, sheet_name="Course_Evidence", keep_default_na=False)
evidence.to_csv(HERE / "Course_Evidence.csv", index=False, encoding="utf-8-sig")

table = pd.DataFrame([
    ["Data", "HTTP/JSON, Pandas", "Unit 2: 19–25; Unit 3: 7, 13–16"],
    ["Text", "Regex, stopwords, noun lemmas", "Unit 10: 21–22"],
    ["Content", "Word clouds/counts; BoW → gensim LDA", "Unit 10: 4–6, 23–24"],
    ["Profiles", "Euclidean distance; cosine supplement", "Unit 12: 22, 25; Unit 14: 19–24"],
    ["Dispersion", "Shannon entropy, log₂", "Unit 6: 12–16; Unit 9: 5–9"],
], columns=["Stage", "Method", "Lecture evidence (PDF pages)"])

try:
    from IPython.display import display
    display(table)
except ImportError:
    pass
