import math

# Напишите программу, ĸоторая считает общую цену.
# Передается m рублей и n ĸопееĸ цена, а таĸже ĸоличество s товара.
# Посчитайте общую цену в рублях и ĸопейĸах за l товаров.
# Уточнение:
# Используйте функцию return чтобы ответ был в рублях и копейках.
# Ответ должен быть в формате: "Общая цена составляет M рублей и N копеек за L товаров"

# * Для одного из тестов нужно применять какую-то библиотеку =)
def common_price(m, n, s, l):
    if not isinstance(m, int) or not isinstance(n, int) or not isinstance(s, int) or not isinstance(l, int):
        return False
    if (s == 0) or (m == 0 and n == 0):
        return False
    if l < 0:
        return False
    kop_total_price = (100*m+n)*l/s
    a = round(kop_total_price//100)
    v = round(kop_total_price-100*a)

    return "Общая цена составляет " + str(a) + " рублей и " + str(v) + " копеек за " + str(l) + " товаров"

# В функцию передаются аргументы: a, b, c - длины сторон треугольника.
# Требуется: проверить, может ли существовать треугольник с такими длинами сторон.
# Если может - найти его площадь с точностью до четырёх десятичных и вернуть площадь (return).
# Пример: если строны треугольника равны 2, 2, 2 то мы должны вернуть 1.7321
# Если такой треугольник существовать не может - функция должна вернуть False.
def triangle(a, b, c):
    if ((not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int)) and
        (not isinstance(a, float) or not isinstance(b, float) or not isinstance(c, float))):
        return False
    if ((a+b) < c) or ((a+c) < b) or ((b+c) < a):
        existment = False
    else:
        p = (a+b+c)/2
        square = round(math.sqrt(p*(p-a)*(p-b)*(p-c)),4)
        return square
    return existment

# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении могут быть знаки препинания.
# Пример: если передано "This is a sample sentence where the longest word is in the middle!",
# то надо вернуть "sentence"
def longest_word(sentence):
    if not isinstance(sentence, str):
        return False
    fixed_string = sentence.replace(',', '')
    fixed_string = fixed_string.replace(':', ' ')
    fixed_string = fixed_string.replace(';', ' ')
    fixed_string = fixed_string.replace('.', ' ')
    fixed_string = fixed_string.replace('!', ' ')
    values = fixed_string.split(' ')
    max_string = max(values[::-1], key=len)
    if max_string == '':
        return False
    return max_string

# Передается строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было передано "abc cde def", то должно быть выведено "abcdef".
def uniques(repeating_string):
    if not isinstance(repeating_string, str):
        return False
    fixed_str = repeating_string.replace(' ', '')
    uniq_set = set(fixed_str)
    uniq_str = ''.join(sorted(uniq_set, key=fixed_str.index))
    return uniq_str

# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Проверка рассчитана только на английские буквы.
def count_string_capitalization(mixed_string):
    if not isinstance(mixed_string, str):
        return False
    big = 0
    little = 0
    for i in mixed_string:
        if i.islower():
            little += 1
        elif i.upper():
            big += 1
        else:
            continue
    return f"В строке '{mixed_string}' {big} большие и {little} маленькие буквы"