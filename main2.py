import pyaudio
import wave
import sys
import numpy as np
from scipy.io import wavfile
import os

CHUNK = 1024

# fs, d = wavfile.read('sounds/4d.wav')
# first beat
# wavfile.write('sounds/4dH.wav', fs, 4*d)

wf = wave.open('sounds/4d.wav', 'rb')
wH = wave.open('sounds/4dH.wav', 'rb')
p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

bpm = 151
beat = 60./bpm  # seconds
times = 3

fs = wf.getframerate()
s_son = wf.getnframes()
s_beat = int(fs*beat)
s_sil = s_beat-s_son

s = np.zeros(s_sil, dtype=np.int16).tobytes()

dataH = wH.readframes(CHUNK)
data = wf.readframes(CHUNK)
try:
    while True:
        while dataH != '':
            stream.write(dataH)
            if wH.tell() == wH.getnframes():
                wH.rewind()
                stream.write(s)
                dataH = wH.readframes(CHUNK)
                break
            dataH = wH.readframes(CHUNK)
        for i in range(0, times-1):
            while data != '':
                stream.write(data)
                if wf.tell() == wf.getnframes():
                    wf.rewind()
                    stream.write(s)
                    data = wf.readframes(CHUNK)
                    break
                data = wf.readframes(CHUNK)

except KeyboardInterrupt:
    stream.stop_stream()
    stream.close()
    p.terminate()
    # os.remove('sounds/4dH.wav')
    print("end")
