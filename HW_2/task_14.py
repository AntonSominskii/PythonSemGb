# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

print("Введите число: ")
n = int(input()) 
power_of_two = 1 

while power_of_two <= n:
    print(power_of_two, end=' ')
    
    power_of_two *= 2

print()