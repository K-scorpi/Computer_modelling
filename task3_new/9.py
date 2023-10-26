import random
print("Введите количество столбцов")
columns = int(input())
print("Введите количество строк")
strings = int(input())
print("Введите номер строки. которую нужно отсортировать")
numberStr = int(input())-1
arr = [[0] * columns for i in range(strings)]
for i in range(strings):
    for x in range(columns):
        arr[i][x] = random.randint(0,100)

print(arr)
arr[numberStr].sort()
print(f"Массив с отсортированной строкой {numberStr+1}")
print(arr)