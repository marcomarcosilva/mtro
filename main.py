import numpy as np
from scipy.io import wavfile
import sounddevice as sd

bpm = 120
beat = 60./bpm  # seconds
fs, data = wavfile.read('sounds/4d.wav')

s_son = len(data)
s_beat = int(fs*beat)
s_sil = s_beat-s_son

print(data)
silence = np.random.uniform(-1, 1, s_sil).astype(np.int16)
v = np.concatenate((2*data, silence, data, silence, data, silence, data, silence), axis=0)
print(v)
while True:
    sd.play(v, fs, blocking=True)
