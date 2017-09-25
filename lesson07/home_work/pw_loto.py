import random


class Loto:

    def __init__(self):
        self.ls_keg = [x for x in range(1, 91)]
        random.shuffle(self.ls_keg)
        self.keg()
        self.card('Пользователь')
        self.card('Компьютер')

    def keg(self):
        print(self.ls_keg.pop())
        print('осталось {} бочонков'.format(len(self.ls_keg)))

    def card(self, ad):
        self.ad = ad
        num = random.sample(range(1, 91), 15)
        a = sorted(num[0: 5])  # + ['--' for x in range(4)]
        b = sorted(num[5: 10])  # + ['--' for x in range(4)]
        c = sorted(num[10:])  # + ['--' for x in range(4)]
        x = [self.ad, self.ls(a), self.ls(b), self.ls(c), '']
        print('{:-^26}\n{}\n{}\n{}\n{:-^26}'.format(*x))

    def ls(self, ls):
        for i in range(0, 4):
            _ = random.randint(0, 9)
            ls.insert(_, '--')
        y = [str(x) for x in ls]
        for x in y:
            if len(x) == 1:
                z = y.index(x)
                x = x + ' '
                y[z] = x
        return ' '.join(y)

    def y_n(self):


numb = Loto()
# print(numb.card('Пользователь'))
# print(numb.card('Компьютер'))
#
# a = []
# b = random.sample(range(1, 91), 15)
# d = '----------'
# for i in range(0, 9):
#     a.append(b[i])
#     a.append('--')
#     # print(a)

