import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

v0 = 1
g = 10
t = np.arange(0, 1.5, 0.01)
y0 = 10


def V(t):
    global v0, g
    return v0 - g * t


def Y(t):
    global y0, v0, g
    return y0 + (v0 * t) - 0.5 * g * t * t


plt.plot(t, Y(t))
plt.show()
plt.plot(t, V(t))
plt.show()
