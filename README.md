# gutural_nlp

## Scream: Fine-Tuned Whisper model for automatic gutural speech recognition 🤟🤟🤟
The objective of this project is to leverage the Whisper state-of-the-art automatic speech recognition (ASR) system developed by OpenAI for automatic speech recognition of gutural and scream sounds mainly present in heavy metal music.

I take advantage of the HuggingFace ecosystem to:

**1)** Create a dataset using .srt files and audio .wav files collected from Youtube in order to annotate vocal sound extracts.

**2)** Fine-tune a large version of the Whisper model on the dataset created.

**3)** Deploy a demo on Space repository using Gradio.

## Folder structure

```
|-- README.md
`-- Notebooks and Scripts
    |-- Dataset Preprocess Notebook.ipynb
    |-- EDA_gutural_nlp.ipynb
    |-- gutural_nlp.ipynb
    |-- preprocess.py
    |-- youtubetowav.py
`-- images
    |-- spectogram 1.png
    |-- spectogram 2.png
    |-- spectogram 3.png
`-- SRT Files
```

## [HuggingFace Profile](https://huggingface.co/jpdiazpardo)

* [Dataset](https://huggingface.co/datasets/jpdiazpardo/guturalScream_metalVocals)
* [Model](https://huggingface.co/jpdiazpardo/whisper-tiny-metal)
* [Gradio App](https://huggingface.co/spaces/jpdiazpardo/jpdiazpardo-whisper-tiny-metal)

## YouTube Playlist - [Gutural Speech Recognition](https://www.youtube.com/playlist?list=PLkCTyMdVt0AHgp-80jqskjUtfHo-Ht4xy)
The audio files for the dataset can be downloaded using the following command using and the python script in this repository:
```python
!python youtubetowav.py https://www.youtube.com/playlist?list=PLkCTyMdVt0AHgp-80jqskjUtfHo-Ht4xy
```

## Spectogram visualization
![Alt text](images/spectogram_1.png?raw=true)
![Alt text](images/spectogram_2.png?raw=true)
![Alt text](images/spectogram_3.png?raw=true)
