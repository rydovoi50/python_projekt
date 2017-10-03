import random
import sys


class Loto:

    def __init__(self):
        self.ls_keg = [x for x in range(1, 91)]
        random.shuffle(self.ls_keg)
        self.user = self.card_user()
        self.comp = self.card_comp()
        self.play()
        # print(self.ls_keg)


    def play(self):
        while True:
            self.keg()
            print(self.user)
            print(self.comp)
            self.y_n()
            self.answere()

    def keg(self):
        self.numb = self.ls_keg.pop()
        print('Новый бочонок: {} (осталоь {})'.format(self.numb, len(self.ls_keg)))
        print(type(self.numb))

    def card_user(self):
        ed = 'Пользователь'
        self.num = random.sample(range(1, 91), 15)
        self.a = sorted(self.num[0: 5])
        self.b = sorted(self.num[5: 10])
        self.c = sorted(self.num[10:])
        args = [ed, self.dash(self.a), self.dash(self.b), self.dash(self.c), '']
        return '{:-^26}\n{}\n{}\n{}\n{:-^26}'.format(*args)

    def card_comp(self):
        ed = 'Компьютер'
        self.num = random.sample(range(1, 91), 15)
        self.a = sorted(self.num[0: 5])
        self.b = sorted(self.num[5: 10])
        self.c = sorted(self.num[10:])
        args = [ed, self.dash(self.a), self.dash(self.b), self.dash(self.c), '']
        return '{:-^26}\n{}\n{}\n{}\n{:-^26}'.format(*args)

    def dash(self, ls):
        for i in range(4):
            _ = random.randint(0, 9)
            ls.insert(_, '--')
        return ' '.join(str(i) for i in ls)

    def exclude(self, numb=None):
        for i in self.a:
            if i == numb:
                z = self.a.index(i)
                self.a[z] = 'xx'
        self.a
        for i in self.b:
            if i == numb:
                z = self.b.index(i)
                self.b[z] = 'xx'
        self.b
        for i in self.c:
            if i == numb:
                z = self.c.index(i)
                self.c[z] = 'xx'
        self.c

    def answere(self):
        # try:
        #     self.comp.exclude(numb=self.numb)
        # except:
        #     pass
        if self.answer == 'y':
            self.exclude(numb=self.numb)
        else:
            # print('END')
            # sys.exit()
            pass

    def y_n(self):
        self.answer = input('Зачеркнуть цифру (yes / no): \n')


loto = Loto()
