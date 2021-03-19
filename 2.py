class Wear:

    def __init__(self, param):
        self.name = ''
        self.param = param

    def calc(self, param):
        pass


class Coat(Wear):
    def __init__(self, param):
        Wear.__init__(self, param)
        self.name = 'Coat'

    @property
    def calc(self):
        self.rez = (self.param/6.5 + 0.5)
        return self.rez

    def __add__(self, other):
        self.rezad = self.calc + other.calc
        return self.rezad


class Smoking(Wear):

    def __init__(self, param):
        Wear.__init__(self, param)
        self.name = 'Smoking'

    @property
    def calc(self):
        self.rez = (self.param * 2 + 0.3)
        return self.rez

    def __add__(self, other):
        self.rezad = self.calc + other.calc
        return self.rezad


c = Coat(13)
c1 = Smoking(8)
print(c.calc)
print(c1.calc)
print(c.name)
print(c1.name)
rez = c + c1
print(rez)
