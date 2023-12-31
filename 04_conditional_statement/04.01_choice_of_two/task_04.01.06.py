"""Соотношение
Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение:
сумма первой и последней цифр равна разности второй и третьей цифр.
Формат входных данных
На вход программе подаётся одно целое положительное четырёхзначное число.
Формат выходных данных
Программа должна вывести «ДА», если соотношение выполняется, и «НЕТ» — если не выполняется."""

num = int(input())
first_digit = num // 1000
second_digit = num // 100 % 10
third_digit = num // 10 % 10
last_digit = num % 10
if first_digit + last_digit == second_digit - third_digit:
    print("ДА")
else:
    print("НЕТ")
