import numpy as np
import matplotlib.pyplot as plt


R1 = 1.486 * 10 ** 8
T1 = 3.156 * 10 ** 7
R2 = 3.844 * 10 ** 5
T2 = 2.36 * 10 ** 6
dt = T1/2000
t = np.arange(0, T1, dt)


def X(t):
    return R1 * np.cos(2 * np.pi * t / T1)


def Y(t):
    return R1 * np.sin(2 * np.pi * t / T1)


def x(t):
    return R2 * np.cos(2 * np.pi * t / T2)


def y(t):
    return R2 * np.sin(2 * np.pi * t / T2)


Xrelative = R2 * np.cos(2 * np.pi * t / T2) + R1 * np.cos(2*np.pi*t/T1) # Вычисление радиус-вектора x Луны в гелиоцентрической системе координат
Yrelative = R2 * np.sin(2 * np.pi * t / T2) + R1 * np.sin(2*np.pi*t/T1) # Вычисление радиус-вектора y Луны в гелиоцентрической системе координат

Xe = np.array([X(i) for i in t])
Ye = np.array([Y(i) for i in t])
Xm = np.array([x(i) for i in t])
Ym = np.array([y(i) for i in t])


def Vx(t):
    return -2*np.pi/T1*R1*np.sin(2*np.pi/T1*t)


def Vy(t):
    return 2*np.pi/T1*R1*np.cos(2*np.pi/T1*t)


def vx(t):
    return -2*np.pi/T2*R2*np.sin(2*np.pi/T2*t)


def vy(t):
    return 2*np.pi/T2*R2*np.cos(2*np.pi/T2*t)


def V(t):
    return np.sqrt(Vx(t)**2+Vy(t)**2)-(Vx(t)*vx(t)+Vy(t)*vy(t))/(np.sqrt(Vx(t)**2+Vy(t)**2))


V = np.array([V(i) for i in t])

f = plt.figure(figsize=(10, 3))
ax = f.add_subplot(121)
ax2 = f.add_subplot(122)

ax.plot(Xe, Ye, 'b', label='Земли')
ax.plot(Xrelative, Yrelative, 'r', label='Луна')
ax.set_title('Орбита Земли')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()

ax2.plot(t, V)
ax2.set_title('График скорости Луны')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
plt.show()
