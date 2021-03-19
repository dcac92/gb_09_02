def gen(obj, n):
    i = 0
    str = ''
    while i < obj.param:
        str += '*'
        i += 1
        if obj.param < n:
            if i == obj.param:
                str += '\n'
        else:
            if i % n == 0:
                str += '\n'
    return str

def obj_eq(a, b):
    if a.__class__ == b.__class__ :
        return True
    else:
        False

class Cell:

    def __init__(self, param):
        self.param = param

    def __add__(self, other):
        if obj_eq(self, other):
            sum = self.param + other.param
            return Cell(sum)
        else:
            print(f'different objects')

    def __sub__(self, other):
        if obj_eq(self, other):
            if self.param > other.param:
                sum = self.param - other.param
                return Cell(sum)
            else:
                print(f'self.p < other.p')
        else:
            print(f'different objects')

    def __mul__(self, other):
        if obj_eq(self, other):
            sum = self.param * other.param
            return Cell(sum)
        else:
            print(f'different objects')

    def __truediv__(self, other):
        if obj_eq(self, other):
            sum = self.param // other.param
            return Cell(sum)
        else:
            print(f'different objects')

    def make_order(self, n):
        return gen(self, n)


a1 = Cell(50)
a2 = Cell(7)
rez = a1 * a2
print(rez.param)
rez = a1 + a2
print(rez.param)
rez = a1 - a2
print(rez.param)
#rez = a2 - a1
print(rez.param)
rez = a2 / a1
print(rez.param)
rez = a1 / a2
print(rez.param)
print(a1.make_order(3))










