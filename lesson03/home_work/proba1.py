import os

a = list(map(chr, range(ord('А'), ord('Я')+1)))
try:
    os.mkdir('.\data\home_work')
except:
    pass
try:
    fru = open('.\data\\fruits.txt', 'r', encoding='UTF-8')
    fruits_in_file = fru.readlines()
    fru.close()
    for i in a:
        fruits_file = '.\\data\home_work\\fruits_' + i + '.txt'
        b = open(fruits_file, 'w', encoding='UTF-8')
        for _ in fruits_in_file:
            if _[0] == i:
                b.write(_)
        b.close()

except Exception as e:
    print(e)
