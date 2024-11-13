from transformers import T5ForConditionalGeneration, AutoTokenizer
from tqdm import tqdm
import pandas as pd
from lingpy import *

# load G2P models
model = T5ForConditionalGeneration.from_pretrained('charsiu/g2p_multilingual_byT5_small_100')
tokenizer = AutoTokenizer.from_pretrained('google/byt5-small')
model.eval()

# load pronunciaiton dictionary
pron = {l.split('\t')[0]:l.split('\t')[1].strip() for l in open('yue.tsv','r',encoding="utf-8").readlines()}

with open('lexicon.txt','w', encoding='utf-8') as output:
    
    rows=[]
    with open('words.txt','r',encoding='utf-8') as f:
        for line in tqdm(f):
            w = line.strip()
            word_pron = ''
            if w in pron:
                word_pron+=pron[w]
            
            else:
                out = tokenizer(['<yue>: '+w],padding=True,add_special_tokens=False,return_tensors='pt')
                preds = model.generate(**out,num_beams=1,max_length=50)
                phones = tokenizer.batch_decode(preds.tolist(),skip_special_tokens=True)
                word_pron+=phones[0]
            
            # writer=csv.writer(output, delimiter='\t')
            # writer.writerow([w,word_pron])
            rows.append([w,word_pron])
    
    lexicon = pd.DataFrame(rows, columns=['word', 'ipa'])
    lexicon['ipa'] = lexicon['ipa'].str.split(',')
    lexicon = lexicon.explode('ipa')
    
    #remove IPA tones and tokenize IPA-encoded strings
    lexicon['ipa'] = lexicon['ipa'].str.replace(r'[\u02E5-\u02E9]+', '', regex=True)
    lexicon['ipa'] = lexicon['ipa'].apply(lambda x: ' '.join(map(str, ipa2tokens(x))))

    #remove duplicated rows
    lexicon.drop_duplicates(inplace=True)
    lexicon.to_csv(output,sep='\t', index=False, header=False)

# Cantonese IPA inventory
# ipa_list = ['p', 'pʰ', 'b',
#     't', 'tʰ', 'd',
#     'k', 'kʰ', 'g',
#     'kw', 'kwʰ', 'gw',
#     'ts', 'tsʰ', 'dz',
#     'tʃ', 'tʃʰ', 'dʒ',
#     'f', 'v', 's', 'ʃ', 'h','ɵ',
#     'm', 'n', 'ŋ',
#     'l', 'j', 'w','r', 'ʁ',
#     'i', 'ɪ', 'e', 'ɛ', 'a', 'ɐ', 'ɔ', 'o', 'u', 'y','ʊ','œ'
#     'ɛ:', 'i:', 'ɔ:', 'y:', 'a:','u:','œ:',
#     'aɪ', 'aʊ', 'oɪ', 'eɪ', 'ou', 'ɛ:u', 'ɐi', 'ɐu', 'ɔ:y']
    