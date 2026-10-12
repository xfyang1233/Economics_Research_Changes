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

journals = ["AER", "QJE", "JPE", "Econometrica", "REStud"]
period = pd.read_excel(WORKBOOK, sheet_name="Coverage_Period", keep_default_na=False)
coverage = pd.read_excel(WORKBOOK, sheet_name="Coverage_Journal", keep_default_na=False)

period.to_csv(HERE / "Coverage_Period.csv", index=False, encoding="utf-8-sig")
coverage.to_csv(HERE / "Coverage_Journal.csv", index=False, encoding="utf-8-sig")

table = period.pivot(index="journal", columns="period_start", values="abstract_rate").reindex(journals)
values = 100 * table.to_numpy(dtype=float)

fig, ax = plt.subplots(figsize=(12, 5))
image = ax.imshow(values, aspect="auto", cmap="Blues", vmin=0, vmax=100)
ax.set_yticks(range(len(journals)), journals)
ax.set_xticks(range(len(table.columns)), [f"{p}-{p + 4}" for p in table.columns], rotation=35, ha="right")
for y in range(values.shape[0]):
    for x in range(values.shape[1]):
        ax.text(x, y, f"{values[y, x]:.0f}", ha="center", va="center",
                color="white" if values[y, x] > 65 else "#233C4A")
fig.colorbar(image, ax=ax, label="Available abstracts (%)")

png = HERE / "coverage.png"
fig.tight_layout()
fig.savefig(png, dpi=180, bbox_inches="tight")

try:
    from IPython.display import Image, display
    display(Image(filename=str(png)))
except ImportError:
    pass
