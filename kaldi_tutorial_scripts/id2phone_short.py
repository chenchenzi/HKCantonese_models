# id2phone_short.py
# Created by Chenzi Xu on 30/09/2023

import pandas as pd

ctm = pd.read_csv('merged_alignment.txt', sep=' ', encoding='utf-8', 
                   names=['file_utt','utt','start','dur','id'])
ctm['file'] = ctm['file_utt']
ctm['filename'] = 'common_voice_zh-HK_' + ctm['file_utt'].str.extract(r'-(\d+)$') #only one utterance per file

phones = pd.read_csv('phones.txt', sep=' ', encoding='utf-8', 
                   names=['phone','id'])

segments = pd.read_csv('segments', sep=' ', encoding='utf-8', 
                   names=["file_utt","file","start_utt","end_utt"])

ctm2 = pd.merge(ctm, phones, on='id', how='left')


ctm3 = pd.merge(ctm2, segments, on=["file_utt","file"], how='left')

ctm3['start_real'] = ctm3['start'] + ctm3['start_utt']
ctm3['end_real'] = ctm3['start_real'] + ctm3['dur']

ctm3= ctm3[['filename', 'phone', 'start_real', 'end_real']]

ctm3.to_csv('final_ali_short.txt', sep='\t', index=False, header=False)
