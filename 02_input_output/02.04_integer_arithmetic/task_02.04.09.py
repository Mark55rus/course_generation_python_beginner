"""Следующее и предыдущее.
Напишите программу, которая считывает целое число, после чего на экран
 выводится следующее и предыдущее целое число с пояснительным текстом.
Формат входных данных
На вход программе подаётся целое число.
Формат выходных данных
Программа должна вывести текст согласно условию задачи."""

n = int(input())
print(f'Следующее за числом {n} число: {n + 1}')
print(f'Для числа {n} предыдущее число: {n - 1}')
