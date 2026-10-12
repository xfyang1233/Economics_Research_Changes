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

words = ["evidence", "theory", "empirical", "data", "experiment", "model"]
period = pd.read_excel(WORKBOOK, sheet_name="Word_Period", keep_default_na=False)
era = pd.read_excel(WORKBOOK, sheet_name="Word_Era", keep_default_na=False)
period.to_csv(HERE / "Word_Period.csv", index=False, encoding="utf-8-sig")
era.to_csv(HERE / "Word_Era.csv", index=False, encoding="utf-8-sig")

fig, axs = plt.subplots(2, 3, figsize=(13, 5), sharex=True)
for ax, word in zip(axs.ravel(), words):
    ax.plot(period.period_start + 2, 100 * period[word], color="#167D9A", lw=2, marker="o", ms=4)
    ax.set_title(word)
    ax.set_ylabel("Titles (%)")
    ax.grid(axis="y", alpha=.2)
fig.supxlabel("Five-year period midpoint")

png = HERE / "method_word_trends.png"
fig.tight_layout()
fig.savefig(png, dpi=180, bbox_inches="tight")

try:
    from IPython.display import Image, display
    display(Image(filename=str(png)))
except ImportError:
    pass
