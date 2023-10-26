from math import cos, e

print("Введите a")
a = int(input())
print("Введите b")
b = int(input())

def midrectangle(f, a, b, n):
    h = (b-a)/100
    result = 0
    for i in range(n):
        result += f(a+(i+0.5)*h)*h
    return result
def f(x):
    return(cos(e**x))
print(round(midrectangle(f,a,b,100),6))
