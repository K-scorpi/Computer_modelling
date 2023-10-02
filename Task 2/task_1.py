import numpy as np
import matplotlib.pyplot as plt

R1 = 1.486 * 10 ** 8
T1 = 3.156 * 10 ** 7
R2 = 3.844 * 10 ** 5
T2 = 2.36 * 10 ** 6

t = np.arange(0, T1, T1/1000)
# print(t)


def X(t):
    return R1 * np.cos(2 * np.pi * t / T1)


def Y(t):
    return R1 * np.sin(2 * np.pi * t / T1)


def x(t):
    return R2 * np.cos(2 * np.pi * t / T2)


def y(t):
    return R2 * np.sin(2 * np.pi * t / T2)


Xrelative = R2 * np.cos(2 * np.pi * t / T2) + R1 * np.cos(2*np.pi*t/T1)  # Вычисление радиус-вектора x Луны в гелиоцентрической системе координат
Yrelative = R2 * np.sin(2 * np.pi * t / T2) + R1 * np.sin(2*np.pi*t/T1)  # Вычисление радиус-вектора y Луны в гелиоцентрической системе координат

Xe = np.array([X(i) for i in t])
Ye = np.array([Y(i) for i in t])
Xm = np.array([x(i) for i in t])
Ym = np.array([y(i) for i in t])


# print(Xe, Ye)   # Вычисление координаты x радиус-вектора Земли
plt.plot(Xrelative, Yrelative, 'b')
plt.title('Орбита Луны в гелиоцентрической системе координат')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

fig = plt.figure(figsize=(4, 4), dpi=100)
plt.subplot(2, 1, 1)
plt.plot(Xe, Ye, label='Земля')
plt.title('Орбита Земли и орбита Луны')
plt.ylabel('Y')
plt.xlabel('X')
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(Xm, Ym, 'r', label='Луна')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
