# gutural_nlp
The objective of this project is to leverage the Whisper state-of-the-art automatic speech recognition (ASR) system developed by OpenAI for automatic speech recognition of gutural and scream sounds mainly present in heavy metal music.

I take advantage of the HuggingFace ecosystem to:

**1)** Create a dataset using .srt files and audio .wav files collected from Youtube Music in orde to annotate vocal sound extracts.

**2)** Fine-tune a large version of the Whisper model on music dataset curated manually by me.

**3)** Deploy a demo on Space repository using Gradio.

## Folder structure

```
|-- README.md
`-- Notebooks and Scripts
    |-- Dataset Preporcess Notebook.ipynb
    |-- preprocess.py
`-- SRT Files
```
