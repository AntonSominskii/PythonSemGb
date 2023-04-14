# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

print("Введите число монеток: ")
n = int(input())
print("Введите стороны монет через пробел, где O - орел, R - решка: ")
coins = input().split()

num_heads = coins.count('O')
num_tails = coins.count('R') 

if num_heads == n or num_tails == n:
    print(0)
else:
    if num_heads < num_tails:
        side_to_flip = 'O'
    else:
        side_to_flip = 'R'
    
    num_flips = 0
    for i in range(n):
        if coins[i] == side_to_flip:
            coins[i] = 'OR'[coins[i] == 'O']
            num_flips += 1
   
print("Количество монеток, которые нужно перевернуть:",num_flips)