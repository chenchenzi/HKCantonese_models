# cv15_getscript.py
# Created by Chenzi Xu on 30/09/2023

import pandas as pd
import re
import sys

if len(sys.argv) != 3:
    print("Usage: python cv_totgs.py <zh-HK_tsv> <yue_tsv>")
    sys.exit(1)

hk_file = sys.argv[1]
yue_file = sys.argv[2]

hk_tsv = pd.read_csv(hk_file, sep="\t", header=0, encoding="utf-8")
yue_tsv = pd.read_csv(yue_file, sep="\t", header=0, encoding="utf-8")

cv_tsv = pd.concat([hk_tsv, yue_tsv], ignore_index=True)

cv_tsv = cv_tsv[["sentence"]]
# remove punctuation
cv_tsv["sentence"] = cv_tsv["sentence"].apply(
    lambda x: re.sub(r"[^\u4e00-\u9FFFa-zA-Z0-9 ]", "", x)
)
# add space between Chinese characters
cv_tsv["sentence"] = cv_tsv["sentence"].apply(
    lambda x: re.sub(r"([\u4e00-\u9fff])", r"\1 ", x).strip()
)
# add space after an English word followed by a Chinese character
cv_tsv["sentence"] = cv_tsv["sentence"].apply(
    lambda x: re.sub(r"([a-zA-Z0-9_]+)([\u4e00-\u9fff])", r"\1 \2", x)
)

cv_tsv.to_csv("transcripts.txt", index=False, header=False)
