"""Only even numbers 🌶️
Напишите программу, которая считывает последовательность из 10 целых чисел и определяет является ли
каждое из них четным или нет.
Формат входных данных
На вход программе подаются 10 целых чисел, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести строку «YES», если все числа четные и «NO» в ином случае."""

flag = True
for i in range(10):
    num = int(input())
    if num % 2 != 0:
        flag = False
print('YES' if flag else 'NO')
