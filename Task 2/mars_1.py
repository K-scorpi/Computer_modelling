from numpy import*
from matplotlib.pyplot import*

R1 = 1.496*10e8
T1 = 365.24
Am = 2.28*10e8
Tm = 689.98
E = 0.093
Np = 36000


def x(g):
    return Am*(cos(g)-E)


def y(g):
    return Am*sqrt(1-E**2)*sin(g)


def t(g):
    return Tm*(g-E*sin(g))/2*pi


def X(g):
    return R1*cos(2*pi*t(g)/T1)


def Y(g):
    return R1*sin(2*pi*t(g)/T1)


Ym = array([y(2*pi*i/Np) for i in arange(0,Np,1)])
Xm = array([x(2*pi*i/Np) for i in arange(0,Np,1)])
Xe = array([X(2*pi*i/Np) for i in arange(0,Np,1)])
Ye = array([Y(2*pi*i/Np) for i in arange(0,Np,1)])
t = array([t(2*pi*i/Np) for i in arange(0,Np,1)])

# 1
fig = figure(figsize=(8,4), dpi= 100)
plot(Xe, Ye,  'r', label='Орбита Земли')
plot(Xm, Ym,  'b', label='Орбита Марса')
title('Орбита Земли и Марса в гелиоцентрической ситеме координат')
xlabel('(X(tk), Xg(tk)')
ylabel('Y(t), Yg(t)')
legend()

# 2
Xrelative = (Xm-Xe)
Yrelative = (Ym-Ye)
fig = figure(figsize=(8, 4), dpi=100)
plot(Xrelative, Yrelative,  'r', label='')
title('Положение Марса в системе отсчёта связанной с Землёй')
xlabel('Xg(tk)')
ylabel('Yg(yk)')

# 3
fig = figure(figsize=(8,4), dpi= 100)
y2 = sqrt(Xrelative**2+Yrelative**2)/10e8
x2 = t/365.24
plot(x2, y2)
title('Зависимость расстояния между Землёй и Марсом от времени в годах')
xlabel('t')
ylabel('D(t)')

show()
