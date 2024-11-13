# mp3towavs.py
# Created by Chenzi Xu on 30/09/2023

import re
import os
import sys
from tqdm import tqdm
import subprocess
from tqdm.contrib.concurrent import process_map

if len(sys.argv) != 3:
    print("Usage: python mp3towav.py <input_path> <output_path>")
    sys.exit(1)

path = sys.argv[1]
output = sys.argv[2]

os.makedirs(output, exist_ok=True)

file_pairs = [(file,re.search(r'(.*?)\.mp3',file).group(1)+'.wav') for file in tqdm(os.listdir(path))]

def convert_and_resample(item):
    command = ['sox', os.path.join(path,item[0]),'-r','16000',os.path.join(output,item[1])]
    subprocess.run(command)

if __name__ == '__main__':
    wavs = process_map(convert_and_resample, file_pairs, max_workers=8, chunksize=1)
