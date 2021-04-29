# Сортировка кучей или пирамидальная сортировка

import time

def siftDown(list, heap_size, root_index):  
    # Предположим, что индекс самого большого элемента является корневым индексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    # Если левый потомок корня является допустимым индексом, а элемент больше
    # чем текущий самый большой элемент, то обновляем самый большой элемент
    if left_child < heap_size and list[left_child] > list[largest]:
        largest = left_child
    # Делайте то же самое для right_child
    if right_child < heap_size and list[right_child] > list[largest]:
        largest = right_child
    # Если самый большой элемент больше не является корневым элементом, меняем их местами
    if largest != root_index:
        list[root_index], list[largest] = list[largest], list[root_index]
        # замена дочернего элемента может повлечь за собой изменения ниже по дереву 
        siftDown(list, heap_size, largest)

def heapsort(list):  
    n = len(list)
    # Первый аргумент - начало отсчёта
    # Второй аргумент означает, что мы останавливаемся на элементе перед -1, то есть на нулевом элементе списка
    # Третий аргумент означает, что мы идём в обратном направлении, уменьшая количество i на 1
    for i in range(n, -1, -1):
        siftDown(list, n, i)

    # Перемещаем корень кучи в конец
    for i in range(n - 1, 0, -1):
        list[i], list[0] = list[0], list[i]
        siftDown(list, i, 0)


print('Какое пожелаете количество элементов массива?')
N = int(input())  # указываем файл с каким кол-вом чисел хотим открыть

with open('input' + str(N) + '.txt') as file:  # открываем файл input[N].txt
    string = [row.strip() for row in file]  # и разделяем на строки

arr = string[1].split(' ')  # строку с числами разделяем на массив
arr = [int(arr) for arr in arr]  # присваиваем элементам массива тип integer
#print(arr)  # начальный массив

start_time = time.time()  # время начала сортировки
 
heapsort(arr)

finish_time = time.time()  # время окончания сортировки
#print(arr)  # конечный массив

print('Время сортировки:')
print(finish_time - start_time, "seconds")  # длительность сортировки

f = open('output' + str(N) + '.txt', 'w')  # создаём файл output[N].txt

for i in range(N):
    f.write(str(arr[i]) + ' ')  # вписываем отсортированные числа в файл, разделяя пробелами

f.close()