import random
import sys


class Loto:

    def __init__(self):
        self.ls_keg = [x for x in range(1, 91)]
        random.shuffle(self.ls_keg)
        self.num = random.sample(range(1, 91), 15)

        self.play()
        # print(self.ls_keg)

    def play(self):
        while True:
            self.keg()
            self.user = self.card('Пользователь')
            self.comp = self.card('Компьютер')
            self.y_n()
            self.answere()

    def keg(self):
        self.numb = self.ls_keg.pop()
        print('Новый бочонок: {} (осталоь {})'.format(self.numb, len(self.ls_keg)))

    def card(self, ed):
        self.a = sorted(self.num[0: 5])
        self.b = sorted(self.num[5: 10])
        self.c = sorted(self.num[10:])
        args = [ed, self.dash(self.a), self.dash(self.b), self.dash(self.c), '']
        print('{:-^26}\n{}\n{}\n{}\n{:-^26}'.format(*args))

    def dash(self, ls):
        for i in range(4):
            _ = random.randint(0, 9)
            ls.insert(_, '--')
        return ' '.join(str(i) for i in ls)

    def exclude(self, numb):
        for i in self.a:
            if i == numb:
                print(i)

    def answere(self):
        if self.answer == 'y':
            self.exclude(self.numb)
        else:
            # print('END')
            # sys.exit()
            pass

    def y_n(self):
        self.answer = input('Зачеркнуть цифру (yes / no): \n')


loto = Loto()
