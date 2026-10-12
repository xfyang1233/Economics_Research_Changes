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

shifts = pd.read_excel(WORKBOOK, sheet_name="Period_Shifts", keep_default_na=False)
topics = pd.read_excel(WORKBOOK, sheet_name="Topic_Period", keep_default_na=False)
shifts.to_csv(HERE / "Period_Shifts.csv", index=False, encoding="utf-8-sig")
topics.to_csv(HERE / "Topic_Period.csv", index=False, encoding="utf-8-sig")

fig, ax = plt.subplots(figsize=(12, 5))
x = range(len(shifts))
tallest = shifts.euclidean_shift.max()
colors = ["#E09B37" if value == tallest else "#167D9A" for value in shifts.euclidean_shift]
ax.bar(list(x), shifts.euclidean_shift, color=colors)
ax.set_xticks(list(x), [f"{a}-{a + 4}\n→ {b}-{b + 4}"
                        for a, b in zip(shifts.previous_period, shifts.current_period)],
              rotation=30, ha="right", fontsize=12)
ax.set_ylabel("Euclidean movement")
ax.grid(axis="y", alpha=.2)

png = HERE / "period_shifts.png"
fig.tight_layout()
fig.savefig(png, dpi=180, bbox_inches="tight")

try:
    from IPython.display import Image, display
    display(Image(filename=str(png)))
except ImportError:
    pass
