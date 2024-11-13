# cv_select_wavs.py
# Created by Chenzi Xu on 30/09/2023

import pandas as pd
import subprocess
#from concurrent.futures import ThreadPoolExecutor
import os
import sys

if len(sys.argv) != 4:
    print("Usage: python cv_select_wavs.py <tsv_file> <input_path> <output_path>")
    sys.exit(1)

file = sys.argv[1]
dir = sys.argv[2]
train_dir = sys.argv[3]

os.makedirs(train_dir, exist_ok=True)

cv_tsv = pd.read_csv(file, sep='\t', header=0, encoding='utf-8')

def move(item):
    item = item[:-4] + '.wav'
    if os.path.exists(os.path.join(dir,item)):
        command = ['mv', os.path.join(dir, item), os.path.join(train_dir, item)]
        subprocess.run(command)
    else:
        print(f"File not found: {os.path.join(dir,item)}")

cv_tsv['path'].apply(move)
#if __name__ == '__main__':
    # Use ThreadPoolExecutor to move files in parallel
#    with ThreadPoolExecutor() as executor:
#        executor.map(move, cv_tsv['path'])
