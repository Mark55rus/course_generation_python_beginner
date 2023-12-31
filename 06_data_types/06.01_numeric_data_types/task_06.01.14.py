"""Интересное число.
Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней по величине цифре.
Напишите программу, которая определяет интересное число или нет. Если число интересное, следует вывести –
«Число интересное» иначе «Число неинтересное».
Формат входных данных
На вход программе подается целое трехзначное число.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи."""

num = int(input())
first = num // 100
second = num // 10 % 10
last = num % 10
largest = max(first, second, last)
smallest = min(first, second, last)
average = first + second + last - largest - smallest
print('Число интересное' if largest - smallest == average else 'Число неинтересное')

# variant 2:
# first, second, last = [int(i) for i in ' '.join(input()).split()]
# largest = max(first, second, last)
# smallest = min(first, second, last)
# average = first + second + last - largest - smallest
# print('Число интересное' if largest - smallest == average else 'Число неинтересное')
