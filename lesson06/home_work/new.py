class Predmet1:
    def __init__(self, a):
        self.a = a
    a = 80

    def asd(self):
        return self.a**2


class Predmet2(Predmet1):
    def __init__(self, a, b):
        Predmet1.__init__(self, a)
        self.b = b
        # self.a = aa

    def asda(self):
        return self.a + 3

x = Predmet1(8)
y = Predmet2(2, 3)
print(y.asda())