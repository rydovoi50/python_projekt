

class Calculation:

    def __init__(self, hourse, workers):
        self.hours = []
        self.worker = []
        self.hours.extend(hourse)
        self.worker.extend(workers)
        print('1 = ', self.hours)
        print('2 = ', self.worker)

    # def proba(self):
        for i in self.hours:
            print(i.h_name)
            for _ in self.worker:
                print(_)
                # if i.h_name == _.w_name:
                #     print(123)


class Hours:

    def __init__(self, args):
        self.h_name = ' '.join(args[0:2])
        self.h_work = int(args[2])
        # print(self.h_name)
        # print(self.h_work)


class Worker:

    def __init__(self, args):
        self.w_name = ' '.join(args[0:2])
        self.w_pay = int(args[2])
        self.w_clock = int(args[4])
        # print(self.w_name, self.w_pay, self.w_clock)

with open('.\\data\\hours_of', 'r',encoding='UTF-8') as a:
    file_1 = a.readlines()[1:]
    for i in file_1:
        c = []
        hours = (i.split())
        Hours(hours)
        # c.extend(hours)

with open('.\\data\\workers', 'r', encoding='UTF-8') as b:
    file_2 = b.readlines()[1:]
    for i in file_2:
        worker = (i.split())
        Worker(worker)

# print('c = ', c)
calc = Calculation(hourse=file_1, workers=file_2)
# print(calc.proba())
