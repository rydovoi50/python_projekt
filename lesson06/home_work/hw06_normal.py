# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

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
        self.classrom = classroom
        self.subject = subject


class Student(People, School):
    def __init__(self, surname, name, middle_name, date_of_birth, mama, papa, classroom, subject):
        People.__init__(self, surname, name, middle_name, date_of_birth)
        School.__init__(self, classroom, subject)
        self.mama = mama
        self.papa = papa
        self.name = name
        self.middle_name = middle_name
        self.dob = date_of_birth

    @property
    def full_name_st(self):
        return self.surname + ' ' + self.name[0] + '. ' + self.middle_name[0] + '. '


class Teacher(People, School):
    def __init__(self, surname, name, middle_name, date_of_birth, classroom, subject):
        People.__init__(self, surname, name, middle_name, date_of_birth)
        School.__init__(self, classroom, subject)


sub = {
    '5 А': "Математика Русский язык Литература",
    '6 Б': "Математика" "Алгебра",
    '7 В': "ОБЖ" "Физ-ра"
}
students = [Student('Иванов', 'Иван', 'Иванович', '20.02.2003', 'Иванова Зинаида Петровна', 'Иванов Иван Петрович',
                    '5 А', sub['5 А']),
            Student('Забулдыгин', 'Фёдор', 'Павлович', '14.01.2004', 'Забулдыгина Вера Аристарховна',
                    'Забулдыгин Павел Валерьевич', '5 А', sub['5 А']),
            Student('Пипеткина', 'Ксения', 'Александровна', '25.07.2003', 'Пипеткина Галина Павловна',
                    'Пипеткин Александр Валентинович', '6 Б', sub['6 Б']),
            Student('Верещагин', 'Дмитрий', 'Алексеевич', '01.01.2003', 'Верещагина Наталья Андреевна',
                    'Верещагин Алексей Петрович', '6 Б', sub['6 Б']),
            ]

for i in students:
    print(i.full_name_st)
