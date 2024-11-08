# HKCantonese_models

This is a repository dedicated for pre-trained acoustic models of Hong Kong Cantonese and Cantonese forced alignment using Montreal Forced Aligner (MFA).

## Acoustic models

The pre-trained acoustic models of Hong Kong Cantonese are available in `pretrained_models/`:

- `acoustic_model_cv15_train.zip`: model trained using the `train` set (~10 hrs) from Common Voice Hong Kong Chinese Corpus (Common Voice Corpus 15.0 updated on 9/14/2023).

- `acoustic_model_cv15_validated.zip`: model trained using the `validated` set (~308.7 hrs, 2325 speakers) from Common Voice Hong Kong Chinese Corpus (Common Voice Corpus 15.0 updated on 9/14/2023).

> **New Updates 2024:**
> v1, v2, and v3 employ slightly different phone sets. For details, see below.

- `acoustic_model_cv19_v1.zip`: model trained using the `validated` set (~106.5 hrs, 3400 speakers) from Common Voice Hong Kong Chinese Corpus (`zh-HK`) plus Common Voice Cantonese Corpus (`yue`) (Common Voice Corpus 19.0 updated on 9/18/2024).
  
- `acoustic_model_cv19_v2.zip`: model trained using the `validated` set (~106.5 hrs, 3400 speakers) from Common Voice Hong Kong Chinese Corpus (`zh-HK`) plus Common Voice Cantonese Corpus (`yue`) (Common Voice Corpus 19.0 updated on 9/18/2024).
  
- `acoustic_model_cv19_v3.zip`: model trained using the `validated` set (~106.5 hrs, 3400 speakers) from Common Voice Hong Kong Chinese Corpus (`zh-HK`) plus Common Voice Cantonese Corpus (`yue`) (Common Voice Corpus 19.0 updated on 9/18/2024).
<br>

## Dictionaries

`cv15_validated_lexicon.txt` and `cv15_validated_lexicon.dict` contain the lexicon in the Common Voice Hong Kong Chinese Corpus 15.0, which is over 4800 entries. The former is in non-probabilistic format and the latter includes pronunciation and silence probabilities.

`v1`: including all new variants; checked syllable as a unit
`v2`: excluding new variants; checked syllable as a unit
`v3`: excluding new variants;  checked syllable separated

<br>

## Alignment using Montreal Forced Aligner

An example of using the pre-trained acoustic model is as follows:
```
mfa align [OPTIONS] corpus_directory dictionary acoustic_model_cv15_validated.zip
          output_directory
```

<br>

## Tutorials

1. [Training acoustic models using the Kaldi recipe](https://chenzixu.rbind.io/resources/3asr/sr3/)
   
   The relevant scripts are available in `kaldi_tutorial_scripts/`.

2. [Training acoustic models with MFA (Kaldi) implementation](https://chenzixu.rbind.io/resources/3asr/sr4/)
   
   The relevant scripts are available in `mfa_tutorial_scripts/`.
