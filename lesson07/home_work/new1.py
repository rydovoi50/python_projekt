import random
import sys
class Card:

    def __init__(self, ed=''):
        self.ed = ed
        self.num = random.sample(range(1, 91), 15)
        self.a = sorted(self.num[0: 5])
        for i in range(4):
            _ = random.randint(0, 9)
            self.a.insert(_, '--')
        self.b = sorted(self.num[5: 10])
        for i in range(4):
            _ = random.randint(0, 9)
            self.b.insert(_, '--')
        self.c = sorted(self.num[10:])
        for i in range(4):
            _ = random.randint(0, 9)
            self.c.insert(_, '--')
        self.abc = [self.a, self.b, self.c]
        self.st_abc = [self.dash(self.a), self.dash(self.b), self.dash(self.c)]
        # self.dash_a = self.dash(self.a)
        # self.dash_b = self.dash(self.b)
        # self.dash_c = self.dash(self.c)
        # self.abc = [self.dash(self.a), self.dash(self.b), self.dash(self.c)]

    def __str__(self,):
        args = [self.ed, self.dash(self.a), self.dash(self.b), self.dash(self.c), '']
        return '{:-^26}\n{}\n{}\n{}\n{:-^26}'.format(*args)

    def test(self, ed=''):
        for i in self.st_abc:
            x = str(i)
            y = x.replace(' ', '')
            x = y.replace('-', '')
            if x.isdigit() == True:
                print(1+1)
                print(x.isdigit())
            elif x.isdigit() == False:
                print(2+2)
                print(x.isdigit())
                print('Победил {}'.format(ed))
                sys.exit()

    def dash(self, ls):
        x = [str(i) for i in ls]
        for i in x:
            if len(i) == 1:
                z = x.index(i)
                x[z] = i + ' '
        # ls1 = ls.copy()
        # for i in range(4):
        #     _ = random.randint(0, 9)
        #     ls1.insert(_, '--')
        return ' '.join(x)

    def exclude(self, numb):
        for i in self.abc:
            for _ in i:
                if _ == numb:
                    z = i.index(_)
                    i[z] = 'xx'
                # else:
                #     print('Вы проиграли')
                #     sys.exit()
        self.abc = [self.a, self.b, self.c]

    def exclude_no(self, numb):
        for i in self.abc:
            for _ in i:
                if _ == numb:
                    print('Вы проиграли')
                    sys.exit()
                else:
                    pass


class Loto:

    def __init__(self):
        self.ls_keg = [x for x in range(1, 91)]
        random.shuffle(self.ls_keg)
        self.user = Card('Пользователь')
        self.comp = Card('Компьютер')
        # self.test1 = Card('Пользователь')
        # self.test2 = Card('Компьютер')
        self.play()
        # print(self.ls_keg)

    def play(self):
        while True:
            self.user.test('Пользователь')
            self.comp.test('Компьютер')
            self.keg()
            print(self.user)
            print(self.comp)
            self.y_n()
            self.answere()

    def keg(self):
        self.numb = self.ls_keg.pop()
        print('Новый бочонок: {} (осталоь {})'.format(self.numb, len(self.ls_keg)))
        # print(type(self.numb))

    def answere(self):
        # try:
        self.comp.exclude(self.numb)
        # except:
        #     pass
        if self.answer == 'y':
            self.user.exclude(self.numb)
        else:
            self.user.exclude_no(self.numb)
            pass

    def y_n(self):
        self.answer = input('Зачеркнуть цифру (yes / no): \n')


loto = Loto()
