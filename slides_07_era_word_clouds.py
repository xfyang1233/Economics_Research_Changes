import re
import unicodedata
from pathlib import Path

import pandas as pd
from wordcloud import WordCloud

HERE = Path(__file__).resolve().parent
WORKBOOK = HERE / "Economics_All_Data.xlsx"
if not WORKBOOK.exists():
    WORKBOOK = HERE.parent / "Economics_All_Data.xlsx"

sheets = ["Analysis_Records", "Lemma_Map", "Stopwords", "Vocabulary",
          "Wordcloud_Frequencies", "Wordcloud_Summary", "Wordcloud_Parameters"]
frames = {name: pd.read_excel(WORKBOOK, sheet_name=name, keep_default_na=False) for name in sheets}
for name, frame in frames.items():
    frame.to_csv(HERE / f"{name}.csv", index=False, encoding="utf-8-sig")

records = frames["Analysis_Records"]
lemmas = dict(zip(frames["Lemma_Map"].token.astype(str), frames["Lemma_Map"].lemma.astype(str)))
stopwords = set(frames["Stopwords"].token.astype(str))
vocabulary = set(frames["Vocabulary"].term.astype(str))

def clean(title):
    words = re.findall(r"[a-z]{2,}", unicodedata.normalize("NFKC", str(title)).lower())
    words = [lemmas.get(word, word) for word in words if word not in stopwords]
    return [word for word in words if word in vocabulary]

for era, start, end, filename in [("Early 1970-1989", 1970, 1989, "wordcloud_early.png"),
                                  ("Recent 2005-2024", 2005, 2024, "wordcloud_recent.png")]:
    titles = records[records.year.between(start, end)].title
    words = [word for title in titles for word in clean(title)]
    cloud = WordCloud(width=1400, height=900, max_words=80, background_color="white",
                      random_state=3154, collocations=False, normalize_plurals=False,
                      relative_scaling=0.5, prefer_horizontal=0.92, min_font_size=10,
                      min_word_length=0, regexp=r"[a-z]+",
                      color_func=lambda *args, **kwargs: "#14758C")
    cloud.generate(" ".join(words))
    cloud.to_file(str(HERE / filename))

try:
    from IPython.display import Image, display
    for name in ["wordcloud_early.png", "wordcloud_recent.png"]:
        display(Image(filename=str(HERE / name)))
except ImportError:
    pass
