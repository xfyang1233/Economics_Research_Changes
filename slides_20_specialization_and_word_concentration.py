from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
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

journals = ["AER", "QJE", "JPE", "Econometrica", "REStud"]
entropy = pd.read_excel(WORKBOOK, sheet_name="Journal_Entropy", keep_default_na=False)
concentration = pd.read_excel(WORKBOOK, sheet_name="Word_Concentration", keep_default_na=False)
entropy.to_csv(HERE / "Journal_Entropy.csv", index=False, encoding="utf-8-sig")
concentration.to_csv(HERE / "Word_Concentration.csv", index=False, encoding="utf-8-sig")

fig, axs = plt.subplots(1, 2, figsize=(12, 5))
x = np.arange(5)
for era, offset, color, label in [("Early 1970-1989", -.18, "#7961A7", "1970-1989"),
                                  ("Recent 2005-2024", .18, "#167D9A", "2005-2024")]:
    values = entropy[entropy.era == era].set_index("journal").reindex(journals).shannon_entropy_bits
    axs[0].bar(x + offset, values, width=.36, color=color, label=label)
axs[0].axhline(np.log2(5), color="#8597A1", linestyle="--", lw=1)
axs[0].set_xticks(x, journals, rotation=25)
axs[0].set_ylabel("Ordinary Shannon entropy (bits)")
axs[0].set_ylim(0, np.log2(5) + .15)
axs[0].legend()

words = ["finance", "inequality", "evidence", "data"]
x = np.arange(len(words))
for era, offset, color, label in [("Early 1970-1989", -.18, "#7961A7", "1970-1989"),
                                  ("Recent 2005-2024", .18, "#167D9A", "2005-2024")]:
    values = (concentration[concentration.era == era].drop_duplicates("word")
              .set_index("word").reindex(words).largest_journal_share * 100)
    axs[1].bar(x + offset, values, width=.36, color=color, label=label)
axs[1].set_xticks(x, words, rotation=20)
axs[1].set_ylabel("Largest journal share of word hits (%)")
axs[1].set_ylim(0, 100)

png = HERE / "entropy_concentration.png"
fig.tight_layout()
fig.savefig(png, dpi=180, bbox_inches="tight")

try:
    from IPython.display import Image, display
    display(Image(filename=str(png)))
except ImportError:
    pass
