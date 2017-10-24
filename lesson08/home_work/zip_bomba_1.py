import itertools
import zipfile
import os


def file():
    with open('bomba', 'w+') as file:
        for i in itertools.repeat('0', 100):
            file.write(i)

class Zip_boom:
    def __init__(self, count=dict):
        self.nesting = count
        self.name_dir = 'level_'
        self.iterate()

    def iterate(self, shift=0):
        for x, y in self.nesting.items():
            for _ in range(1, y + 1 + shift):
                try:
                    os.mkdir(self.name_dir + str(x+shift) + '_' + str(_))
                    self.iterate(1)
                except Exception as e:
                    print(e)
            print(os.listdir())
            os.chdir(self.name_dir + str(x) + '_' + str(_))
        print(os.listdir())



nest = {1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5}

x = Zip_boom(nest)

