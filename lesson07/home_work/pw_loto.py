import random



class Card:
    def __init__(self, id=''):
        self.ad = id
        num = random.sample(range(1, 91), 15)
        self.a = sorted(num[0: 5])
        self.b = sorted(num[5: 10])  # + ['--' for x in range(4)]
        self.c = sorted(num[10:])  # + ['--' for x in range(4)]
        self.ls = [self.a, self.b, self.c]
        self.str_a = self.lqs(self.a)
        self.str_b = self.lqs(self.b)
        self.str_c = self.lqs(self.c)

    def exlude(self, number=None):
        for _ in self.ls:
            for i in _:
                if i == number:
                    z = _.index(i)
                    _[z] = 'xx'
        # print(self.ls)
        self.str_a = self.lqs(self.a)
        self.str_b = self.lqs(self.b)
        self.str_c = self.lqs(self.c)


    def __str__(self):
        x = [self.ad, self.str_a, self.str_b, self.str_c, '']
        z = '{:-^26}\n{}\n{}\n{}\n{:-^26}'.format(*x)
        return z
        # if self.y_n() == 'y':
        #     for i in x:
        #         if self.ls_keg.pop() == i:
        #             z = x.index(i)
        #             i = '-'
        #             x[z] = i

    def lqs(self, lis):
        lis1 = lis.copy()
        for i in range(4):
            _ = random.randint(0, 9)
            lis1.insert(_, '--')
        y = [str(x) for x in lis1]
        for x in y:
            if len(x) == 1:
                z = y.index(x)
                x = x + ' '
                y[z] = x
        return ' '.join(y)

class Loto:

    def __init__(self):
        self.ls_keg = [x for x in range(1, 91)]
        random.shuffle(self.ls_keg)
        self.user = Card('Пользователь')
        self.comp = Card('Компьютер')
        self.answer = None
        self.loop()

    def loop(self):
        while True:
            self.keg()
            print(self.user)
            print(self.comp)
            self.answer = self.y_n()
            self.exclude()

    def keg(self):
        self.k = self.ls_keg.pop()
        print('\nВыпал боченок - {}'.format(self.k))
        print('осталось {} бочонков'.format(len(self.ls_keg)))

    def exclude(self):
        try:
            self.comp.exlude(number=self.k)
        except:
            pass
        if self.answer == 'y':
            self.user.exlude(number=self.k)

    def y_n(self):
        answer = input('Зачеркнуть цифру yes / no: ')
        return answer


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

