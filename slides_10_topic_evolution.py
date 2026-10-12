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

topics = pd.read_excel(WORKBOOK, sheet_name="Topic_Period", keep_default_na=False)
changes = pd.read_excel(WORKBOOK, sheet_name="Topic_Changes", keep_default_na=False)
topics.to_csv(HERE / "Topic_Period.csv", index=False, encoding="utf-8-sig")
changes.to_csv(HERE / "Topic_Changes.csv", index=False, encoding="utf-8-sig")

palette = ["#167D9A", "#E09B37", "#7961A7", "#C9676C", "#439B7A"]
fig, ax = plt.subplots(figsize=(12, 5))
for i, topic in enumerate(["T01", "T02", "T03", "T04", "T05"]):
    ax.plot(topics.period_start + 2, 100 * topics[topic], marker="o", lw=2,
            label=topic, color=palette[i])
ax.set_ylabel("Mean soft topic share (%)")
ax.set_xlabel("Five-year period midpoint")
ax.legend(ncol=5, loc="upper center", bbox_to_anchor=(.5, 1.17))
ax.grid(axis="y", alpha=.2)

png = HERE / "topic_trends.png"
fig.tight_layout()
fig.savefig(png, dpi=180, bbox_inches="tight")

try:
    from IPython.display import Image, display
    display(Image(filename=str(png)))
except ImportError:
    pass
