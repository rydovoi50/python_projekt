class Predmet1:
    def __init__(self, a):
        self.a = a

    # @proper
    def asd(self):
        return self.a * 2


class Predmet2(Predmet1):
    def __init__(self, a, b, c, d, e):
        Predmet1.__init__(self, a)
        self.b = b
        self.c =c
        self.d =d
        self.e =e
        # self.a = a

    def asda(self):
        return self.a * 3

x = Predmet1('a1')
y = Predmet2('a2', 'b2', 'c2', 'd2', 'e2')
print(y.asd())