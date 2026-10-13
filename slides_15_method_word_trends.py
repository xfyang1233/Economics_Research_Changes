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
eras = era.set_index("era")


def period_average(ax, word):
    """Prespecified early and recent averages, drawn so the rates quoted in the talk are visible on the chart."""
    for label, x0, x1, color, align in [("Early 1970-1989", 1972, 1987, "#7961A7", "left"),
                                        ("Recent 2005-2024", 2007, 2022, "#167D9A", "right")]:
        value = 100 * eras.loc[label, word]
        x = x0 if align == "left" else x1
        ax.hlines(value, x0, x1, color=color, lw=2.5, ls=(0, (5, 3)), zorder=2)
        ax.annotate(f"avg {value:.2f}", (x, value), xytext=(3, 6) if align == "left" else (-3, 6),
                    textcoords="offset points", ha=align, va="bottom", fontsize=10, color=color,
                    weight="bold", zorder=4,
                    bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=0.85))
    ax.margins(x=.09, y=.16)


fig, axs = plt.subplots(2, 3, figsize=(13, 5), sharex=True)
for ax, word in zip(axs.ravel(), words):
    ax.plot(period.period_start + 2, 100 * period[word], color="#167D9A", lw=2, marker="o", ms=4)
    ax.set_title(word)
    ax.set_ylabel("Titles (%)")
    ax.grid(axis="y", alpha=.2)
    period_average(ax, word)
fig.supxlabel("Five-year period midpoint")

png = HERE / "method_word_trends.png"
fig.tight_layout()
fig.savefig(png, dpi=180, bbox_inches="tight")

try:
    from IPython.display import Image, display
    display(Image(filename=str(png)))
except ImportError:
    pass
