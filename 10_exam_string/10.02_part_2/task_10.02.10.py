"""Второе вхождение.
На вход программе подается строка текста. Напишите программу, которая выводит индекс второго вхождения буквы «f».
Если буква «f» встречается только один раз, выведите число -1, а если не встречается ни разу, выведите число -2.
Формат входных данных
На вход программе подается строка текста.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи."""

text = input()
if text.count('f') == 1:
    print(-1)
elif text.count('f') == 0:
    print(-2)
else:
    text = text.replace('f', '!', 1)
    print(text.find('f'))
