"""Ревью кода-3
На обработку поступает последовательность из 7 целых чисел. Известно, что вводимые числа по абсолютной величине
не превышают 10 ** 6. Нужно написать программу, которая подсчитывает и выводит сумму всех чётных чисел
последовательности или 0, если чётных чисел в последовательности нет. Программист торопился и написал программу
неправильно.
Найдите все ошибки в этой программе (их ровно 4). Известно, что каждая ошибка затрагивает только одну строку и может
быть исправлена без изменения других строк.
Примечание 1. Число x не превышает по абсолютной величине 10 ** 6, если -10 ** 6 <= x <= 10 ** 6.
Примечание 2. При необходимости вы можете добавить необходимые строки кода.

s = 1
for i in range(1, 7):
    n = input()
    if i % 2 == 0:
        s = s + n
print(s)"""

total = 0
for i in range(3):
    n = int(input())
    if n % 2 == 0:
        total += n
print(total if total else 0)
