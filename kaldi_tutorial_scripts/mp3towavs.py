# mp3towavs.py
# Created by Chenzi Xu on 30/09/2023

import re
import os
from tqdm import tqdm
import subprocess
from tqdm.contrib.concurrent import process_map

path = 'cv-corpus-15.0-2023-09-08/zh-HK/clips'
output = 'cv-corpus-15.0-2023-09-08/zh-HK/clips_wavs'

file_pairs = [(file,re.search(r'(.*?)\.mp3',file).group(1)+'.wav') for file in tqdm(os.listdir(path))]

def convert_and_resample(item):
    command = ['sox', os.path.join(path,item[0]),'-r','16000',os.path.join(output,item[1])]
    subprocess.run(command)

if __name__ == '__main__':
    wavs = process_map(convert_and_resample, file_pairs, max_workers=4, chunksize=1)