import numpy as np
from scipy.io import wavfile
import sounddevice as sd

bpm = 180
beat = 60./bpm
fs, data = wavfile.read('sounds/4d.wav')

s_son = len(data)
s_beat = int(fs*beat)
s_sil = s_beat-s_son

print(data)

# data = np.random.uniform(-1, 1, fs)
v = np.concatenate((data, data, data, data), axis=0)
print(v)
sd.play(v, fs, blocking=True)
