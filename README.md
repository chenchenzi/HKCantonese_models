# HKCantonese_models

This is a repository dedicated for training acoustic models of Hong Kong Cantonese and Cantonese forced alignment.

## Acoustic models
Acoustic models of Hong Kong Cantonese are available in `pretrained_models/`:
- `acoustic_model_cv15_train.zip`: model trained using the `train` set from Common Voice Hong Kong Chinese corpus (Common Voice Corpus 15.0 updated on 9/14/2023).
- `acoustic_model_cv15_validated.zip` (coming soon): model trained using the `validated` set from Common Voice Hong Kong Chinese corpus (Common Voice Corpus 15.0 updated on 9/14/2023).

## Tutorials
1. [Training acoustic models using the Kaldi recipe](https://chenzixu.rbind.io/resources/3asr/sr3/)
   
   The relevant scripts are available in `kaldi_tutorial_scripts/`.

2. [Training acoustic models with MFA (Kaldi) implementation](https://chenzixu.rbind.io/resources/3asr/sr4/)
   
      The relevant scripts are available in `mfa_tutorial_scripts/`.
