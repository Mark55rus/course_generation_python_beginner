""".com or .ru
На вход программе подается строка текста. Напишите программу, которая проверяет, что строка заканчивается подстрокой
.com или .ru.
Формат входных данных
На вход программе подается строка текста.
Формат выходных данных
Программа должна вывести «YES» если введенная строка заканчивается подстрокой .com или .ru и «NO» в противном случае."""

text = input()
print('YES' if text.endswith('.com') or text.endswith('.ru') else 'NO')
