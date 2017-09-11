# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


import os


def create_a_folder(count):
    for i in range(1, count):
        try:
            os.mkdir('dir_' + str(i))
        except FileExistsError:
            print('Папка {} в директории {} уже существует'.format('dir_' + str(i), os.getcwd()))


def delete_folder(count):
    for i in range(1, count):
        os.rmdir('dir_' + str(i))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.



def list():
    print(os.listdir())

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.



def cope_file():
    with open('hw05_easy.py', 'r', encoding='UTF-8') as hw:
        file_1 = hw.read()
    with open('new_hw05_easy.py', 'w', encoding='UTF-8') as new:
        new.write(file_1)


list()
create_a_folder(10)
list()
delete_folder(10)
list()
cope_file()
list()
input()
