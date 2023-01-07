'''
   Running this file only will run both the python files and give the desired output
'''

import speech_to_text
import numpy as np
import wave
import struct

def detect_silence_duration(audio_file):
    
    Silence_durations = []
    sampling_freq = 44100
    window = 350
    start = []  
    end = []

    audio_file.rewind()

    file_length = audio_file.getnframes()
    sound = np.zeros(file_length)
    for i in range(file_length):
        data = audio_file.readframes(1)
        data = struct.unpack("<h", data)
        sound[i] = int(data[0])
    sound = np.divide(sound, float(2 ** 15))    
    sound_square = np.square(sound)

    i = 0
    xsum = []

    while(i<(file_length) - window):
        s = 0.00
        j = 0
         
        while(j<=window):
            s = s + sound_square[i + j]
            j = j + 1

        xsum.append(s)
        i = i + window

    i = 0
    fx = 0
    threshold = 0.006

    for i in range(len(xsum)):
        if xsum[i]>threshold and fx==0:
            fx=1
            start.append(i*window)

        elif xsum[i]<threshold and fx==1:
            end.append(i*window)
            fx=0
        
        else:
            continue

    if len(start)!=len(end):
        end.append(i*window)
    
    for z in range(len(start)-1):
        sx = start[z+1]/44100.00
        ex = end[z]/44100.00
        if (sx-ex) >= 1.5:
         Silence_durations.append([round(ex,2),round((sx),2)])

    return Silence_durations

audio_file = wave.open(speech_to_text.p)
Silence_durations = detect_silence_duration(audio_file)
Silence_durations2 = [] 
for i in Silence_durations:
    Silence_durations2.append("Pause from "+str(i))
print(*Silence_durations2,sep=" ")
