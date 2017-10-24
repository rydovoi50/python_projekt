import itertools
import zipfile
import os


def file():
    with open('bomba', 'w+') as file:
        for i in itertools.repeat('0', 100):
            file.write(i)
#
# with zipfile.ZipFile('bomba.zip', 'w') as myzip:
#     myzip.write('bomba')
#     with zipfile.ZipFile('Papka2.zip', 'w') as file_2:
#         file_2.write('bomba')

# os.chdir('.\\level_0')
# file()
def dir(name, num):
    try:
        for i in range(1, num):
            os.mkdir(name + str(i))
            # file()
            print('создал папку {}{}'.format(name, i))
    except FileExistsError:
        print('создал папку {}{}'.format(name, i))


def transit(name, num):
    for i in range(1, num):
        # print(i)
        try:
            os.chdir(name + str(i))
            print('Перешел в ', os.getcwd())
            file()
            # os.chdir('..')
        except FileNotFoundError:
            print('Папки не существует')
            os.chdir('..\\{}{}'.format(name, i))
            file()
            print('вернулся к папке ', os.getcwd())


'''level 0'''
dir('level_0_', 2)
transit('level_0_', 2)
# print(os.getcwd())

'''level 1'''
dir('level_1_', 3)
transit('level_1_', 3)
# print(os.getcwd())

'''level 2'''
dir('level_2_', 4)
transit('level_2_', 4)
# print(os.getcwd())

'''level 3'''
dir('level_3_', 5)
transit('level_3_', 5)
# print(os.getcwd())

