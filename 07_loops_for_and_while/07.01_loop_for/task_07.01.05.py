"""Звездный прямоугольник.
На вход программе подается натуральное число n. Напишите программу, которая печатает звездный прямоугольник размерами
n × 19.
Формат входных данных
На вход программе подаётся натуральное число n∈[1;20] — высота звездного прямоугольника.
Формат выходных данных
Программа должна вывести звездный прямоугольник размерами n × 19."""

n = int(input())
for i in range(n):
    print('*' * 19)