"""
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
"""
import random

num_array_elem  = int(input('Введие кол-во элементов массива: '))

array = [random.randint(1, num_array_elem) for _ in range(num_array_elem)]
print (array)

number = int(input('Введите число которое хотите найти '))

dif = abs(number - array[0])
count = array[0]

for i in array:
    if dif > abs(number - i):
        count = i
        dif = abs(number - i)
        if dif == 0:
            break
        
print(f'Самое близкое число к {number} число {count}')