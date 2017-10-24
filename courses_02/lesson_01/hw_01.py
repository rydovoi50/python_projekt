import pickle

test = 'test1329384a'
'''1) Записать строку символов в текстовый файл и вывести содержимое файла'''
file_01 = open('.\\data\\text_01', 'w')
file_01.write(test)
file_01.close()
file_01 = open('.\\data\\text_01', 'r')
r = file_01.read()
print('содержимое первого файла \'text_01\' : ', r)
file_01.close()

'''2) Записать строку символов в файл, явным указанием кодировки utf-8, вывести содержимое файла'''
file_02 = open('.\\data\\text_02', 'w', encoding='UTF-8')
file_02.write(test)
file_02.close()
file_02 = open('.\\data\\text_02', 'r', encoding='UTF-8')
r = file_02.read()
print('содержимое вторго файла \'text_02\' с указанием кодировки: ', r)
file_02.close()

'''3) Декодировать содержимое файла из предыдущего задания'''
file_02 = open('.\\data\\text_02', 'r')
f = file_02.read()
print('декоируем содержимое файла \'text_02\' : ', f.encode(encoding="utf-8"))
file_02.close()

'''4) Записать строку символов в двоичный файл и вывести содержимое файла'''
file_03 = open('.\\data\\text_03', 'wb')
pickle.dump(test, file_03)
file_03.close()
file_03 = open('.\\data\\text_03', 'rb')
f = pickle.load(file_03)
print('содержимое файла \'text_03\' : ', f)
file_03.close()

'''5) Записать строку символов в файл, явным указанием кодировки latin-1, вывести содержимое файла'''
file_04 = open('.\\data\\text_04', 'wb')
file_04.write(bytes(test, encoding='latin-1'))
file_04.close()
file_04 = open('.\\data\\text_04', 'rb')
print('содержимое файла \'text_04\' с явным указанием кодировки : ', file_04.read())
file_04.close()

'''Декодировать содержимое файла из предыдущего задания'''
file_04 = open('.\\data\\text_04', 'rb')
f = file_04.read()
print('декодируем файл \'text_04\' : ', f.decode())
file_04.close()
