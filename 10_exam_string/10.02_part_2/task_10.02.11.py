"""Переворот.
На вход программе подается строка текста в которой буква «h» встречается как минимум два раза.
Напишите программу, которая возвращает исходную строку и переворачивает последовательность символов, заключенную между
первым и последним вхождением буквы «h».
Формат входных данных
На вход программе подается строка текста.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи."""

text = input()
start = text.find('h')
end = text.rfind('h')
new_text = ''
for i in range(start, end + 1):
    new_text = text[i] + new_text
print(text[:start] + new_text + text[end + 1:])