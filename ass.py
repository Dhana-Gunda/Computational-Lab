import numpy as np
import matplotlib.pyplot as plt
x = np.random.randn(1000)
window_size = 20
energies = []
for k in range(len(x) // window_size):
    start_index = k * window_size
    end_index = start_index + window_size
    window_energy = np.sum(x[start_index:end_index]**2)
    energies.append(window_energy)
plt.plot(energies)
plt.xlabel('Window Index (k)')
plt.ylabel('Energy (E[k])')
plt.title('Energy for every 20 amplitudes')
plt.grid(True)
plt.show()

