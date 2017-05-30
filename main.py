import numpy as np
from scipy.io import wavfile
import sounddevice as sd

bpm = 120
beat = 60./bpm  # seconds
fs, d = wavfile.read('sounds/4d.wav')

s_son = len(d)
s_beat = int(fs*beat)
s_sil = s_beat-s_son

s = np.random.uniform(-1, 1, s_sil).astype(np.int16)
v = np.concatenate((2*d, s, d, s, d, s, d, s), axis=0)
while True:
    sd.play(v, fs, blocking=True)
