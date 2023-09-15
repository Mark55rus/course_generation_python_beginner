"""Сортировка трёх 🌶️.
Напишите программу, которая упорядочивает три числа от большего к меньшему.
Формат входных данных
На вход программе подается три целых числа, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести три числа, каждое на отдельной строке, упорядоченных от большего к меньшему."""

n1, n2, n3 = [int(input()) for _ in range(3)]
largest = max(n1, n2, n3)
smallest = min(n1, n2, n3)
average = (n1 + n2 + n3) - smallest - largest
print(largest, average, smallest, sep='\n')