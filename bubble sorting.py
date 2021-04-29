# сортировка пузырьком

import time

print('Какое пожелаете количество элементов массива?')
N = int(input())  # указываем файл с каким кол-вом чисел хотим открыть

with open('input' + str(N) + '.txt') as file:  # открываем файл input[N].txt
    string = [row.strip() for row in file]  # и разделяем на строки

arr = string[1].split(' ')  # строку с числами разделяем на массив
arr = [int(arr) for arr in arr]
#print('Начальный массив:')
print(arr)  # начальный массив

start_time = time.time()  # время начала сортировки

for i in range(N - 1):  # делаем N-1 проходов
    for j in range(N - i - 1):
        if arr[j] > arr[j + 1]:  # сравниваем рядом стоящие элементы и меняем их местами при необходимости
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

finish_time = time.time()  # время окончания сортировки
print('Отсортированный массив:')
print(arr)  # конечный массив


print('Время сортировки:')
print(finish_time - start_time, "seconds")  # длительность сортировки

f = open('output' + str(N) + '.txt', 'w')  # создаём файл output[N].txt

for i in range(N):
    f.write(str(arr[i]) + ' ')  # вписываем отсортированные числа в файл, разделяя пробелами

f.close()
