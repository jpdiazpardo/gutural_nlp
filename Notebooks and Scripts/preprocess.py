import os
from spleeter.separator import Separator
import soundfile as sf
import librosa
# Using embedded configuration.
separator = Separator('spleeter:2stems', multiprocess=False)

# # Using custom configuration file.
# separator = Separator('/path/to/config.json')

# Use audio loader explicitly for loading audio waveform :
from spleeter.audio.adapter import AudioAdapter

audio_loader = AudioAdapter.default()
sample_rate = 44100
i=0
loc='C:/Users/jpd0304/Stanley Black & Decker/Diaz, Juan J - Documents/Gutural NLP/Scream Detection Dataset 2/'
for file_name in os.listdir(loc):
    if file_name.endswith(".wav"):
        name=file_name[:-4]
        print(name)
        waveform, _ = audio_loader.load(loc+file_name, sample_rate=sample_rate)
        #waveform,_ = librosa.load(loc+file_name, sr=44100, mono=False)

        # Perform the separation :
        prediction = separator.separate(waveform)
        sf.write('C:/Users/jpd0304/Stanley Black & Decker/Diaz, Juan J - Documents/Gutural NLP/Scream Detection Dataset 2 (Vocals)/'+name+'.wav', prediction['vocals'], 44100)
        #sf.write('./resources/vocal_only_audio/'+name+'_vocal.wav', prediction['vocals'], 44100)
        # if i == 0:
        #     print(prediction['vocals'])
        #     break