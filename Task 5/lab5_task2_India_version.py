import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp,odeint


def LorenzForce(t,z):
    global H,B
    f=np.zeros((6))
    f[0]=z[1]
    f[1]=(H[0]+z[3]*B[2]-z[5]*B[1])
    f[2]=z[3]
    f[3]=(H[1]+z[5]*B[1]-z[1]*B[2])
    f[4]=z[5]
    f[5]=(H[2]+z[1]*B[1]-z[3]*B[1])
    return f

H=[0,1,0] # Задаем вектор электрического поля
B=[0,0,1] # Задаем вектор магнитного поля
x0 = 0
y0 = 10
z0 = 0
vx0 = 0
vy0 = 0
vz0 = 0
z=solve_ivp(LorenzForce, [0,100], [x0, y0, z0,vx0,vy0,vz0], max_step=10/1024)
t = z.t
y = z.y

#3D график
az=plt.figure().add_subplot(projection='3d')
az.plot(y[0],y[2],y[4])
az.set_title("Траектория движения заряда постоянном магнитном поле")
az.set_xlabel("X")
az.set_ylabel("Y")
az.set_zlabel("Z")
plt.show()

#проекция на OXY
plt.plot(y[0],y[2])
plt.title("Проекция траектории на плоскость OXY")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# проекция на OZY
plt.plot(y[2],y[4])
plt.title("Проекция траектории на OZY")
plt.ylabel("Z")
plt.xlabel("Y")
plt.show()