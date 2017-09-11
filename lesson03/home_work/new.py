import os
import sys



# while True:
#     user = input('1. Перейти в папку\n'
#                 '2. Просмотреть содержимое текущей папки\n'
#                 '3. Удалить папку\n'
#                 '4. Создать папку\n'
#                 'Введите "q" для выхода\n')

def ch_dir():
    name = input('Введите имя папки в которую хотите перейти: ')
    try:
        os.chdir(name)
        print('Вы успено перешли в \'{}\''.format(name))
    except FileNotFoundError:
        print('Папки \'{}\' не существует'.format(name))


def list():
    print(os.listdir())


def rm_dir():
    name = input('Введите имя папки которую хотите удалить')
    try:
        os.rmdir(name)
        print('Папка \'{}\' успешно удалена'.format(name))
    except FileNotFoundError:
        print('Папки \'{}\' не существует'.format(name))


def mk_dir():
    name = input('Введите имя папки: ')
    try:
        os.mkdir(name)
        print('Папка \'{}\' успешно создана'.format(name))
    except FileExistsError:
        print('Папка \'{}\' уже существует'.format(name))

