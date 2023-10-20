import math


def F(x):
    if x > 0:
        return math.sin(3*x) + math.cos(5*x)
    else:
        return math.sin(2*x)


print(F(int(input())))
