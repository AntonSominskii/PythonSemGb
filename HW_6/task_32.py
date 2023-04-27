# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

my_list = [2, 5, 9, 3, 7, 8, 6, 1, 4]
min_val = 3
max_val = 7

indices = [i for i in range(len(my_list)) if my_list[i] >= min_val and my_list[i] <= max_val]

print(indices)