import numpy as np


def matrix(n):
    a = np.random.randint(5, size=(n, n))  # print(a)  # выводит матрицу
    s1 = list(a.sum(axis=0))  # столбцы
    s2 = list(a.sum(axis=1))  # строки
    d1 = sum(np.diag(a))  # right
    d2 = sum(np.diag(np.rot90(a)))  # left
    if d1 in (s1 or s2):
        if d2 in (s1 or s2):
            print(f'Сумма одной диагонали {d1}, а второй {d2}')
    elif (d1 or d2) in (s1 or s2):
        print(f'Сумма одной диагонали {d1}')
    else:
        print('Сумм нет')


def auth_login(login):
    handbook = ['Мавпродош', 'Лорнектиф', 'Древерол',
                'Фиригарпиг', 'Клодобродыч']
    if login in handbook:
        print(f'Логин {login} найден. Приятной работы')
    else:
        print(f'Логин {login} не найден. Повторите попытку')
        auth_login((input()))


matrix(int(input('Введите число для размерности матрицы: ')))  # Можно сразу вставить число
auth_login(input('Введите логин: '))
