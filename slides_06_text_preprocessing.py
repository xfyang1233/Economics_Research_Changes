from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).resolve().parent
WORKBOOK = HERE / "Economics_All_Data.xlsx"
if not WORKBOOK.exists():
    WORKBOOK = HERE.parent / "Economics_All_Data.xlsx"

plt.rcParams.update({"font.size": 12, "axes.titlesize": 15, "axes.labelsize": 14,
                     "xtick.labelsize": 12, "ytick.labelsize": 13, "legend.fontsize": 10,
                     "axes.spines.top": False, "axes.spines.right": False,
                     "axes.edgecolor": "#BDCDD4", "text.color": "#233C4A",
                     "axes.labelcolor": "#233C4A", "xtick.color": "#4D6673",
                     "ytick.color": "#4D6673"})

vocabulary = pd.read_excel(WORKBOOK, sheet_name="Vocabulary", keep_default_na=False)
lemma_map = pd.read_excel(WORKBOOK, sheet_name="Lemma_Map", keep_default_na=False)
stopwords = pd.read_excel(WORKBOOK, sheet_name="Stopwords", keep_default_na=False)
parameters = pd.read_excel(WORKBOOK, sheet_name="Parameters", keep_default_na=False)
for name, frame in [("Vocabulary", vocabulary), ("Lemma_Map", lemma_map),
                    ("Stopwords", stopwords), ("Parameters", parameters)]:
    frame.to_csv(HERE / f"{name}.csv", index=False, encoding="utf-8-sig")

top = vocabulary.nlargest(18, "document_frequency").sort_values("document_frequency")
fig, ax = plt.subplots(figsize=(12, 5.8))
ax.barh(top.term, top.document_frequency, color="#167D9A")
ax.set_xlabel("Titles containing each retained term")
ax.grid(axis="x", alpha=.2)

png = HERE / "top_terms.png"
fig.tight_layout()
fig.savefig(png, dpi=180, bbox_inches="tight")

try:
    from IPython.display import Image, display
    display(Image(filename=str(png)))
except ImportError:
    pass
