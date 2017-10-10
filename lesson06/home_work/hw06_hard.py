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
#     def __init__(self, data):
        # self.read = args
        # self.h_name = ' '.join(data[0:2])
        # self.hours_worked = int(data[2])
        # print(self.h_name)
        # print(self.hours_worked)
        # print('q = ', self.read)


class Worker:
    def __init__(self, args, data=None):
        # Hours.__init__(self, data)
        self.name = ' '.join(args[0:2])
        self.pay = int(args[2])
        self.post = args[3]
        self.standard_watches = int(args[4])
        # print(self.name)
        # print(self.pay)
        # print(self.proba(hours))

    def proba(self, args):
        self.h_name = ' '.join(args[0:2])
        self.hours_worked = int(args[2])
        if self.h_name == self.name:
            self.a = self.pay / self.standard_watches * self.hours_worked
            print("{} / {} * {}".format(self.pay, self.standard_watches, self.hours_worked))
        return '{} -> {}'.format(self.name, self.a)


with open('.\\data\\workers', 'r', encoding='UTF-8') as file_1:
    a = file_1.readlines()[1:]
    for i in a:
        Worker(i.split())

with open('.\\data\\hours_of', 'r', encoding='UTF=8') as file_2:
    b = file_2.readlines()[1:]
    for x in b:
        hours = x.split()

print(Worker.proba(hours))
