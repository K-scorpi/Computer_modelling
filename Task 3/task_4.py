import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def F(v, t, g, v1, v2):
    dxdt = v[0]
    dvdt = -(g * (1 - (v[0]**-1/v1**-1)))
    '''
    -(g * (1 - (v[0]/v1)) - (v[0]**-1 / v2) ** 2)
    print(dxdt, dvdt)
    '''
    return [dxdt, dvdt]


v1 = 960
v2 = 0.65
g = 10
y0 = [1, 10]
t = np.linspace(0, 1.5, 50)
sol = odeint(F, y0, t, args=(v1,v2,g,),)
plt.plot(t, sol[:, 1])
plt.show()

