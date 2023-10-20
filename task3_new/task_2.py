import math


def F(mass):
    massive = []
    for x in mass:
        if x > 0:
            massive.append(math.sin(3*x) + math.cos(5*x))
        else:
            massive.append(math.sin(2*x))
    return massive


m = list()
for i in range(int(input())):
    m.append(int(input()))

print(F(m))
