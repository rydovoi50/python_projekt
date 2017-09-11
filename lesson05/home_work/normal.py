import os
import sys



while True:
    user = input('1. Перейти в папку\n'
                '2. Просмотреть содержимое текущей папки\n'
                '3. Удалить папку\n'
                '4. Создать папку\n'
                'Введите "q" для выхода\n')

    if user == '1':
        name = input('Введите имя папки в которую хотите перейти: ')
        try:
            os.chdir(name)
            print('Вы успешно перешли в \'{}\''.format(name))
        except FileNotFoundError:
            print('Папки \'{}\' не существует'.format(name))

    elif user == '2':
        print(os.listdir())

    elif user == '3':
        name = input('Введите имя папки которую хотите удалить')
        try:
            os.rmdir(name)
            print('Папка \'{}\' успешно удалена'.format(name))
        except FileNotFoundError:
            print('Папки \'{}\' не существует'.format(name))

    elif user == '4':
        name = input('Введите имя папки: ')
        try:
            os.mkdir(name)
            print('Папка \'{}\' успешно создана'.format(name))
        except FileExistsError:
            print('Папка \'{}\' уже существует'.format(name))

    elif user == 'q':
        sys.exit()

    else:
        print('Не известная команда, попробуйте еще раз')
