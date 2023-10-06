# utt2spk.py
# Created by Chenzi Xu on 30/09/2023

import pandas as pd

cv_tsv = pd.read_csv('cv-corpus-15.0-2023-09-08/zh-HK/train.tsv', sep='\t')

df = cv_tsv[['path','client_id']]
df['path']=df['path'].str.replace('common_voice_zh-HK_','')
df['path']=df['path'].str.replace('.mp3','')
df['utt_id']=df['client_id'] +'-'+df['path']
df.to_csv('table.csv', index=False, header=False)

df = df[['utt_id', 'client_id']]
df.drop_duplicates(inplace=True)
df.to_csv('utt2spk', sep=' ', index=False, header=False)
