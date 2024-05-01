import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 1, 0.01)

sin_dict = {'s1': [2, 5], 's2': [11, 17], 's3': [12, 20], 's4': [20, 30], 's5': [24, 50]}

h = input('Enter sinusoidal key to generate: ')

if h in sin_dict:
    x = sin_dict[h][0] * np.sin(2 * np.pi * sin_dict[h][1] * t)
    plt.plot(t, x)
    plt.show()
else:
    print("Invalid key entered. Please choose from the following keys:", list(sin_dict.keys()))

