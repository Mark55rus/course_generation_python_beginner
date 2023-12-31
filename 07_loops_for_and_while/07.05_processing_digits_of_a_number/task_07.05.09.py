"""Одинаковые цифры.
Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
Формат входных данных
На вход программе подается одно натуральное число.
Формат выходных данных
Программа должна вывести «YES» если число состоит из одинаковых цифр и «NO» в противном случае."""

num = int(input())
flag = True
last_digit = num % 10
while num != 0:
    if last_digit == num % 10:
        last_digit = num % 10
        num //= 10
    else:
        flag = False
        break
print("YES" if flag else "NO")
