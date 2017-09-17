# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.


import os
import sys
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("rmdir <dir_name> - удаление директории")
    print("срdir <dir_name> - перейти в директорию")
    print("listdir - список файлов в директории")
    print("copy_file <file>  - копирование заданного файла")
    print("del <file>  - удаление заданного файла")
    print("getcwd  - отображает путь дирректории")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def rm_dir():
    if not dir_name:
        print('Необходимо указать имя директории вторым параметром')
        return
    try:
        os.rmdir(dir_name)
        print('Директория {} удалена'.format(dir_name))
    except FileNotFoundError:
        print('директории {} не существует'.format(dir_name))


def ch_dir():
    if not dir_name:
        print('Необходимо указать имя директории вторым параметром')
        return
    os.chdir(dir_name)
    # dir_name = os.getcwd()
    print('Успешно перешли в {}'.format(dir_name))


def ls():
    print(os.listdir(os.getcwd()))


def copy():
    if not file:
        print('Необходимо указать имя файла вторым параметром')
        return
    with open(file, 'r', encoding='UTF-8') as file_1:
        h = file_1.read()
    with open('new' + file, 'w', encoding='UTF-8') as file_2:
        file_2.write(h)
    print('Файл удачно скопирован')


def cwd():
    print(os.getcwd())


def delet():
    if not file:
        print('Необходимо указать имя директории вторым параметром')
        return
    user = input('Вы точно хотите удалит файл {}, y/n: '.format(file))
    if user == 'y':
        os.remove(file)
        print('Файл {} успешно удален'.format(file))


do = {
    "help": print_help,
    "mkdir": make_dir,
    "rmdir": rm_dir,
    "chdir": ch_dir,
    "listdir": ls,
    "copy_file": copy,
    "getcwd": cwd,
    "del": delet
}

try:
    file = sys.argv[2]
except IndexError:
    file = None

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")

while True:
    print('Введите команду')
    key = input()


# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
