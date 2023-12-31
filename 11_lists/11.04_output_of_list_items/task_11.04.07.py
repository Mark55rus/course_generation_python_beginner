"""Google search - 2 🌶️🌶️.
На вход программе подается натуральное число n, затем n строк, затем число k — количество поисковых запросов, затем
k строк — поисковые запросы. Напишите программу, которая выводит все введенные строки, в которых встречаются все
поисковые запросы.
Формат входных данных
На вход программе подаются натуральное число n — количество строк, затем сами строки в указанном количестве, затем
число k, затем сами поисковые запросы.
Формат выходных данных
Программа должна вывести все введенные строки, в которых встречаются все поисковые запросы.
Примечание. Поиск не должен быть чувствителен к регистру символов."""

lst_string = [input() for _ in range(int(input()))]
lst_request = [input() for _ in range(int(input()))]
for string in lst_string:
    count = 0
    for request in lst_request:
        if request.lower() in string.lower():
            count += 1
    if count == len(lst_request):
        print(string)
