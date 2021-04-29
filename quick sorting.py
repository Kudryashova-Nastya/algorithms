# Быстрая сортировка Хоара

import time

def quicksort(alist, start, end):
    if end - start > 1:
        p = partition(alist, start, end)
        quicksort(alist, start, p)
        quicksort(alist, p + 1, end)
 
 
def partition(alist, start, end):  # разделение
    pivot = alist[start]  # точка опоры
    i = start + 1
    j = end - 1
 
    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
        while (i <= j and alist[j] >= pivot):
            j = j - 1
 
        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j
 

print('Какое пожелаете количество элементов массива?')
N = int(input())  # указываем файл с каким кол-вом чисел хотим открыть

with open('input' + str(N) + '.txt') as file:  # открываем файл input[N].txt
    string = [row.strip() for row in file]  # и разделяем на строки

arr = string[1].split(' ')  # строку с числами разделяем на массив
arr = [int(arr) for arr in arr]  # присваиваем элементам массива тип integer
#print(arr)  # начальный массив

start_time = time.time()  # время начала сортировки
 
quicksort(arr, 0, len(arr))

finish_time = time.time()  # время окончания сортировки
#print(arr)  # конечный массив

print('Время сортировки:')
print(finish_time - start_time, "seconds")  # длительность сортировки

f = open('output' + str(N) + '.txt', 'w')  # создаём файл output[N].txt

for i in range(N):
    f.write(str(arr[i]) + ' ')  # вписываем отсортированные числа в файл, разделяя пробелами

f.close()
