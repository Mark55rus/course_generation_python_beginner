"""Гласные и согласные
На вход программе подается одна строка с буквами русского языка. Напишите программу, которая определяет количество
гласных и согласных букв.
Формат входных данных
На вход программе подается одна строка.
Формат выходных данных
Программа должна вывести количество гласных и согласных букв.
Примечание. В русском языке 10 гласных букв (а, у, о, ы, и, э, я, ю, ё, е) и
21 согласная буква (б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ)."""

text = input()
count_vowel_letters = 0
count_consonant_letters = 0
for c in text:
    if c in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        count_vowel_letters += 1
    if c in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        count_consonant_letters += 1
print(f'Количество гласных букв равно {count_vowel_letters}')
print(f'Количество согласных букв равно {count_consonant_letters}')
