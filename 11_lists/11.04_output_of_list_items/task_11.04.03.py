"""Значение функции
На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая для каждого
введенного числа x выводит значение функции f(x) = x ** 2 + 2 * x + 1, каждое на отдельной строке.
Формат входных данных
На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести сначала введенные числа, затем пустую строку, а затем соответствующие значения функции.
Примечание. Для первого теста имеем:
f(1) = 1 ** 2 + 2 * 1 + 4, f(2) = 2 ** 2 + 2 * 2 + 1 = 9, f(3) = 3 ** 2 + 2 * 3 + 1 = 16, ..."""

lst = [int(input()) for i in range(int(input()))]
new_lst = []
for i in lst:
    new_lst.append(i ** 2 + 2 * i + 1)
print(*lst, sep='\n')
print()
print(*new_lst, sep='\n')