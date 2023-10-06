# wavscp.py
# Created by Chenzi Xu on 30/09/2023

import os
import pandas as pd

dir = 'cv-corpus-15.0-2023-09-08/zh-HK/clips_wavs'

table = pd.read_csv('table.csv', names = ['file', 'client_id','utt_id'])

path=[]

for root, dirs, files in os.walk(os.path.abspath(dir)):
    for file in files:
        path.append([file[19:-4], os.path.join(root, file)])

df = pd.DataFrame(path, columns=['file', 'path'])
df['file'] = df['file'].astype('int64')

df_update = pd.merge(df, table, on='file', how='right')
df_update = df_update[['utt_id','path']]
df_update.to_csv('wav.scp', sep=' ', index=False, header=False)