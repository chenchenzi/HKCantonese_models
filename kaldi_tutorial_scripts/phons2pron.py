#  phons2pron.py
#
#
#  Created by Eleanor Chodroff on 2/07/16.
#  Modified by Chenzi Xu on 1/10/23.

import glob

pron_ali=open("pron_alignment.txt",'w')
pron=[]

files = glob.glob('align_txt/*.txt')

# process each file
for file in files:
    print(file)
    f = open(file, 'r')
    pron_ali.write('\n')
    for line in f:
        line = line.split("\t")       
        file=line[6]
        file = file.strip()
        phon_pos=line[7]
        #print phon_pos
        if phon_pos == "sil":
            phon_pos = "sil_S"
        phon_pos=phon_pos.split("_")
        phon=phon_pos[0]
        pos=phon_pos[1]
        #print pos
        if pos == "B":
            start=line[10]
            pron.append(phon)
        if pos == "S":
            start=line[10]
            end=line[11]
            pron.append(phon)
            pron_ali.write(file + '\t' + ' '.join(pron) +'\t'+ str(start) + '\t' + str(end))
            pron=[]
        if pos == "E":
            end=line[11]
            pron.append(phon)
            pron_ali.write(file + '\t' + ' '.join(pron) +'\t'+ str(start) + '\t' + str(end))
            pron=[]
        if pos == "I":
            pron.append(phon)