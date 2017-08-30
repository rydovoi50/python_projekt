# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

a = [9, 10, 25, 100, 4, -2, 7, 34]
b = []
print(a)
for i in a:
    if i < 0:
        continue
    elif i % ( i ** 0.5 ) == 0:
        b.append(int(i ** 0.5))
print(b)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
date = '08,07,1988'

days1 = {1: 'первое', 2: 'второе', 3: 'третье', 4: 'четвертое', 5: 'пятое', 6: 'шестое',
        7: 'седьмое', 8: 'восьмое', 9: 'девятое', 10: 'десятое', 11: 'одинадцатое',
        12: 'двенадцатое', 13: 'тринадцатое', 14: 'четырнадцатое', 15: 'пятнадцатое',
        16: 'шестнадцатое', 17: 'семнадцатое', 18: 'восемнадцатое', 19: 'девятнадцатое',
        20: 'двадцатое', 30: 'тридцатое'}
days2 = {2: 'двадцать', 3: 'тридцать'}

months = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня', 7: 'июля',
          8: 'августa', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}

day = int(date[0:2])
month = int(date[3:5])
yare = int(date[6:10])
if day % 10 != 0 and day > 20:
    print('{0} {1} {2} {3} года'.format(days2[day//10], days1[day%10], months[month], yare))
else:
     print('{0} {1} {2} года'.format(days1[day], months[month], yare))

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random
n = int(input( 'введите число:\n' ))
lst = []
for i in range( 0 , n ):
        lst.append ( random.randint( -100, 100 ))
print (lst)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]