# /home/dmitry/Документы/laby_model_phis_process/lab3/task_3_dvig_bez_trenia.py
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def F(s, t, g):
    dydt = s[1]
    dzdt = -g
    return [dydt, dzdt]


g = 10
y0 = [10, 1]
t = np.linspace(0, 1.5, 150)
sol = odeint(F, y0, t, args=(g,))
fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Графики')
ax1.plot(t, sol[:, 0])
ax2.plot(t, sol[:, 1])
ax1.set_title('Зависимость координаты материальной точки от времени')
ax2.set_title('зависимость скорости движения точки от времени')
for ax in fig.get_axes():
    ax.label_outer()
ax1.grid()
ax2.grid()
plt.show()

