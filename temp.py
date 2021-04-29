# Бинарный поиск
import time
from random import randint

start_time = time.time()

array = []

i = 1000

while i > 0:
    x = randint(0, 1000)
    array.append(x)
    i -= 1

array.sort()

print(array)
print('Какое число ищете?')

value = int(input())

mid = len(array) // 2
low = 0
high = len(array) - 1

while array[mid] != value and low <= high:
    if value > array[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("Не найдено")
else:
    print("ID числа: ", mid)