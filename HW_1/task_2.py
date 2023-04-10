# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
print("Задача №2:")
number = int(input("Введите трехзначное число: "))

digit1 = number // 100
digit2 = (number // 10) % 10
digit3 = number % 10

sum_of_digits = digit1 + digit2 + digit3

print("Сумма цифр трехзначного числа: ", sum_of_digits)