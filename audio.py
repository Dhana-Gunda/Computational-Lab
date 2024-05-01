import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
file_path = '/home/rguktrkvalley/python(Cl)/Chorus.wav'

sample, data_audio = wavfile.read(file_path)

timing= np.arange(len(data_audio)) / sample

plt.plot(timing,data_audio)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Audio Signal')
plt.show()
