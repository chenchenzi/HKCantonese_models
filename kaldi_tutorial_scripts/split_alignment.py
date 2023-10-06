#!/bin/sh

#  split_alignment.py
#  
#  Created by Eleanor Chodroff on 3/25/15.
#  Modified by Chenzi Xu on 1/10/23.

import sys,csv
results=[]

#name = name of first text file in final_ali.txt
#name_fin = name of final text file in final_ali.txt

name = "common_voice_zh-HK_22267475"
name_fin = "common_voice_zh-HK_23688013"

try:
    with open("final_ali_short.txt") as f: #pron_alignment
#        next(f) #skip header
        for line in f:
            columns=line.split("\t")
            name_prev = name
            name = columns[0]
            if (name_prev != name):
                try:
                    with open("align_txt/"+name_prev+".txt",'w') as fwrite: #align_prons
                        writer = csv.writer(fwrite)
                        fwrite.write("\n".join(results))
                        fwrite.close()
                #print name
                except Exception as e:
                    print("Failed to write file",e)
                    sys.exit(2)
                del results[:]
                results.append(line[0:-1])
            else:
                results.append(line[0:-1])
except Exception as e:
    print("Failed to read file",e)
    sys.exit(1)
# this prints out the last textfile (nothing following it to compare with)
try:
    with open("align_txt/"+name_prev+".txt",'w') as fwrite:
        writer = csv.writer(fwrite)
        fwrite.write("\n".join(results))
        fwrite.close()
                #print name
except Exception as e:
    print("Failed to write file", e) 
    sys.exit(2)