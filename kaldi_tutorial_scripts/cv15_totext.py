# cv15_totext.py
# Created by Chenzi Xu on 30/09/2023

from datasets import load_dataset
import re

cv_tsv = load_dataset('csv', 
                      data_files="cv-corpus-15.0-2023-09-08/zh-HK/train.tsv",
                      sep="\t")

cv_tsv = cv_tsv['train']
cv_text = cv_tsv.remove_columns(['up_votes', 'down_votes', 'age', 'gender', 'accents', 'variant', 'locale', 'segment'])

def prepare_text(batch):
  """Function to preprocess the dataset with the .map method"""
  transcription = batch["sentence"]
  utt_id = batch['path']
  spk_id = batch['client_id']
  
  # puncs = '！!?,"？｡。＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃《》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.'
  # transcription = re.sub(r"[%s]+" %puncs, "", transcription)
  
  #remove punctuation
  puncs = r'[^\u4e00-\u9FFFa-zA-Z0-9 ]'
  transcription = re.sub(puncs, '', transcription)
  
  #add space between Chinese characters
  transcription = re.sub(r'([\u4e00-\u9fff])', r'\1 ', transcription).strip()
  #add space after an English word followed by a Chinese character
  transcription = re.sub(r'([a-zA-Z0-9_]+)([\u4e00-\u9fff])', r'\1 \2', transcription)
  
  batch["sentence"] = transcription
  batch['client_id']=spk_id+ '-'+ utt_id[19:-4]
  
  return batch

texts = cv_text.map(prepare_text, desc="preprocess text")
texts = texts.remove_columns(['path'])
texts.to_csv('text', sep='\t', header=False,index=False)
