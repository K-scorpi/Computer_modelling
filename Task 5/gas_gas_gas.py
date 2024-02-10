import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import random
import math


def InitL(L, NParticle):
    x=np.zeros((NParticle))
    y=np.zeros((NParticle))
    Site=np.zeros((NParticle,NParticle))
    i=0
    while i<=NParticle-1:
        Xadd=math.floor((L+1)*random.random()+1)
        Yadd=math.floor((L+1)*random.random()+1)
        if Xadd==0:
            Xadd=1
        if Yadd==0:
            Yadd=1
        if Site[Yadd][Xadd]==0:
            Site[Xadd][Yadd]=10**307
            x[i]=Xadd
            y[i]=Yadd
            i+=1
    return x,y,Site


def MoveL(L,NParticle,NTrial,x,y,Site):
    X=x
    Y=y
    Site1=Site
    z=np.vstack([X,Y])
    for i in range(0,NTrial):
        for j in range(0, NParticle):
            ITrial=math.floor(NParticle*random.random()-1)
            if ITrial==0:
                ITrial=1
            XTrial=X[ITrial]
            YTrial=Y[ITrial]
            Direction=math.floor(4*random.random()+1)
            if Direction==1:
                XTrial=XTrial+1
                if XTrial>L:
                    XTrial=XTrial-L
            if Direction==2:
                XTrial=XTrial-1
                if XTrial<1:
                    XTrial=L-XTrial
            if Direction==3:
                YTrial=YTrial+1
                if YTrial>L:
                    YTrial=YTrial-L
            if Direction==4:
                YTrial=YTrial-1
                if YTrial<1:
                    YTrial=L-YTrial
            a=XTrial
            b=YTrial
            a=int(a)
            b=int(b)
            if Site1[b][a]==0:
                c=X[ITrial]
                d=Y[ITrial]
                c=int(c)
                d=int(d)
                Site1[d][c]=0
                X[ITrial]=XTrial
                Y[ITrial]=YTrial
                Site1[a][b]=10**307 
        z1=np.vstack([X,Y])
        z=np.vstack([z1,z])
    return z


L=50
NParticle=2000
NTrial=100
Xi,Yi,Site=InitL(L,NParticle)

plt.scatter(Xi,Yi, s=2)
plt.title('Начальная конфигурация')
plt.show()

C=MoveL(L,NParticle,NTrial,Xi,Yi,Site)
dR=[0]*NTrial

for i in range(0,NTrial):
    R2=0
    if i==0 or i%2==0:
        X=C[i]
        Y=C[i+1]
    else:
        Y=C[i]              
        X=C[i+1]
    for j in range(0,NParticle):
        dx=X[j]-Xi[j]
        dy=Y[j]-Yi[j]
        if abs(dx)>L/2:
            dx=dx-dx/abs(dx)*L
        if abs(dy)>L/2:
            dy=dy-dy/abs(dy)*L
        R2=R2+dx**2+dy**2
    dR[i]=R2/NParticle
K=[0]*NTrial
for i in range(0,NTrial):
    K[i]=i
plt.plot(K,dR)
plt.title('Зависимость мгновенных значений среднеквадратического отклонения от равновесного положения')
plt.show()