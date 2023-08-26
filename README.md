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
|-- LICENSE
`-- Notebooks and Scripts
    |-- Dataset Preprocess Notebook.ipynb
    |-- EDA_gutural_nlp.ipynb
    |-- gutural_nlp.ipynb
    |-- SRT_downloader.ipynb
    |-- preprocess.py
    |-- youtubetowav.py
`-- images
    |-- spectogram 1.png
    |-- spectogram 2.png
    |-- spectogram 3.png
`-- Metadata
    |-- Dataset Lookup.csv
`-- Dashboard
    |-- Gutural Dashboard.pbix
    |-- Dashboard.JPG
`-- SRT Files
```
## [HuggingFace Profile](https://huggingface.co/jpdiazpardo)

* [Dataset](https://huggingface.co/datasets/jpdiazpardo/guturalScream_metalVocals)
  
Speech-to-text dataset with +2.5h of annotated audio, comprised of clean vocals and different gutural sounds, including: low, mid, & high fry screams. The data was built with an eclectic sample of artists from varied sub-genres of hard metal music. Some of the artists included are: Suicide Silence, Lamb of God, Cradle of Filth, Cannibal Corpse and much more (full YouTube playlist available below).
  
* [Model](https://huggingface.co/jpdiazpardo/whisper-tiny-metal)
  
* [Gradio App](https://huggingface.co/spaces/jpdiazpardo/jpdiazpardo-whisper-tiny-metal)

Live demo of the ASR engine. With the transcription, I analyze the emotions present in the lyrics to identify: anger 🤬, disgust 🤢, fear 😨, joy 😀, neutral 😐, sadness 😭, surprise 😲 in a user friendly and interactive spider chart.

## YouTube Playlist - [Gutural Speech Recognition](https://www.youtube.com/playlist?list=PLkCTyMdVt0AHgp-80jqskjUtfHo-Ht4xy)
The audio files for the dataset can be downloaded using the following command with the python script in this repository:
```python
!python youtubetowav.py https://www.youtube.com/playlist?list=PLkCTyMdVt0AHgp-80jqskjUtfHo-Ht4xy
```
or using this [OneDrive link](https://livejaverianaedu-my.sharepoint.com/:f:/g/personal/juandiazp_javeriana_edu_co/EgXL8iZjxP9HsGKI7cbtMNMBOZJYtdVogvN_zX5-p8uC9A?e=gSJ6vR)

## Dashboard
![Alt text](Dashboard/Dashboard.JPG?raw=true)

## Spectogram visualization
![Alt text](images/spectogram_1.png?raw=true)
![Alt text](images/spectogram_2.png?raw=true)
![Alt text](images/spectogram_3.png?raw=true)

## License
**MIT License**

Copyright (c) 2023 Juan Pablo Díaz Pardo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
