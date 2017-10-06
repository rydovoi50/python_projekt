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
        self.card_text()

    def card_text(self):
        self.args = [self.ed, self.dash(self.a), self.dash(self.b), self.dash(self.c), '']
        return self.args

    def __str__(self,):
        x = self.card_text()
        return '{:-^26}\n{}\n{}\n{}\n{:-^26}'.format(*x)


    def test(self):
        x = str(self.args[1] + self.args[2] + self.args[3])
        y = x.replace(' ', '')
        x = y.replace('-', '')
        z = x.replace('x', '')
        print(len(z))
        return len(z)
        # if z.isdigit() == True:
        #     pass
        # elif z.isdigit() != True:
        #     print('Победил {}'.format(self.ed))
        #     sys.exit()

    def dash(self, ls):
        x = [str(i) for i in ls]
        for i in x:
            if len(i) == 1:
                z = x.index(i)
                x[z] = i + ' '
        return ' '.join(x)

    def exclude(self, numb):
        for i in self.abc:
            for _ in i:
                if _ == numb:
                    z = i.index(_)
                    i[z] = 'xx'
                    self.abc = [self.a, self.b, self.c]
                    return True
        return False


class Loto:

    def __init__(self):
        self.ls_keg = [x for x in range(1, 91)]
        random.shuffle(self.ls_keg)
        self.user = Card('Пользователь')
        self.comp = Card('Компьютер')
        self.play()

    def play(self):
        while True:
            # self.user.test()  # проверяет на оставшееся количество цифр карточку пользователя
            # self.comp.test()  # проверяет на оставшееся количество цифр карточку компьютера
            print(self.user.abc, self.user.test(), 11111)
            self.keg()          # выбрасывает боченок и возвращает цифру
            print(self.user)    # выводит карточку на экран
            print(self.comp)    # выводит карточку на экран
            print(self.user.abc, self.user.test(), 22222)
            self.finish()
            self.y_n()          # спрашивает зачеркнуть ли цифру
            self.answere()      # сверяет ответ пользователя и зачеркивает цифру
            print(self.user.abc, self.user.test(), 333333)

    def keg(self):
        self.numb = self.ls_keg.pop()
        print('Новый бочонок: {} (осталоь {})'.format(self.numb, len(self.ls_keg)))

    def answere(self):
        self.comp.exclude(self.numb)
        x = self.user.exclude(self.numb)
        if self.answer == 'y' and x:
            pass
        # elif self.answer == 'y' and not x:
        #     print('У Вас нет такой цифры на карточке')
        #     sys.exit()
        # elif self.answer == 'n' and not x:
        #     pass
        # elif self.answer == 'n' and x:
        #     print('На Вашей карточке была такая цифра')
        #     sys.exit()
        # else:
        #     print(self.user.exclude(self.numb))
        #     print('Вы лузер')
        #     sys.exit()

    def y_n(self):
        self.answer = input('Зачеркнуть цифру (yes / no): \n')

    def finish(self):
        user = self.user.test()
        comp = self.comp.test()
        if not user and not comp:
            print('Ничья')
            sys.exit()
        elif comp == 0:
            print('Победил компьютер')
            sys.exit()
        elif user == 0:
            print('Вы победили')
            sys.exit()


loto = Loto()
