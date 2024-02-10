import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import random

##
## НИЖЕ МНОГО КОМЕНТОВ, РАСКОМЕНТИТЬ ПЕРЕД СДАЧЕЙ 
## P.S скорей всего это все одновременно будет работать мучительно долго
## P.P.S поэтому и было закоменчено
##

def Init2(NParticle,R): #функция, возвращающая начальную конфигруацию системы
    XY=np.zeros((NParticle,2))
    for i in range(0,NParticle):
        R0=(2*random.random()-1)*R
        teta=2*np.pi*random.random()
        XY[i][0]=R0*np.cos(teta)
        XY[i][1]=R0*np.sin(teta)  
    return XY


def Move(XY,NParticle,NStep): #функция, возвращающая мгновенные координаты пешеходов
    Z=np.zeros((NParticle,NStep,2))
    for i in range(0,NParticle):
        for j in range(0,NStep):
            prob=random.random()
            if prob<=0.25:
                Z[i][j][0]=XY[i][0]+1
                Z[i][j][1]=XY[i][0]
            if prob>0.25 and prob<=0.5:
                Z[i][j][0]=XY[i][0]-1
                Z[i][j][1]=XY[i][0]
            if prob>0.5 and prob<=0.75:
                Z[i][j][0]=XY[i][0]
                Z[i][j][1]=XY[i][0]-1
            if prob>0.75:
                Z[i][j][0]=XY[i][0]
                Z[i][j][1]=XY[i][0]+1
    return Z


NParticle=2000
NStep=400
R=1
A=Init2(NParticle,R)
Np=2000
X0=[]
Y0=[]
for i in range(1,Np):
    dphi=2*np.pi/(Np-1)
    phi=dphi*(i-1)
    x=np.cos(phi)
    y=np.sin(phi)
    X0.append(x)
    Y0.append(y)
'''
plt.subplot(1,1,1)
plt.plot(X0,Y0)

plt.subplot(1,1,1)
plt.title('Начальная конфигурация пешеходов на плоскости')
plt.xlabel('X')
plt.ylabel('Y')
plt.scatter(A[:,0],A[:,1],s=0.2)
plt.show()
'''
Am=Move(A,NParticle,NStep)
K=[0]*NStep
for i in range(1,NStep):# массив шагов монте карло
    K[i]=i


# расчет зависимости координаты х,у от шага монте карло для 1-ого и 100-ого пешехода(сойдет)
''' 
plt.subplot(1,1,1)
plt.plot(K,Am[0][:,0])
plt.title('зависимости координаты х,у от шага монте карло для 1-ого и 100-ого пешехода')

plt.subplot(1,1,1)
plt.plot(K,Am[99][:,0])

plt.show()
'''

# расчет зависимости радиус векторов для первого и сотого пешеходов
'''
R1=[0]*NStep
R100=[0]*NStep
for i in range(0,NStep):
    R1[i]=(Am[0][i][0]**2+Am[0][i][1]**2)**0.5
    R100[i]=(Am[99][i][0]**2+Am[99][i][1])**0.5
print(R1)
plt.subplot(1,1,1)
plt.title('зависимости радиус векторов для первого и сотого пешеходов')
plt.plot(K,R1)

plt.subplot(1,1,1)
plt.plot(K,R100)
plt.show()
'''
#вычисление зависимости усредненных координат от шага монте карло
'''
sum_sr_x=0
sum_sr_y=0
SR_X=[]
SR_Y=[]
k=0
for i in range(0,NStep):
    for j in range(1,NParticle):
        sum_sr_x+=Am[j][i][0]
        sum_sr_y+=Am[j][i][1]
        k+=1
    SR_X.append(sum_sr_x/k)
    SR_Y.append(sum_sr_y/k)
    sum_sr_x=0
    sum_sr_y=0
    k=0
'''
'''
plt.subplot(1,1,1)
plt.title('Зависимость усредненных по ансамблю координат x и y')
plt.plot(K,SR_X)

plt.subplot(1,1,1)
plt.plot(K,SR_Y)

plt.show()
'''

#вычисление радиус векторов усредненных по ансаамблю
'''
R_SR=[]
for i in range (0,NStep):
        R_SR.append(((SR_X[i])**2+(SR_Y[i])**2)**0.5)

plt.plot(K,R_SR)
plt.title('заивисимость радиус вектора усредненного по ансамблю от шага монте карло')
plt.show()
'''

#вычисление среднеквадратичного отклонения("Сомнительно, но ок")
'''
SR_KV_X=[]
SR_KV_Y=[]
R_KV_O=[0]*NStep
sum_sr_kv_x=0
sum_sr_kv_y=0
for i in range(0,NStep):
    for j in range(0,NParticle):
        sum_sr_kv_x+=Am[j][i][0]**2
        sum_sr_kv_y+=Am[j][i][1]**2
        k+=1
    SR_KV_X.append(sum_sr_kv_x/k)
    SR_KV_Y.append(sum_sr_kv_y/k)
    k=0
    R_KV_O[i]=SR_KV_X[i]+SR_KV_Y[i]-SR_X[i]**2-SR_Y[i]**2
print(R_KV_O)
plt.plot(K,R_KV_O)
plt.title('среднеквадратичного отклонения')
plt.show()
'''


def Walk2(NStep,NTrial,p,x0,dx): # офигеть, ходьба два уже вышла
    XY=np.zeros((NTrial,NStep))
    for i in range(0,NTrial-1):
        x=x0
        d=dx
        for j in range(0,NStep-1):
            if p<random.random():
                d=-d
            x=x+d
            XY[i][j]=x
    return XY


NStep=1000
NTrial=1000
p=0.5
x0=0
dx=1

M=Walk2(NStep,NTrial,p,x0,dx)

#вычисление мгновенных значений среднего по ансамблю пешеходов
X=np.zeros((NTrial,NStep)) #массив смещений
for i in range(0,NStep):
    for j in range(0,NTrial):
        X[j][i]=M[j][i]

sum_sr=0
X_SR=[]
for i in range(0,NTrial):
    for j in range(0,NStep):
        sum_sr+=X[i][j]
    X_SR.append(sum_sr/NStep)
    sum_sr=0
# вычисление мгновенных значений среднего по ансамблю пешеходов квадрата среднего
X_KV_SR=[]
sum_kv_sr=0
for i in range(0,NTrial):
    for j in range(0,NStep):
        sum_kv_sr+=M[i][j]**2
    X_KV_SR.append(sum_kv_sr/NStep)
# вычисление и визуализация мгновенных значений среднеквадратичного отклонения пешехода
# от начальной точки, усредненных по ансамблю
K=[0]*NStep
for i in range(0,NStep):
    K[i]=i+1
Xs=[]
for i in range(0,NStep):
    Xs.append(X_KV_SR[i]-X_SR[i]**2)
plt.plot(K,Xs)
plt.title('Зависимость мгновенных значений среднеквадратичного отклонения пешехода')
plt.show()
