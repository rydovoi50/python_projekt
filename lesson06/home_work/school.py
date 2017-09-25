hw = {1: 'Получить полный список всех классов школы',
      2: '''Получить список всех учеников в указанном классе\n(каждый ученик отображается в формате "Фамилия И.О.")''',
      3: '''Получить список всех предметов указанного ученика\n(Ученик --> Класс --> Учителя --> Предметы)''',
      4: 'Узнать ФИО родителей указанного ученика',
      5: 'Получить список всех Учителей, преподающих в указанном классе',
      6: ''}


class MySchool:
    def __init__(self, name_school, teachers=None, students=None):
        self.name_school = name_school
        self.teachers = []
        self.students = []
        self.teachers.extend(teachers)
        self.students.extend(students)
        # print(self.students)

    def all_classes(self):  # 1 задание
        classrooms = []
        for x in self.teachers:
            classrooms.extend(x.classroom)
        for x in self.students:
            classrooms.append(x.classroom)
        return list(set(classrooms))

    def stud_for_class(self, number=str):  # 2 задание
        cl = []
        for x in self.students:
            if x.classroom == number:
                cl.append(x.fio_short)
        return cl

    def stud_subj(self, *data):  # 3 задание
        for y in self.students:
            if ' '.join(data) == y.fio:
                teacher_in_class = []
                subject_in_class = []
                for _ in self.teachers:
                    for z in _.classroom:
                        if z == y.classroom:
                            teacher_in_class.append(_.fio)
                            subject_in_class.append(_.subject)
                return 'У данного ученика:\t{},\t{} класса,\n' \
                       'преподают следующие учителя:\t{}\n' \
                       'следующие уроки:\t{}'.format(y.fio, y.classroom, teacher_in_class, subject_in_class)

    def fio_parents(self, *data):  # 4 задание
        for y in self.students:
            if ' '.join(data) == y.fio:
                return y.parents

    def class_teachers(self, number_cl):  # 5 задание
        list_teacher = []
        for x in self.teachers:
            if number_cl in x.classroom:
                list_teacher.append(x.fio)
        return list_teacher

    def __str__(self):
        y = [x.fio for x in self.teachers]
        return str(y)


class MyPeople:
    def __init__(self, surname, first_name, patronymic):
        self.surname = surname
        self.first_name = first_name
        self.patronymic = patronymic
        self.fio = ' '.join([self.surname, self.first_name, self.patronymic])
        self.fio_short = ' '.join([self.surname, (self.first_name[0] + '.'), (self.patronymic[0] + '.')])


class MyTeacher(MyPeople):
    def __init__(self, *data):
        super().__init__(*data[0:3])
        self.subject = data[3]
        self.classroom = []
        self.classroom.extend([i for i in data[4:]])

    def append_classroom(self, classroom):
        self.classroom.append(classroom)

    def __str__(self):
        return 'ФИО преподавателя:\t\t\t\t{}\n' \
               'Предмет:\t\t\t\t\t\t{}\n' \
               'Классы, в которых ведет урок:\t{}'.format(self.fio, self.subject, ', '.join(self.classroom))


class MyStudent(MyPeople):
    def __init__(self, *data, **parents):
        super().__init__(*data[0:3])
        self.classroom = data[3]
        self.parents = {}
        for key in parents:
            self.parents[key] = parents[key]

    def __str__(self):
        return '{} - {}'.format(self.fio_short, self.fio)


students = [MyStudent('Иванов', 'Иван', 'Иванович', '5 А',
                      mother='Иванова Зинаида Петровна',
                      father='Иванов Иван Петрович'),
            MyStudent('Забулдыгин', 'Фёдор', 'Павлович', '5 А',
                      mother='Забулдыгина Вера Аристарховна',
                      father='Забулдыгин Павел Валерьевич'),
            MyStudent('Пипеткина', 'Ксения', 'Александровна', '6 A',
                      mother='Пипеткина Галина Павловна',
                      father='Пипеткин Александр Валентинович'),
            MyStudent('Верещагин', 'Дмитрий', 'Алексеевич', '6 A',
                      mother='Верещагина Наталья Андреевна',
                      father='Верещагин Алексей Петрович'),
            MyStudent('Антонов', 'Анатолий', 'Аникеевич', '8 А',
                      mother='Антонова Галина Владимировна',
                      father='Антонов Аникей Львович'),
            MyStudent('Москвин', 'Владимир', 'Анатольевич', '7 A',
                      mother='Москвина Вероника Антоновна',
                      father='Москвин Анатолий Сергеевич'),
            MyStudent('Рожкова', 'Инна', 'Александровна', '9 А',
                      mother='Рожкова Анастасия Артуровна',
                      father='Рожков Александр Александрович'),
            MyStudent('Лисина', 'Анжела', 'Ивановна', '10 А',
                      mother='Лисина Нелля Вадимовна',
                      father='Лисин Иван Каримович')
            ]

teachers = [MyTeacher('Пермякова', 'Валентина', 'Петровна', 'Математика', '5 А', '6 A', '8 А', '9 А'),
            MyTeacher('Петров', 'Пётр', 'Андреевич', 'Русский язык', '5 А', '10 А'),
            MyTeacher('Языкова', 'Тамара', 'Павловна', 'Литература', '5 А', '7 A', '9 А'),
            MyTeacher('Форсункина', 'Аврора', 'Генадьевна', 'Алгебра', '6 A', '8 А'),
            MyTeacher('Черпаков', 'Валерий', 'Петрович', 'ОБЖ', '7 A', '8 А'),
            MyTeacher('Данилин', 'Роберт', 'Владиславович', 'Физ-ра', '7 A', '10 А')
            ]


def wk(number):
    work = ' Задание № ' + str(number) + ' '
    return '\n{:=^70}\n\"{}\"\n'.format(work, hw[number])

s = MySchool('СШ №4', teachers=teachers, students=students)
print(wk(1))
print(s.all_classes())
print(wk(2))
# print(s.stud_for_class('5 А'))
print(s.stud_for_class(number='6 A'))
print(wk(3))
print(s.stud_subj('Иванов', 'Иван', 'Иванович'))
print(wk(4))
print(s.fio_parents('Иванов', 'Иван', 'Иванович'))
print(wk(5))
print(s.class_teachers('5 А'))
print(wk(6))
print(s)
