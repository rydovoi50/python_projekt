# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.

a = str(input("Число/n"))
b= a.find('9')
print(a[b])


a = input ('число')
l = len(a)  #длинна строки
i = 0
while i < l:
    print(a[i])
    i += 1
print ( "END" )

a =int( input ("Введите число:\n"))
while a > 0:
    print(a % 10)
    a = a // 10
print(' END ')

a = int ( input ( 'a = '))
a_max = 0
while a > 0:
    if a_max< a % 10:
        a_max = a % 10
    a = a // 10
print(a_max)


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
x = int( input ('Введите x:\n'))
y = int( input ('Введите y:\n'))
x = x + y
y = x - y
x = x - y
print ('x =', x ,'y =', y)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math
# import math
# math.sqrt(4) - вычисляет корень числа 4