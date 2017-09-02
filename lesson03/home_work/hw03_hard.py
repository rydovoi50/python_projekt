# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


import os

path = os.path.join('G:\Courses\Python. Уровень1\python_projekt\lesson03\home_work\data', 'workers')
f = open(path, 'r', encoding='UTF-8')
print(f.read())
f.close()

print('**************')
path_1 = os.path.join('G:\Courses\Python. Уровень1\python_projekt\lesson03\home_work\data', 'hours_of')
d = open(path_1, 'r', encoding='UTF-8')
print(d.read())
d.close()

print('*' * 100)

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))


path = os.path.join('G:\Courses\Python. Уровень1\python_projekt\lesson03\home_work\data', 'fruits.txt')
fru = open(path, 'r', encoding='UTF-8')
fruits_A = open('data\\home_work\\fruits_A.txt', 'w', encoding='UTF-8')
fruits_Б = open('data\\home_work\\fruits_Б.txt', 'w', encoding='UTF-8')
fruits_В = open('data\\home_work\\fruits_В.txt', 'w', encoding='UTF-8')
fruits_Г = open('data\\home_work\\fruits_Г.txt', 'w', encoding='UTF-8')
fruits_Д = open('data\\home_work\\fruits_Д.txt', 'w', encoding='UTF-8')
fruits_Е = open('data\\home_work\\fruits_Е.txt', 'w', encoding='UTF-8')
fruits_Ё = open('data\\home_work\\fruits_Ё.txt', 'w', encoding='UTF-8')
fruits_Ж = open('data\\home_work\\fruits_Ж.txt', 'w', encoding='UTF-8')
fruits_З = open('data\\home_work\\fruits_З.txt', 'w', encoding='UTF-8')
fruits_И = open('data\\home_work\\fruits_И.txt', 'w', encoding='UTF-8')
fruits_Й = open('data\\home_work\\fruits_Й.txt', 'w', encoding='UTF-8')
fruits_К = open('data\\home_work\\fruits_К.txt', 'w', encoding='UTF-8')
fruits_Л = open('data\\home_work\\fruits_Л.txt', 'w', encoding='UTF-8')
fruits_М = open('data\\home_work\\fruits_М.txt', 'w', encoding='UTF-8')
fruits_Н = open('data\\home_work\\fruits_Н.txt', 'w', encoding='UTF-8')
fruits_О = open('data\\home_work\\fruits_О.txt', 'w', encoding='UTF-8')
fruits_П = open('data\\home_work\\fruits_П.txt', 'w', encoding='UTF-8')
fruits_Р = open('data\\home_work\\fruits_Р.txt', 'w', encoding='UTF-8')
fruits_С = open('data\\home_work\\fruits_С.txt', 'w', encoding='UTF-8')
fruits_Т = open('data\\home_work\\fruits_Т.txt', 'w', encoding='UTF-8')
fruits_У = open('data\\home_work\\fruits_У.txt', 'w', encoding='UTF-8')
fruits_Ф = open('data\\home_work\\fruits_Ф.txt', 'w', encoding='UTF-8')
fruits_Х = open('data\\home_work\\fruits_Х.txt', 'w', encoding='UTF-8')
fruits_Ц = open('data\\home_work\\fruits_Ц.txt', 'w', encoding='UTF-8')
fruits_Ч = open('data\\home_work\\fruits_Ч.txt', 'w', encoding='UTF-8')
fruits_Ш = open('data\\home_work\\fruits_Ш.txt', 'w', encoding='UTF-8')
fruits_Щ = open('data\\home_work\\fruits_Щ.txt', 'w', encoding='UTF-8')
fruits_Ъ = open('data\\home_work\\fruits_Ъ.txt', 'w', encoding='UTF-8')
fruits_Ы = open('data\\home_work\\fruits_Ы.txt', 'w', encoding='UTF-8')
fruits_Ь = open('data\\home_work\\fruits_Ь.txt', 'w', encoding='UTF-8')
fruits_Э = open('data\\home_work\\fruits_Э.txt', 'w', encoding='UTF-8')
fruits_Ю = open('data\\home_work\\fruits_Ю.txt', 'w', encoding='UTF-8')
fruits_Я = open('data\\home_work\\fruits_Я.txt', 'w', encoding='UTF-8')

for i in fru:
    if i[0] == 'А':
        fruits_A.write(i)
    elif i[0] == 'Б':
        fruits_Б.write(i)
    elif i[0] == 'В':
        fruits_В.write(i)
    elif i[0] == 'Г':
        fruits_Г.write(i)
    elif i[0] == 'Д':
        fruits_Д.write(i)
    elif i[0] == 'Е':
        fruits_Е.write(i)
    elif i[0] == 'Ё':
        fruits_Ё.write(i)
    elif i[0] == 'Ж':
        fruits_Ж.write(i)
    elif i[0] == 'З':
        fruits_З.write(i)
    elif i[0] == 'И':
        fruits_И.write(i)
    elif i[0] == 'Й':
        fruits_Й.write(i)
    elif i[0] == 'К':
        fruits_К.write(i)
    elif i[0] == 'Л':
        fruits_Л.write(i)
    elif i[0] == 'М':
        fruits_М.write(i)
    elif i[0] == 'Н':
        fruits_Н.write(i)
    elif i[0] == 'О':
        fruits_О.write(i)
    elif i[0] == 'П':
        fruits_П.write(i)
    elif i[0] == 'Р':
        fruits_Р.write(i)
    elif i[0] == 'С':
        fruits_С.write(i)
    elif i[0] == 'Т':
        fruits_Т.write(i)
    elif i[0] == 'У':
        fruits_У.write(i)
    elif i[0] == 'Ф':
        fruits_Ф.write(i)
    elif i[0] == 'Х':
        fruits_Х.write(i)
    elif i[0] == 'Ц':
        fruits_Ц.write(i)
    elif i[0] == 'Ч':
        fruits_Ч.write(i)
    elif i[0] == 'Ш':
        fruits_Ш.write(i)
    elif i[0] == 'Щ':
        fruits_Щ.write(i)
    elif i[0] == 'Ъ':
        fruits_Ъ.write(i)
    elif i[0] == 'Ы':
        fruits_Ы.write(i)
    elif i[0] == 'Ь':
        fruits_Ь.write(i)
    elif i[0] == 'Э':
        fruits_Э.write(i)
    elif i[0] == 'Ю':
        fruits_Ю.write(i)
    elif i[0] == 'Я':
        fruits_Я.write(i)