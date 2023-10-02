import numpy as np
import matplotlib.pyplot as plt

R1 = 1.486 * 10 ** 8
R2 = 3.844 * 10 ** 5
T2 = 2.36 * 10 ** 6
T1 = 3.156 * 10 ** 7
R22 = 3.3844 * 10 ** 7
t = np.arange(0, T1, T1/1000)


def x(t):
    return R2 * np.cos(2 * np.pi * t / T2)


def y(t):
    return R2 * np.sin(2 * np.pi * t / T2)


Xm = np.array([x(i) for i in t])
Ym = np.array([y(i) for i in t])

Xrelative = R2 * np.cos(2 * np.pi * t / T2) + R1 * np.cos(2*np.pi*t/T1)  # Вычисление радиус-вектора x Луны в гелиоцентрической системе координат
Yrelative = R2 * np.sin(2 * np.pi * t / T2) + R1 * np.sin(2*np.pi*t/T1)  # Вычисление радиус-вектора y Луны в гелиоцентрической системе координат
Xrelative2 = R22 * np.cos(2 * np.pi * t / T2) + R1 * np.cos(2*np.pi*t/T1)  # Вычисление радиус-вектора x Луны в гелиоцентрической системе координат
Yrelative2 = R22 * np.sin(2 * np.pi * t / T2) + R1 * np.sin(2*np.pi*t/T1)  # Вычисление радиус-вектора y Луны в гелиоцентрической системе координат

fig = plt.figure(figsize=(8, 4), dpi=100)
plt.subplot(1, 2, 1)
plt.plot(Xrelative, Yrelative)
plt.title('График орбиты Луны при R2 = 3.844*10^5')
plt.xlabel('x')
plt.ylabel('y')
plt.subplot(1, 2, 2)
plt.plot(Xrelative2, Yrelative2)
plt.title('График орбиты Луны при R2 = 3.844*10^7')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

