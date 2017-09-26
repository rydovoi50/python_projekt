import random

numb = random.randrange(1, 10)
print(numb)

def new():
    list = random.sample(range(1, 11), 10)
    for i in list:
        print(i)
        if numb == i:
            z = list.index(i)
            i = '-'
            list[z] = i

    x = ' '.join([str(_) for _ in list])
    print(x)
    # q = []
    # y = 3
    # for i in x:
    #     print(i)
    #     if i != ' ':
    #         q.append(int(i))
    #         print(q)


new()
