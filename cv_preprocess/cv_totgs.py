# cv_totgs.py
# Created by Chenzi Xu on 30/09/2023

import pandas as pd
import re
import sys
from praatio import textgrid

if len(sys.argv) != 4:
    print("Usage: python cv_totgs.py <input_path> <tsv_file> <duration_file>")
    sys.exit(1)

dir = sys.argv[1]
file = sys.argv[2]
clip_dur = sys.argv[3]

cv_tsv = pd.read_csv(file, sep='\t', header=0, encoding='utf-8')

cv_tsv = cv_tsv[['client_id', 'path', 'sentence']]
# remove punctuation
cv_tsv['sentence']=cv_tsv['sentence'].apply(lambda x:re.sub(r'[^\u4e00-\u9FFFa-zA-Z0-9 ]', '', x))
# add space between Chinese characters
cv_tsv['sentence']=cv_tsv['sentence'].apply(lambda x: re.sub(r'([\u4e00-\u9fff])', r'\1 ', x).strip())
# add space after an English word followed by a Chinese character
cv_tsv['sentence']=cv_tsv['sentence'].apply(lambda x: re.sub(r'([a-zA-Z0-9_]+)([\u4e00-\u9fff])', r'\1 \2', x))


dur = pd.read_csv(clip_dur, sep='\t', header=0, encoding='utf-8')

df = pd.merge(cv_tsv, dur, left_on='path', right_on='clip')

for index, row in df.iterrows():
    try:
        tg_path = dir + row['path'][:-4] + '.TextGrid'
        entry = (0, row['duration[ms]']/1000, row['sentence'])
        #print(entry)
        wordTier = textgrid.IntervalTier(row['client_id'], [entry], 0, row['duration[ms]']/1000)
        tg = textgrid.Textgrid()
        tg.addTier(wordTier)
        tg.save(tg_path, format="short_textgrid", includeBlankSpaces=True)
        print(f"Saved TextGrid: {tg_path}")
    except Exception as e:
        print("Failed to write file",e)