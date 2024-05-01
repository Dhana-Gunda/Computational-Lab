import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0, 2*np.pi, 0.01)
y1 = np.sin(t)
y2 = np.cos(t)
y3 = np.sin(3*t)
y4 = np.cos(2*t)

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(t, y1)
plt.title('sin(t)')

plt.subplot(2, 2, 2)
plt.plot(t, y2)
plt.title('cos(t)')

plt.subplot(2, 2, 3)
plt.plot(t, y3)
plt.title('sin(3t)')

plt.subplot(2, 2, 4)
plt.plot(t, y4)
plt.title('cos(2t)')

plt.tight_layout()  
plt.show()
