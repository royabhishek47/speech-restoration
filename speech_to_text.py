'''
   Running the silence_duration.py file will only run both the python files and give the desired output
'''

import noisereduce as nr
import librosa
import speech_recognition as sr
import wavio

path = "D:/Python/SR2.0/voices.wav"     # Change the path accordingly
data, rate = librosa.load(path)

reduced_noise = nr.reduce_noise(y = data, sr=rate, n_std_thresh_stationary=2,stationary=True)

p = 'D:/Python/SR2.0/voice1.wav'        # Change the path accordingly

wavio.write(p, data, rate, sampwidth=2)
AUDIO_FILE = p

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)                
        print(r.recognize_google(audio))
        print()