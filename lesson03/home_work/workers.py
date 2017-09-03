with open('.\data\workers', 'r', encoding='UTF-8') as k:
    a = k.readlines()[1:]
c = ''
d = []
e = []
for _ in a:
    for i in _:
        if not i.isspace():
            c += i
            if c != '' and i.isspace():
                d.append(c)
                c = ''
        elif c != '' and i.isspace():
            d.append(c)
            c = ''
    e.append(d)
    d = []
f = []
q = []
for i in e:
    z = ' '.join(i[0:2])
    f.append(z)
    f.append(i[2])
    # f.append(i[4])
    try:
        f.append(i[4])
    except Exception as e:
        print(e)
    finally:
        q.append(f)
        f = []
print(q)
print('*' * 150)

with open('.\data\hours_of', 'r', encoding='UTF-8') as k:
    a = k.readlines()[1:]
c = ''
d = []
e = []
for i in a:
    for _ in i:
        if not _.isspace():
            c += _
            if c != '' and _.isspace():
                d.append(c)
                c = ''
        elif _.isspace() and c != '':
            d.append(c)
            c = ''
    e.append(d)
    d = []
f = []
g = []
for i in e:
    f.append(' '.join(i[0:2]))
    f.append(i[2])
    g.append(f)
    f = []
print(g)
print('*' * 190)

name = []
cell = []
for i in q:
    name = i[0]
    for _ in g:
        if name == _[0] and int(i[2]) < int(_[1]):
            cell = int(_[1]) - int(i[2])
            print('{} зарплата за этот месяц = {}'.format(name, (int(i[1]) + (int(cell) * 2 * int(i[1]) / int(i[2])))))
        elif name == _[0] and int(i[2]) > int(_[1]):
            print('{} зарплата за этот месяц = {}'.format(name, (int(i[1]) / int(i[2]) * int(_[1]))))
