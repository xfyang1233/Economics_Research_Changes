from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
WORKBOOK = HERE / "Economics_All_Data.xlsx"
if not WORKBOOK.exists():
    WORKBOOK = HERE.parent / "Economics_All_Data.xlsx"

journals = ["AER", "QJE", "JPE", "Econometrica", "REStud"]
flow = pd.read_excel(WORKBOOK, sheet_name="Cleaning_Flow", keep_default_na=False)
coverage = pd.read_excel(WORKBOOK, sheet_name="Coverage_Journal", keep_default_na=False)
audit = pd.read_excel(WORKBOOK, sheet_name="Record_Audit", keep_default_na=False)
flow.to_csv(HERE / "Cleaning_Flow.csv", index=False, encoding="utf-8-sig")
coverage.to_csv(HERE / "Coverage_Journal.csv", index=False, encoding="utf-8-sig")
audit.to_csv(HERE / "Record_Audit.csv", index=False, encoding="utf-8-sig")

coverage = coverage.set_index("journal").reindex(journals)
table = pd.DataFrame([[j,
                       f"{coverage.loc[j, 'retained_n']:,}",
                       f"{100 * coverage.loc[j, 'abstract_rate']:.1f}%",
                       f"{coverage.loc[j, 'lda_n']:,}"] for j in journals],
                     columns=["Journal", "Retained titles", "Abstract coverage", "LDA titles"])

try:
    from IPython.display import display
    display(table)
except ImportError:
    pass
