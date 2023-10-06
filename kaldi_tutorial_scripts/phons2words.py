#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#  phons2words.py
#
#
#  Created by Eleanor Chodroff on 2/07/16.
#  Modified by Chenzi Xu on 1/10/23.

#### issues with unicode (u'')
import sys,csv,os,os.path,re,codecs

# make dictionary of word: prons
lex = {}

with codecs.open("lexicon.txt", "rb", "utf-8") as f:
    for line in f:
        line = line.strip()
        columns = line.split("\t")
        word = columns[0]
        pron = columns[1]
        #print pron
        try:
            lex[pron].append(word)
        except:
            lex[pron] = list()
            lex[pron].append(word)

# open file to write

word_ali = codecs.open("word_alignment.txt", "wb", "utf-8")

# read file with most information in it
with codecs.open("pron_alignment.txt", "rb", "utf-8") as f:
    for line in f:
        line = line.strip()
        line = line.split("\t")
        # get the pronunciation
        pron = line[1]
        # look up the word from the pronunciation in the dictionary
        word = lex.get(pron)
        word = word[0]
        file = line[0]
        start = line[2]
        end = line[3]
        word_ali.write(file + '\t' + word + '\t' + start + '\t' + end + '\n')
