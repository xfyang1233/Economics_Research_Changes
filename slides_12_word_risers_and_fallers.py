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

changes = pd.read_excel(WORKBOOK, sheet_name="Word_Changes", keep_default_na=False)
changes.to_csv(HERE / "Word_Changes.csv", index=False, encoding="utf-8-sig")

top = changes.reindex(changes.change_pp.abs().sort_values(ascending=False).index).head(10)
top = top.sort_values("change_pp")

fig, ax = plt.subplots(figsize=(12, 5.8))
y = range(len(top))
ax.hlines(y, 100 * top.early_rate, 100 * top.recent_rate, color="#BFCDD4", lw=2)
ax.scatter(100 * top.early_rate, y, color="#7961A7", s=40, label="1970-1989")
ax.scatter(100 * top.recent_rate, y, color="#167D9A", s=40, label="2005-2024")
ax.set_yticks(list(y), top.word)
ax.set_xlabel("Exact lemma occurrence in titles (%)")
ax.legend(ncol=2, loc="upper center", bbox_to_anchor=(.5, 1.13))
ax.grid(axis="x", alpha=.2)

png = HERE / "word_changes.png"
fig.tight_layout()
fig.savefig(png, dpi=180, bbox_inches="tight")

try:
    from IPython.display import Image, display
    display(Image(filename=str(png)))
except ImportError:
    pass
