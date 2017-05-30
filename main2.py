"""PyAudio Example: Play a WAVE file."""

import pyaudio
import wave
import sys
import numpy as np

CHUNK = 1024

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
while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)
    if wf.tell() == wf.getnframes():
        wf.rewind()
        stream.write(s)

stream.stop_stream()
stream.close()

p.terminate()
