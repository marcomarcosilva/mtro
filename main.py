import numpy as np
# from scipy.io import wavfile
import sounddevice as sd
import soundfile as sf

# fs, data = wavfile.read('sounds/4d.wav')
fs, data = sf.read('sounds/4d.wav')
# fs = 44100
# data = np.random.uniform(-1, 1, fs)
v = np.concatenate((data, np.zeros(fs), data, np.zeros(fs)))
print(len(v))
sd.play(data, fs, blocking=True)
