# tsv2praat.py
# Created by Chenzi Xu on 30/09/2023

import os
import re
from praatio import textgrid
from praatio.utilities.constants import Interval
import pandas as pd
from tqdm import tqdm


for file in tqdm(os.listdir('align_txt/')):
    name, ext = os.path.splitext(file)
    if ext != ".txt":
        continue
    tg_path = 'tg_phons/' + name + '.TextGrid'
    tsv=pd.read_csv('align_txt/'+file, sep='\t', names=['file', 'phone_pos','start','end'])
    dur = tsv.iloc[-1,-1]
    wordTier = textgrid.IntervalTier('phones', [], 0, dur)
    tg = textgrid.Textgrid()
    new = [(round(row[2], 2), round(row[3], 2), re.sub(r'_.*$', '', row[1])) for index, row in tsv.iterrows()]
    wordTier = wordTier.new(entries=new)
    tg.addTier(wordTier)
    tg.save(tg_path, format="short_textgrid", includeBlankSpaces=True)
    
    

