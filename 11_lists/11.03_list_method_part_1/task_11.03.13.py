"""k-ая буква слова 🌶️🌶️
На вход программе подается натуральное число n и n строк, а затем число k. Напишите программу, которая выводит
k-ую букву из введенных строк на одной строке без пробелов.
Формат входных данных
На вход программе подается натуральное число n, далее n строк, каждая на отдельной строке. В конце вводится натуральное
число k – номер буквы (нумерация начинается с единицы).
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Примечание. Если некоторые строки слишком короткие, и в них нет символа с заданным номером, то такие строки при выводе
нужно игнорировать."""

lst = [input() for i in range(int(input()))]
k = int(input())
new_list = []
for c in lst:
    if len(c) >= k:
        for i in range(1, len(c) + 1):
            if i == k:
                print(c[i - 1], end='')