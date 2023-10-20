import math


def sqrt_kor(h):
    a = math.sqrt((abs(math.sin(8 * h)) + 17) /
                   (1 - math.sin(4 * h) * math.cos(h * h + 18)) * 2)
    b = math.sqrt((3) / (3 + abs(math.tan(a * h * h) - math.sin(a * h))))
    c = a * h * h * math.sin(b * h) + b * h * 3 * math.cos(a * h)

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


sqrt_kor(int(input()))
