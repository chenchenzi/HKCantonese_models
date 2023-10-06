# cv15_getscript.py
# Created by Chenzi Xu on 30/09/2023

import pandas as pd
import re

dir = '/Users/cx936/Work/mfa-canto/train_wavs/'
cv_tsv = pd.read_csv('cv-corpus-15.0-2023-09-08/zh-HK/train.tsv', sep='\t', header=0)

cv_tsv = cv_tsv[['sentence']]
# remove punctuation
cv_tsv['sentence']=cv_tsv['sentence'].apply(lambda x:re.sub(r'[^\u4e00-\u9FFFa-zA-Z0-9 ]', '', x))
# add space between Chinese characters
cv_tsv['sentence']=cv_tsv['sentence'].apply(lambda x: re.sub(r'([\u4e00-\u9fff])', r'\1 ', x).strip())
# add space after an English word followed by a Chinese character
cv_tsv['sentence']=cv_tsv['sentence'].apply(lambda x: re.sub(r'([a-zA-Z0-9_]+)([\u4e00-\u9fff])', r'\1 \2', x))

cv_tsv.to_csv('transcripts.txt', index=False, header=False)