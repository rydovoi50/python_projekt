# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def check(self):
        ab = ((self.a[0] - self.b[0]) ** 2 + (self.a[1] - self.b[1]) ** 2) ** 0.5
        bc = ((self.b[0] - self.c[0]) ** 2 + (self.b[1] - self.c[1]) ** 2) ** 0.5
        ca = ((self.c[0] - self.a[0]) ** 2 + (self.c[1] - self.a[1]) ** 2) ** 0.5
        return ab < bc + ca and bc < ab + ca and ca < ab + bc

    @property
    def perimeter(self):
        ab = ((self.a[0] - self.b[0]) ** 2 + (self.a[1] - self.b[1]) ** 2) ** 0.5
        bc = ((self.b[0] - self.c[0]) ** 2 + (self.b[1] - self.c[1]) ** 2) ** 0.5
        ca = ((self.c[0] - self.a[0]) ** 2 + (self.c[1] - self.a[1]) ** 2) ** 0.5
        return ab + bc + ca

    @property
    def height(self):
        ab = ((self.a[0] - self.b[0]) ** 2 + (self.a[1] - self.b[1]) ** 2) ** 0.5
        bc = ((self.b[0] - self.c[0]) ** 2 + (self.b[1] - self.c[1]) ** 2) ** 0.5
        ca = ((self.c[0] - self.a[0]) ** 2 + (self.c[1] - self.a[1]) ** 2) ** 0.5
        p = (ab + bc + ca) / 2
        return 2 / bc * (p * (p - bc) * (p - ca) * (p - ab)) ** 0.5

    @property
    def area(self):
        ab = ((self.a[0] - self.b[0]) ** 2 + (self.a[1] - self.b[1]) ** 2) ** 0.5
        bc = ((self.b[0] - self.c[0]) ** 2 + (self.b[1] - self.c[1]) ** 2) ** 0.5
        ca = ((self.c[0] - self.a[0]) ** 2 + (self.c[1] - self.a[1]) ** 2) ** 0.5
        p = (ab + bc + ca) / 2
        return (p * (p - bc) * (p - ca) * (p - ab)) ** 0.5


d = Triangle((1, 3), (5, 1), (8, 11))
w = Triangle((1, 3), (4, 6), (6, 8))
print('Невырожденный - ', w.check)
print('Периметр = ', w.perimeter)
print('Высота = ', w.height)
print('Площадь = ', w.area)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapezoid:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


    @property
    def check(self):
        c = ((self.a[0] - self.b[0]) ** 2 + (self.a[1] - self.b[1]) ** 2) ** 0.5
        d = ((self.c[0] - self.d[0]) ** 2 + (self.c[1] - self.d[1]) ** 2) ** 0.5
        ac = ((self.a[0] - self.c[0]) ** 2 + (self.a[1] - self.c[1]) ** 2) ** 0.5
        bd = ((self.b[0] - self.d[0]) ** 2 + (self.b[1] - self.d[1]) ** 2) ** 0.5
        return c == d and ac == bd


    @property
    def side(self):
        c = ((self.a[0] - self.b[0]) ** 2 + (self.a[1] - self.b[1]) ** 2) ** 0.5
        a = ((self.b[0] - self.c[0]) ** 2 + (self.b[1] - self.c[1]) ** 2) ** 0.5
        d = ((self.c[0] - self.d[0]) ** 2 + (self.c[1] - self.d[1]) ** 2) ** 0.5
        b = ((self.d[0] - self.a[0]) ** 2 + (self.d[1] - self.a[1]) ** 2) ** 0.5
        return c, d, a, b


    @property
    def perimeter(self):
        c = ((self.a[0] - self.b[0]) ** 2 + (self.a[1] - self.b[1]) ** 2) ** 0.5
        a = ((self.b[0] - self.c[0]) ** 2 + (self.b[1] - self.c[1]) ** 2) ** 0.5
        d = ((self.c[0] - self.d[0]) ** 2 + (self.c[1] - self.d[1]) ** 2) ** 0.5
        b = ((self.d[0] - self.a[0]) ** 2 + (self.d[1] - self.a[1]) ** 2) ** 0.5
        return c + a + d + b

    @property
    def area(self):
        c = ((self.a[0] - self.b[0]) ** 2 + (self.a[1] - self.b[1]) ** 2) ** 0.5
        a = ((self.b[0] - self.c[0]) ** 2 + (self.b[1] - self.c[1]) ** 2) ** 0.5
        d = ((self.c[0] - self.d[0]) ** 2 + (self.c[1] - self.d[1]) ** 2) ** 0.5
        b = ((self.d[0] - self.a[0]) ** 2 + (self.d[1] - self.a[1]) ** 2) ** 0.5
        return (a + b) / 2 * (c ** 2 - 1/4 * (((c - d) ** 2 / (b - a)) + b - a) ** 2) ** 0.5


trap = Trapezoid((1, 1), (2, 4), (5, 4), (6, 1))
print('Равнобедренный = ', trap.check)
print('Стороны = ', trap.side)
print('Периметр = ', trap.perimeter)
print('Площадь = ', trap.area)
