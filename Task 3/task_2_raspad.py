import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
N=1000 #временной промежуток
x0=0
y0=10000 #начальное количество ядер
h=0.15
def f(x:float,y:float) -> float :
    return -h*y
X=[]
Y=[]
Y.append(y0)
X.append(x0)
x=0
i=0
while i<N:
    x+=h
    i+=1
    X.append(x)
    Y.append(Y[i-1]+h*f(X[i-1],Y[i-1]))
plt.title('распад ядер')
plt.ylabel('количество ядер')
plt.xlabel('время')
plt.plot(X,Y)
plt.show()

