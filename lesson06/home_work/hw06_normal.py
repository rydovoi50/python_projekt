# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# +1. Получить полный список всех классов школы
# +/-2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# +4. Узнать ФИО родителей указанного ученика
# +/-5. Получить список всех Учителей, преподающих в указанном классе

class People:
    def __init__(self, surname, name, middle_name, date_of_birth):
        self.surname = surname
        self.name = name
        self.middle_name = middle_name
        self.dob = date_of_birth

    @property
    def full_name(self):
        return self.surname + ' ' + self.name + ' ' + self.middle_name


class School:
    def __init__(self, classroom, subject):
        self.classroom = classroom
        self.subject = subject
        # self.subject = subject

    # @property
    def full_clas(self):
        full = self.classroom.keys()
        return full

    def prepod(self, cl):
        for i in classroom[cl]:
            for _ in subject:
                if i == _:
                    print('В данном классе преподает {}'.format(subject[i]))


class Student(People, School):
    def __init__(self, surname, name, middle_name, date_of_birth, mama, papa, classroom, subject):
        People.__init__(self, surname, name, middle_name, date_of_birth)
        School.__init__(self, subject, classroom)
        self.mama = mama
        self.papa = papa
        self.name = name
        self.middle_name = middle_name
        self.dob = date_of_birth
        self.classroom = classroom

    def full_name(self):
        return self.surname + ' ' + self.name[0] + '. ' + self.middle_name[0] + '. '

    def sub(self):
        name = self.surname + ' ' + self.name[0] + '. ' + self.middle_name[0] + '. '
        return name + ' учится в ' + self.subject

    def cl_st(self, _):
        if _ == self.classroom:
            name = self.surname + ' ' + self.name[0] + '. ' + self.middle_name[0] + '. '
            print('В \'{}\' классе учится {}'.format(_, name)) #Student.full_name

    def ma(self):
        return self.mama

    def pa(self):
        return self.papa

    def subject_teacher(self):
        name = self.surname + ' ' + self.name[0] + '. ' + self.middle_name[0] + '. '
        return print('{} учится в \'{}\' классе. Преподают в этом классе {} учителя {} предметы' \
                     .format(name, self.classroom, School.subject, ))


class Teacher(People, School):
    def __init__(self, surname, name, middle_name, date_of_birth, classroom, subject):
        People.__init__(self, surname, name, middle_name, date_of_birth)
        School.__init__(self, classroom, subject)
        # self.subject = subject

        # def add_classroom(self, ):


classroom = {'5 А': ["Математика", "Русский язык", "Литература"],
             '6 A': ["Математика", "Алгебра"],
             '7 A': ["ОБЖ, Физ-ра", "Литература"],
             '8 А': ["Математика", "Адгебра, ОБЖ"],
             '9 А': ["Литература", "Математика"],
             '10 А': ["Физ-ра", "Русский язык"]}

subject = {'Математика': ['Пермяков'],      #Нужно додумать как оформить список преподающих учителей.
           'Русский язык': ['Петров'],
           'Литература': ['Языкова'],
           'Алгебра': ['Форсункина'],
           'Физ-ра': ['Данилин'],
           'ОБЖ': ['Черпаков']}

"""Все для класса Student"""

students = [Student('Иванов', 'Иван', 'Иванович', '20.02.2003', 'Иванова Зинаида Петровна', 'Иванов Иван Петрович',
                    '5 А', classroom['5 А']),
            Student('Забулдыгин', 'Фёдор', 'Павлович', '14.01.2004', 'Забулдыгина Вера Аристарховна',
                    'Забулдыгин Павел Валерьевич', '5 А', classroom['5 А']),
            Student('Пипеткина', 'Ксения', 'Александровна', '25.07.2003', 'Пипеткина Галина Павловна',
                    'Пипеткин Александр Валентинович', '6 A', classroom['6 A']),
            Student('Верещагин', 'Дмитрий', 'Алексеевич', '01.01.2003', 'Верещагина Наталья Андреевна',
                    'Верещагин Алексей Петрович', '6 A', classroom['6 A']),
            Student('Антонов', 'Анатолий', 'Аникеевич', '17.10.2003', 'Антонова Галина Владимировна',
                    'Антонов Аникей Львович', '8 А', classroom['8 А']),
            Student('Москвин', 'Владимир', 'Анатольевич', '05.01.2002', 'Москвина Вероника Антоновна',
                    'Москвин Анатолий Сергеевич', '7 A', classroom['7 A']),
            Student('Рожкова', 'Инна', 'Александровна', '01.01.2002', 'Рожкова Анастасия Артуровна',
                    'Рожков Александр Александрович', '9 А', classroom['9 А']),
            Student('Лисина', 'Анжела', 'Ивановна', '30.12.2002', 'Лисина Нелля Вадимовна',
                    'Лисин Иван Каримович', '10 А', classroom['10 А']),
            ]


"""Все для класса Teacher"""

teachers = [Teacher('Пермякова', 'Валентина', 'Петровна', '13.12.1975', '5 А, 6 A, 8 А, 9 А', 'Математика'),
            Teacher('Петров', 'Пётр', 'Андреевич', '24.04.1955', '5 А, 10 А', 'Русский язык'),
            Teacher('Языкова', 'Тамара', 'Павловна', '30.03.1980', '5 А, 7 A, 9 А', 'Литература'),
            Teacher('Форсункина', 'Аврора', 'Генадьевна', '03.10.1977', '6 A, 8 А', 'Алгебра'),
            Teacher('Черпаков', 'Валерий', 'Петрович', '10.11.1966', '7 A, 8 А', 'ОБЖ'),
            Teacher('Данилин', 'Роберт', 'Владиславович', '29.02.1988', '7 A, 10 А', 'Физ-ра'),
            ]


"""Все для класса Shcool"""

school = School(classroom, subject)

'''Решение'''

print('Всего классов в данной школе', school.full_clas())   # 1. Получить полный список всех классов школы

for i in students:                                          #Получить список всех учеников в указанном классе
    print(i.sub())                                          #(каждый ученик отображается в формате "Фамилия И.О.")

for i in students:                                          #Получить список всех учеников в указанном классе
    print(i.cl_st('5 А'))                                   #(каждый ученик отображается в формате "Фамилия И.О.")

for i in students:
    print('{}: мама - {}, папа - {}'.format(i.full_name(), i.ma(), i.pa())) #4.Узнать ФИО родителей указанного ученика

print(school.prepod('5 А'))                           #5. Получить список всех Учителей, преподающих в указанном классе

print(students.subject_teacher())

# for i in classroom['6 A']:                                   #Кто преподает в данном классе
#     for _ in subject:
#         if i == _:
#             print('В данном классе преподает {}'.format(subject[i]))
