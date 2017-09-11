''' Дата: 
    Основная идея:
    запомнить предыдущий символ(last_char) в цикле,
    если предыдущий и текущий маленькие,
    то флаг в True, если нет в False
                                            '''


def re_my(line):

    flag_two_lower = False
    last_char = ''
    tmp_str_upper = ''
    new_list = []

    for i in line:
        if i.islower():
            if last_char.islower():
                flag_two_lower = True
            else:
                flag_two_lower = False
            if len(tmp_str_upper) > 2:
                new_list.append(tmp_str_upper[:-2])
                tmp_str_upper = ''
            else:
                tmp_str_upper = ''
        elif i.isupper() & flag_two_lower:
                tmp_str_upper += i
        last_char = i

    return new_list
