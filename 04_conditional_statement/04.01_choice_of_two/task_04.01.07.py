"""Роскомнадзор.
Напишите программу, которая определяет, разрешен пользователю доступ к интернет-ресурсу или нет.
Формат входных данных
На вход программе подаётся целое число — возраст пользователя.
Формат выходных данных
Программа должна вывести текст «Доступ разрешен» если возраст не менее 18, и «Доступ запрещен» в противном случае."""

age = int(input())
if age >= 18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')