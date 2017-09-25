import random


class Loto:

    def card(self, ad):
        num = random.sample(range(1, 91), 15)
        a = sorted(num[0: 5]) + list(' ' * 4)
        b = sorted(num[5: 10]) + list(' ' * 4)
        c = sorted(num[10:]) + list(' ' * 4)
        random.shuffle(a)
        random.shuffle(b)
        random.shuffle(c)
        return '{:-^41} \n{} \n{} \n{} \n{:-^41}'.format(ad, a, b, c, '')

numb = Loto()
print(numb.card('Пользователь'))
print(numb.card('Компьютер'))

a = []
b = random.sample(range(1, 91), 15)
d = '----------'
for i in range(0, 9):
    a.append(b[i])
    a.append('--')
    # print(a)

random.shuffle(a)
# print(a)


