# cv15_select_wavs.py
# Created by Chenzi Xu on 30/09/2023

import pandas as pd
import subprocess
import os

dir = 'cv-corpus-15.0-2023-09-08/zh-HK/clips_wavs'
train_dir = 'cv-corpus-15.0-2023-09-08/zh-HK/train_wavs'

cv_tsv = pd.read_csv('cv-corpus-15.0-2023-09-08/zh-HK/train.tsv', sep='\t', header=0)

def move(item):
    item = item[:-4] + '.wav'
    command = ['mv', os.path.join(dir, item), os.path.join(train_dir, item)]
    subprocess.run(command)

cv_tsv['path'].apply(move)

