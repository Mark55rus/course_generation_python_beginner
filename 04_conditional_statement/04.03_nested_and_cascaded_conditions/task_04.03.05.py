"""Среднее число.
Даны три различных целых числа. Напишите программу, которая находит среднее по величине число.
Формат входных данных
На вход программе подаётся три различных целых числа, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести среднее число.
Примечание. Средним называется число, которое будет вторым, если три числа отсортировать в порядке возрастания."""

a, b, c = int(input()), int(input()), int(input())
if a > b and a > c:
    if b > c:
        print(b)
    else:
        print(c)
elif b > a and b > c:
    if a > c:
        print(a)
    else:
        print(c)
elif c > a and c > b:
    if a > b:
        print(a)
    else:
        print(b)
