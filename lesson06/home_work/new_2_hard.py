# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла


# class Hours:
#
#     def __inti__(self, hours):
#         self.hours_name = ' '.join(hours[0:2])
#         self.hours_worked = int(hours[2])
#         self.read = [self.hours_name, self.hours_worked]
    #
    # def __init__(self, hours):
    #     # self.read = hours
    #     # self.hours_name = ''
    #     # self.hours_worked = ''
    #     self.hours_name = ' '.join(hours[0:2])
    #     self.hours_worked = int(hours[2])
    #     self.read = [self.hours_name, self.hours_worked]
    #     # print(self.read)
    #     # print('Имя из Хоурс = ', self.hours_name)
    #     # print('Отработанные часы = ', self.hours_worked)
    #     # print('q = ', self.read)


# class Worker(Hours):
#     def __init__(self, args):
#         # Hours.__init__(self, hours)
#         self.name = ' '.join(args[0:2])
#         self.pay = int(args[2])
#         self.post = args[3]
#         self.standard_watches = int(args[4])
#         # self.hours_name = ' '.join(hours[0:2])
#         # self.hours_worked = int(hours[2])
#         # print('Имя из Воркер = ', self.name)
#         # print('Зарплата = ', self.pay)
#         print(self.proba())


class Wwww:
    def __init__(self,a, b):
        self.a = a
        self.b = b
        self.name = [' '.join(i.split()[0:2]) for i in self.a]
        self.pay = [int(i.split()[2]) for i in self.a]
        self.standard_watches = [int(i.split()[4]) for i in self.a]
        self.hours_name = [' '.join(i.split()[0:2]) for i in self.b]
        self.hours_worked = [int(i.split()[2]) for i in self.b]
        self.read = [self.hours_name, self.hours_worked]
        print(self.proba())
        print(self.name)

    def list_1(self):
        for i in self.a:
            a_1 = i.split()
            self.name = ' '.join(a_1[0:2])
            self.pay = int(a_1[2])
            self.post = a_1[3]
            self.standard_watches = int(a_1[4])

    def list_2(self):
        for i in b:
            b_1 = i.split()
            self.hours_name = ' '.join(b_1[0:2])
            self.hours_worked = int(b_1[2])
            self.read = [self.hours_name, self.hours_worked]


        # self.name = ' '.join(a[0:2])
        # self.pay = int(a[2])
        # self.post = a[3]
        # self.standard_watches = int(a[4])
        # self.hours_name = ' '.join(b[0:2])
        # self.hours_worked = int(b[2])
        # self.read = [self.hours_name, self.hours_worked]
        # print(self.hours_name)

    def proba(self):
        self.a = ''
        for i in self.read:
            print(i)
            if i == self.name:
                print('{} == {}'.format(i, self.name))
        # print('{} == {}'.format(self.hours_name, self.name))
        # if self.hours_name == self.name:
        #     print('{} == {}'.format(self.hours_name, self.name))
                self.a = self.pay / self.standard_watches * self.hours_worked
                print("{} / {} * {}".format(self.pay, self.standard_watches, self.hours_worked))
        return '{} -> {}'.format(self.name, self.a)


with open('.\\data\\hours_of', 'r', encoding='UTF=8') as file_2:
    b = file_2.readlines()[1:]
    def x_3():
        for x in b:
            x_1 = []
            x_1.extend(x.split())
            return x_1
        # return x_1
        # hours = x.split()
        # s = Hours(hours)

with open('.\\data\\workers', 'r', encoding='UTF-8') as file_1:
    a = file_1.readlines()[1:]
    def x_4():
        for i in a:
            x_2 = i.split()
            return x_2

# print(b)
s = Wwww(a, b)