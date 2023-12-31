"""Три города.
Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
Формат входных данных
На вход программе подаётся названия трех городов, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.
Примечание. Гарантируется, что длины названий всех трех городов различны."""

city_1, city_2, city_3 = [input() for _ in range(3)]
if min(len(city_1), len(city_2), len(city_3)) == len(city_1):
    print(city_1)
elif min(len(city_2), len(city_3)) == len(city_2):
    print(city_2)
else:
    print(city_3)
if max(len(city_1), len(city_2), len(city_3)) == len(city_1):
    print(city_1)
elif max(len(city_2), len(city_3)) == len(city_2):
    print(city_2)
else:
    print(city_3)

# variant 2:
# city_1, city_2, city_3 = [input() for _ in range(3)]
# print(min(city_1, city_2, city_3, key=len))
# print(max(city_1, city_2, city_3, key=len))