import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp,odeint


def LorenzForce(t,z):
    global H
    H=[0,0,1]
    f=np.zeros((6))
    f[0]=z[1]
    f[1]=2*np.pi*(H[2]*z[3]-H[1]*z[5])
    f[2]=z[3]
    f[3]=-2*np.pi*(H[2]*z[1]-H[0]*z[5])
    f[4]=z[5]
    f[5]=2*np.pi*(z[1]*H[1]-z[3]*H[0])
    return f

# z=odeint(LorenzForce,[0,0,0, 0.1, 0, 0.01],[0.10/1024])
x0 = 0
y0 = 0
z0 = 0
vx0 = 0.1
vy0 = 0
vz0 = 0.01
z=solve_ivp(LorenzForce, [0,10], [x0, y0, z0,vx0,vy0,vz0], max_step=10/1024)
t = z.t
y = z.y

# 3D график
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


