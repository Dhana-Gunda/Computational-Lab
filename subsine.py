import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.01)
x2 = np.arange(0,20,0.02)

sin1 = np.sin(x)
sin2 = np.sin(x2)

x2 /= 2

sin3 = sin1-sin2

plt.plot(x,sin3)
plt.show()
