import numpy as np
from scipy.io import wavfile
import sounddevice as sd

bpm = 180
beat = 60./bpm
fs, data = wavfile.read('sounds/4d.wav')

s_son = len(data)
s_beat = int(fs*beat)
s_sil = s_beat-s_son

print(type(data))

# data = np.random.uniform(-1, 1, fs)
# v = np.concatenate((data, np.zeros(s_sil), data, np.zeros(s_sil)))
# print(len(v))
# sd.play(data, fs, blocking=True)
