# segments.py
# Created by Chenzi Xu on 30/09/2023

import pandas as pd

dur = pd.read_csv('cv-corpus-15.0-2023-09-08/zh-HK/clip_durations.tsv', sep='\t', header=0)

dur['file']=dur['clip'].str.replace('common_voice_zh-HK_','')
dur['file']=dur['file'].str.replace('.mp3','')
dur['file'] = dur['file'].astype('int64')

table = pd.read_csv('table.csv', names = ['file', 'client_id','utt_id'])

df = pd.merge(dur, table, on='file', how='right')
df['file_id'] = df['utt_id']
df['start_time'] = 0.0
df['end_time']= df['duration[ms]']/1000
df = df[['utt_id','file_id','start_time','end_time']]

df.to_csv('segments', sep=' ', index=False, header=False)