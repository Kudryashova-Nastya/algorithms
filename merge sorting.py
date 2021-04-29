# Сортировка слиянием
# Сначала разбиваем массив на массивы по одному элементу, затем попарно начинаем их сливать

import time

def merge_sort(alist, start, end):
    if end - start > 1:
        mid = (start + end)//2  # целочисленное деление
        merge_sort(alist, start, mid)
        merge_sort(alist, mid, end)
        merge_list(alist, start, mid, end)
 
def merge_list(alist, start, mid, end):
    left = alist[start:mid] # массив от начала до середины
    right = alist[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            alist[k] = left[i]
            i = i + 1
        else:
            alist[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            alist[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            alist[k] = right[j]
            j = j + 1
            k = k + 1
 
 
print('Какое пожелаете количество элементов массива?')
N = int(input())  # указываем файл с каким кол-вом чисел хотим открыть

with open('input' + str(N) + '.txt') as file:  # открываем файл input[N].txt
    string = [row.strip() for row in file]  # и разделяем на строки

arr = string[1].split(' ')  # строку с числами разделяем на массив
arr = [int(arr) for arr in arr]  # присваиваем элементам массива тип integer
#print(arr)  # начальный массив

start_time = time.time()  # время начала сортировки
 
merge_sort(arr, 0, len(arr))

finish_time = time.time()  # время окончания сортировки
#print(arr)  # конечный массив

print('Время сортировки:')
print(finish_time - start_time, "seconds")  # длительность сортировки

f = open('output' + str(N) + '.txt', 'w')  # создаём файл output[N].txt

for i in range(N):
    f.write(str(arr[i]) + ' ')  # вписываем отсортированные числа в файл, разделяя пробелами

f.close()