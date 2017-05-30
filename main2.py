import pyaudio
import wave
import sys
import numpy as np
from scipy.io import wavfile
import os

CHUNK = 1024

fs, d = wavfile.read('sounds/4d.wav')
# first beat
# wavfile.write('sounds/4dH.wav', fs, 4*d)
# derivate beat
# wavfile.write('sounds/4dl.wav', fs, d/2)

wf = wave.open('sounds/4d.wav', 'rb')
p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

bpm = 120
beat = 60./bpm  # seconds

fs = wf.getframerate()
s_son = wf.getnframes()
s_beat = int(fs*beat)
s_sil = s_beat-s_son

s = np.zeros(s_sil, dtype=np.int16).tobytes()

data = wf.readframes(CHUNK)
try:
    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)
        if wf.tell() == wf.getnframes():
            wf.rewind()
            stream.write(s)

except KeyboardInterrupt:
    stream.stop_stream()
    stream.close()
    p.terminate()
    # os.remove('sounds/4dH.wav')
    # os.remove('sounds/4dl.wav')
    print("end")
