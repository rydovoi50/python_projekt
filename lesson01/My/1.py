'''a = 123888
a = str(a)
a1 = a[0:3]
a2 = a[3:6]
print(a1,a2)
a1 = int(a1)
a2 = int(a2)
summ1 = 0
while a1 > 0:
        summ1 = summ1 + a1 % 10
        a1 = a1 // 10
summ2 = 0 
while a2 > 0:
        summ2 = summ2 + a2 % 10
        a2 = a2 // 10
print ( summ1 == summ2 )


name = input('Введите Имя > ')
age = input('Введите возраст > ')
if not age.isdigit():
    print('Введите возраст цифрами')


a = 'Anna Maria Peter' # Набор слов может быть любой длины
a = a.split() # Для начала разделим строку по пробелам на список слов
res = [] # Заводим список, в котором будет результат
while len(a) > 0 : # Задаем цикл: пока в списке а что-то есть...
        res.append(a.pop()) # ...Мы будем вырезать из него последний элемент и вставлять на последнее место в результат
print( ' '.join(res)) #Выводим на экран результат, превращенный в строку. Вернет 'Peter Maria Anna'

a = 'Anna Maria Peter'
print(a)
print(type(a))
a = a.split(' ')
print(type(a))
print(a)

lst=[5,2,7,4,0,9,8,6,-100]
print(lst)
k=0
n=1
while n<(len(lst)):
    while k<(len(lst)-n):
        if lst[k]>lst[k+1]:
            lst[k],lst[k+1]=lst[k+1],lst[k]
            print (lst) # чтоб видеть "эволюцию" списка :-)
        k+=1
    k=0

    2, 10, -12, 2.5, 20, -11, 4, 4, 0
    n+=1
    '''
import random


lst1 =[random.randit(0, 30) for _ in range(10)]
print('lst1 = ', lst1)
