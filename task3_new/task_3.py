import math


def sqrt_kor(a, b, c):
    d = b*b - 4 * a * c
    if d < 0:
        print('Действительных корней нет')
    elif d == 0:
        x = -b/(2 * a)
        print(f'x = {x}')
    elif d > 0:
        x1 = (- b + math.sqrt(d)) / (2 * a)
        x2 = (- b - math.sqrt(d)) / (2 * a)
        print(f'x1 = {x1}')
        print(f'x2 = {x2}')


a1 = int(input())
b1 = int(input())
c1 = int(input())
sqrt_kor(a1, b1, c1)
