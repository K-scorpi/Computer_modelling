import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
N=100
x0=0
y0=1
h=0.304
def f(x:float,y:float) -> float :
    return x-(y*y)
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
    #print(Y)
#print(Y)
plt.plot(X,Y)
plt.show()

