"""Делители-1 🌶️.
На вход программе подается два натуральных числа a и b (a < b). Напишите программу, которая находит натуральное число
из отрезка [a;b] с максимальной суммой делителей.
Формат входных данных
На вход программе подаются два числа, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести два числа на одной строке, разделенных пробелом: число с максимальной суммой делителей и сумму
его делителей.
Примечание. Если таких чисел несколько, то выведите наибольшее из них."""

a, b = int(input()), int(input())
digit = 0
total_div = 0
for i in range(a, b + 1):
    num = i
    total = 0
    for j in range(1, i + 1):
        if i % j == 0:
            total += j
    if total >= total_div:
        digit = i
        total_div = total
print(digit, total_div)