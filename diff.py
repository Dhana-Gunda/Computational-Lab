import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the differential equation dy/dt = f(t, y)
def myODE(y, t):
    return -0.5 * y

# Define the time span
t = np.linspace(0, 10, 100)  # Time points for the solution

# Define the initial condition
y0 = 1

# Solve the differential equation
y = odeint(myODE, y0, t)

# Plot the solution
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.title('Solution of the Differential Equation')
plt.show()
