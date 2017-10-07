hw = {1: 'Получить полный список всех классов школы',
      2: 'Получить список всех учеников в указанном классе (каждый ученик отображается в формате "Фамилия И.О.")',
      3: 'Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)',
      4: 'Узнать ФИО родителей указанного ученика',
      5: 'Получить список всех Учителей, преподающих в указанном классе'
      }


class Shcool:
    def __init__(self, students, teachers):
        self.student = []
        self.teacher = []
        self.student.extend(students)
        self.teacher.extend(teachers)
        # print(self.classroom())

    '''Получаем список всех классов в школе'''
    def classroom(self):
        self.room = []
        for i in self.student:
            print(i)
            self.room.extend(i.classroom)
        for i in self.teacher:
            self.room.extend(i.classroom)
        return set(self.room)

    '''Получаем список всех учеников в классе'''
    def list_of_student_in_the_class(self, num):
        list_student = []
        for i in self.student:
            if i.classroom == num:
                print(i.st_fio0)
                # list_student.append(i.st_fio)
        return list_student
        pass


class People:
    def __init__(self, surname, name, middle_name):
        self.surname = surname
        self.name = name
        self.middle_name = middle_name
        self.st_fio = self.surname + ' ' + self.name[0] + '. ' + self.middle_name[0] + '.'
        self.fio = self.surname + ' ' + self.name + ' ' + self.middle_name


class Teacher(People):
    def __init__(self, *args):
        People.__init__(self, surname, name, middle_name)
        self.classroom = []
        self.classroom.extend([x for x in args[4:]])


class Student(People):
    def __init__(self, *args):
        People.__init__(self, surname, name, middle_name)
        self.classroom = []
        self.classroom.extend([x for x in args[4:5]])


students = [Student('Иванов', 'Иван', 'Иванович', '20.02.2003', '5 А', 'Иванова Зинаида Петровна',
                    'Иванов Иван Петрович'),
            Student('Забулдыгин', 'Фёдор', 'Павлович', '14.01.2004', '5 А', 'Забулдыгина Вера Аристарховна',
                    'Забулдыгин Павел Валерьевич'),
            Student('Пипеткина', 'Ксения', 'Александровна', '25.07.2003', '6 А', 'Пипеткина Галина Павловна',
                    'Пипеткин Александр Валентинович'),
            Student('Верещагин', 'Дмитрий', 'Алексеевич', '01.01.2003', '6 А', 'Верещагина Наталья Андреевна',
                    'Верещагин Алексей Петрович'),
            Student('Антонов', 'Анатолий', 'Аникеевич', '17.10.2003', '8 А', 'Антонова Галина Владимировна',
                    'Антонов Аникей Львович'),
            Student('Москвин', 'Владимир', 'Анатольевич', '05.01.2002', '7 А', 'Москвина Вероника Антоновна',
                    'Москвин Анатолий Сергеевич'),
            Student('Рожкова', 'Инна', 'Александровна', '01.01.2002', '9 А', 'Рожкова Анастасия Артуровна',
                    'Рожков Александр Александрович'),
            Student('Лисина', 'Анжела', 'Ивановна', '30.12.2002', '10 А', 'Лисина Нелля Вадимовна',
                    'Лисин Иван Каримович'),
            ]

teachers = [Teacher('Пермякова', 'Валентина', 'Петровна', 'Математика', '5 А', '6 А', '8 А', '9 А'),
            Teacher('Петров', 'Пётр', 'Андреевич', 'Русский язык', '5 А', '10 А'),
            Teacher('Языкова', 'Тамара', 'Павловна', 'Литература', '5 А', '7 А', '9 А'),
            Teacher('Форсункина', 'Аврора', 'Генадьевна', 'Алгебра', '6 А', '8 А'),
            Teacher('Черпаков', 'Валерий', 'Петрович', 'ОБЖ', '7 А', '8 А'),
            Teacher('Данилин', 'Роберт', 'Владиславович', 'Физ-ра', '7 А', '10 А')
            ]


s = Shcool(students, teachers)

def separator(numb):
    sw = 'Задание №' + str(numb)
    return '\n{:*^70}\n {: ^70}\n'.format(sw, hw[numb])

print(separator(1))
print(s.classroom())
print(separator(2))
print(s.list_of_student_in_the_class('5 А'))
