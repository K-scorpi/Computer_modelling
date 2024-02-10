import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import random
import scipy
from math import*


def Walk(NStep,NTrial,p):
    X=[0]*(NTrial+1)
    for i in range(2,NTrial):
        x=0
        for j in range (1, NStep):
            r=random.random()
            #print(r)
            if p>=r:
                x+=1
            else:
                x-=1

        X[i]=x
    return X


NStep=1000
NTrial=1000
p=0.5
kk=[0]*(NTrial+1)
for i in range(1,NTrial):
    kk[i]=i

M=Walk(NStep,NTrial,p)
#Ниже временный коммент, чтобы не мешало

''' 
plt.plot(kk,M)
plt.title('Случайная последовательность возвращенная функцией')
plt.show()


plt.hist(M,bins=100)
plt.title('Гистограмма для случайной последовательности')
plt.show()
'''

#вычисление среднего арифметического
sum_sr = 0
for i in range(len(M)):
    sum_sr+=abs(M[i])
srednee = sum_sr/(len(M))
print("Среднее отклонение: ",srednee)

# вычисление среднего квадратического, оно же сигма
sum_kv = 0
for i in range(len(M)):
    sum_kv+=(M[i]-srednee)**2
srednee_kvadratichnoe = np.sqrt(sum_kv/len(M))
print("Среднее квадтратичное отклонение: ",srednee_kvadratichnoe)

# вычисление коэффициента Xi^2
X0=srednee
sigma=srednee_kvadratichnoe
Ni=50
Xmin=min(M)
Xmax=max(M)
dx=(Xmax-Xmin)/(Ni-1)
'''
def x(k):
    return Xmin+dx*(k-1)

def integral(x):
    return NTrial*(scipy.stats.norm.pdf(x,X0,sigma))

Xi=0
result_of_integral=[0]*Ni
s=plt.hist(M,Ni)
Nf=20
for i in range(1,Ni):
    v, err=scipy.integrate.quad(integral,x(i),x(i+1))
    result_of_integral[i]=v
result_of_x=[0]*Ni
for i in range (1,Ni):
    X1=x(i)
    X2=x(i)
    dx=(X2-X1)/(Nf-1)
    x1=X1+dx*(i-1)
    result_of_x[i]=x1
v=np.trapz(result_of_x,result_of_integral)
print(v)

for i in range(1,Ni):
   Xi=Xi+(s[0][i]-v)**2/v
   print(Xi)
''' # спросить что за херня

print("Xi экспериментальное: ",scipy.stats.chi2.ppf(0.995, Ni-1-3))


#Построение гистограммы, показывающей вероятность нахождения пешехода в этой точке
X=[]
Y=[]
def Distr(M):
    M1=min(M)
    M2=max(M)
    k=M1
    KKK=1
    while k<=M2:
        n=0
        for i in range(1, len(M)):
            if k==M[i]:
                n+=1
        X.append(k)
        Y.append(n/len(M))
        KKK+=1
        k+=1
Distr(M)
plt.plot(X,Y)
plt.title('Вероятность нахождения пешохода в конкретной точке') 
plt.show()
