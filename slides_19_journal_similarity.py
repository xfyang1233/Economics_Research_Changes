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
distance = pd.read_excel(WORKBOOK, sheet_name="Journal_Distance", keep_default_na=False)
period = pd.read_excel(WORKBOOK, sheet_name="Distance_Period", keep_default_na=False)
profiles = pd.read_excel(WORKBOOK, sheet_name="Journal_Era_Topics", keep_default_na=False)
distance.to_csv(HERE / "Journal_Distance.csv", index=False, encoding="utf-8-sig")
period.to_csv(HERE / "Distance_Period.csv", index=False, encoding="utf-8-sig")
profiles.to_csv(HERE / "Journal_Era_Topics.csv", index=False, encoding="utf-8-sig")

largest = distance.euclidean_distance.max()
fig, axs = plt.subplots(1, 2, figsize=(12, 5), sharey=True)
for ax, era, title in zip(axs, ["Early 1970-1989", "Recent 2005-2024"], ["1970-1989", "2005-2024"]):
    values = (distance[distance.era == era]
              .pivot(index="journal_a", columns="journal_b", values="euclidean_distance")
              .reindex(index=journals, columns=journals).to_numpy())
    ax.imshow(values, aspect="auto", cmap="Oranges", vmin=0, vmax=largest)
    ax.set_xticks(range(5), journals, rotation=35, ha="right")
    ax.set_yticks(range(5), journals)
    ax.set_title(title)
    for y in range(5):
        for x in range(5):
            ax.text(x, y, f"{values[y, x]:.3f}", ha="center", va="center", fontsize=13)

png = HERE / "journal_distance.png"
fig.tight_layout()
fig.savefig(png, dpi=180, bbox_inches="tight")

try:
    from IPython.display import Image, display
    display(Image(filename=str(png)))
except ImportError:
    pass
