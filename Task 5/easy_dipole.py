import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp,odeint
import math


###
### ООО "ПАКОСТИ КОРПАРАЙТЕД" (Трепещи Перри-Утконос, я изобрел похититель 74,5 ГБ оперативы-инатор)
###


def Dipol(t, states):
    global M
    y=states
    z=np.zeros((6))
    r=np.array([y[0],y[2],y[4]])
    rt=np.array([[y[0]],[y[2]],[y[4]]])
    
    Hx=3*np.dot(M,rt)*r[0]/((np.dot(r,rt))**2.5)-M[0]/((np.dot(r,rt))**1.5)
    Hy=3*np.dot(M,rt)*r[1]/((np.dot(r,rt))**2.5)-M[1]/((np.dot(r,rt))**1.5)
    Hz=3*np.dot(M,rt)*r[2]/((np.dot(r,rt))**2.5)-M[2]/((np.dot(r,rt))**1.5)
    z[0]=y[1]
    z[1]=2*np.pi*(Hz*y[3]-Hy*y[5])
    z[2]=y[3]
    z[3]=2*np.pi*(Hx*y[5]-Hz*y[1])
    z[4]=y[5]
    z[5]=2*np.pi*(Hy*y[1]-Hx*y[3])

    return z


global M
V0=1.55
M=[0,np.sin(11.5*np.pi/180),np.cos(11.5*np.pi/180)]
state0 = [1.0, 0.0, 0.0, V0, 0.0, 0.0]

Tmax=100
Ts=1
t = np.arange(0.0, Tmax+Ts, Ts)
states=solve_ivp(Dipol,[0,100],state0,method='RK45')
t=states.t
y=states.y

###### 1 график
POBEDA=plt.figure().add_subplot(projection='3d')
POBEDA.plot(y[0],y[2],y[4])
POBEDA.set_xlabel('X')
POBEDA.set_ylabel('Y')
POBEDA.set_zlabel('Z')
plt.title('траектория заряда')
plt.show() # "Круто! Да это ж круто!" @ Олег Тиньков


# вычисление вектора скорости
# он же график №2 "Итс окей" @ Олег Тиньков
vx=y[1]
vy=y[3]
vz=y[5]
V=[]
for i in range (0,len(vx)):
    V.append((vx[i]**2+vy[i]**2+vz[i]**2)**0.5)
V0=V[0]
dE=[]
for i in range(0,len(V)):
    dE.append((V0-V[i])*100/V0)
plt.plot(t,dE)
plt.xlabel('t')
plt.ylabel('dE')
plt.title('Зависимость разности между начальным и \n текущими значениями кинетической энергии заряда от времени')
plt.show()

# вычисление напряженности магнитного поля и магнитного момента     "Ну сколько можно" @ Олег Тиньков
# он же график №3
x_H=y[0]
y_H=y[2]
z_H=y[4]
H=[]
HV=[]
I=[]
Hx_m=[]
Hy_m=[]
Hz_m=[]
V2=[]
for i in range(0,len(y[0])):
    Hx=((3*(x_H[i]*M[0]+y_H[i]*M[1]+z_H[i]*M[2]))*x_H[i])/(x_H[i]**2+y_H[i]**2+z_H[i]**2)**2.5-M[0]/((x_H[i]**2+y_H[i]**2+z_H[i]**2)**1.5)
    Hy=((3*(x_H[i]*M[0]+y_H[i]*M[1]+z_H[i]*M[2]))*y_H[i])/(x_H[i]**2+y_H[i]**2+z_H[i]**2)**2.5-M[1]/((x_H[i]**2+y_H[i]**2+z_H[i]**2)**1.5)
    Hz=((3*(x_H[i]*M[0]+y_H[i]*M[1]+z_H[i]*M[2]))*z_H[i])/(x_H[i]**2+y_H[i]**2+z_H[i]**2)**2.5-M[2]/((x_H[i]**2+y_H[i]**2+z_H[i]**2)**1.5)
    Hx_m.append(Hx)
    Hy_m.append(Hy)
    Hz_m.append(Hz)
    h=(Hx**2+Hy**2+Hz**2)**0.5
    H.append(h)
    hv=Hx*vx[i]+Hy*vy[i]+Hz*vz[i]
    HV.append(hv)
    v2=V[i]**2-(hv/h)**2
    V2.append(v2)
    I.append(v2/h)

plt.plot(t,I)
plt.xlabel('t')
plt.ylabel('I')
plt.title('Зависимость магнитного момента заряда от времени')
plt.show()
 # "Я заплакал" @ Олег Тиньков

# кэф неоднородности поля 
# он еж график №4 (да он еж)
dr=10**(-5)
K=[]
for i in range(0,len(y[0])):
    x1=x_H[i]-dr
    y1=y_H[i]-dr
    z1=z_H[i]-dr
    dHx=(3*(x1*M[0]+y1*M[1]+z1*M[2])*x1)/((x1**2+y1**2+z1**2)**2.5)-M[0]/((x1**2+y1**2+z1**2)**1.5)
    dHy=(3*(x1*M[0]+y1*M[1]+z1*M[2])*y1)/((x1**2+y1**2+z1**2)**2.5)-M[1]/((x1**2+y1**2+z1**2)**1.5)
    dHz=(3*(x1*M[0]+y1*M[1]+z1*M[2])*z1)/((x1**2+y1**2+z1**2)**2.5)-M[2]/((x1**2+y1**2+z1**2)**1.5)
    H1=(dHx**2+Hy_m[i]**2+Hz_m[i]**2)**0.5
    H2=(Hx_m[i]**2+dHy**2+Hz_m[i]**2)**0.5
    H3=(Hx_m[i]**2+Hy_m[i]**2+dHz**2)**0.5
    G1=(H[i]-H1)/dr
    G2=(H[i]-H2)/dr
    G3=(H[i]-H3)/dr
    G=(G1**2+G2**2+G3**2)**0.5
    k=((V2[i]**0.5)*G)/(2*np.pi*H[i])
    K.append(k)
plt.plot(t,K)
plt.xlabel('t')
plt.ylabel('K')
plt.title('Зависимость коэффициента неоднородности поля от времени')
plt.show()
 # "Нуууууу" @ Олег Тиньков

# Разность модулей радиусов-векторов зарядов, находившихся в начальный момент времени в близких точках.
# он же график №5 
R=[]
dx=10**(-4)
for i in range(0,len(y[0])):
    r=(x_H[i]**2+y_H[i]**2+z_H[i]**2)**0.5
    R.append(r)
state01 = [1.0+dx, 0.0, 0.0, V0, 0.0, 0.0]
states1=solve_ivp(Dipol,[0,40],state01,method='RK45')
t_new=states1.t
y_new=states1.y
x2=y_new[0]
y2=y_new[2]
z2=y_new[4]
dR=[]
for i in range(0,len(x2)):
    r2=(x2[i]**2+y2[i]**2+z2[i]**2)**0.5
    dr=R[i]-r2
    dR.append(dr)

plt.plot(t_new,dR)
plt.xlabel('t')
plt.ylabel('dR')
plt.title('Разность модулей радиусов-векторов зарядов, находившихся в начальный момент времени в близких точках')
plt.show()

# зависимость радиус вектора от времени
# он же график №6

plt.plot(t,R)
plt.xlabel('t')
plt.ylabel('R')
plt.title('Зависимость модуля радиуса-вектора от времени')
plt.show()
 # "я так чувствую" @ Олег Тиньков

# зависимость скорости изменения модуля радиуса-вектора от времени
# он же график №7
v=np.diff(R)
t=t[:len(t)-1]

plt.plot(t,v)
plt.xlabel('t')
plt.ylabel('V')
plt.title('Зависимость скорости изменения модуля радиуса-вектора от времени')
plt.show()

# спектр зависимости
# он же график №8
Fmax=1/Ts
df=1/Tmax
f=[0]*100
sum=0
for i in range(0,len(f)):
    sum+=df
    f[i]=sum
a=np.fft.fft(R)
b=abs(a)
S=[]
for i in range(0,len(b)):
    s=b[i]/max(b)
    S.append(s)
S=S[:100]

plt.plot(f,S)
plt.title('Спектр функции')
plt.xlabel('f')
plt.ylabel('S/Smax')
plt.show()