import numpy as np
import matplotlib.pyplot as plt
lx = 50  
ly = 30  
x = np.random.randn(lx)
y = np.random.randn(ly)
lz = lx + ly - 1 
z = np.zeros(lz)
for k in range(0, lx + ly - 1, 2):
    for n in range(lx):
        if (n + k + 1) <= lz:
            z[n + k] += x[n] * y[n]
plt.stem(z)
plt.xlabel('n')
plt.ylabel('z[n]')
plt.title('z[n] = \Sigma_{t=0}^{n} x[n]y[n+k]')
plt.show()

