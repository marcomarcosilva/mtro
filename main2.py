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
# sub beat
# wavfile.write('sounds/4dH.wav', fs, np.array(d*0.5, dtype=np.int16))

wf = wave.open('sounds/4d.wav', 'rb')
wH = wave.open('sounds/4dH.wav', 'rb')
p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

bpm = 156
beat = 60./bpm  # seconds
times = 1

fs = wf.getframerate()  # sample frame rate

sample_frames = wf.getnframes()  # SOUND frame number
beat_frames = int(fs*beat)  # BEAT frame number
silence_frames = beat_frames-sample_frames

s = np.zeros(silence_frames, dtype=np.int16).tobytes()

dataH = wH.readframes(CHUNK)
data = wf.readframes(CHUNK)
try:
    while True:
        while dataH != '':
            stream.write(dataH)
            if wH.tell() == wH.getnframes():
                wH.rewind()
                stream.write(s)  # write here the subdivisions
                dataH = wH.readframes(CHUNK)
                break
            dataH = wH.readframes(CHUNK)
        for i in range(0, times-1):
            while data != '':
                stream.write(data)
                if wf.tell() == wf.getnframes():
                    wf.rewind()
                    stream.write(s)  # write here the subdivisions
                    data = wf.readframes(CHUNK)
                    break
                data = wf.readframes(CHUNK)

except KeyboardInterrupt:
    stream.stop_stream()
    stream.close()
    p.terminate()
    # os.remove('sounds/4dH.wav')
    print("end")
