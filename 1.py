class Matrix:
    def __init__(self, l):

        self.l = l
        self.st =''

    def __str__(self):

        for i in self.l:
            for j in i:
                self.st += str(j) + ' '
            self.st += '\n'

        return self.st

    def __add__(self, other):

        self.rez = []
        self.ltemp = []

        for i in range(len(self.l)):
            for j in range(len(self.l[0])):
                self.ltemp.append(self.l[i][j] + other.l[i][j])
            self.rez.append(self.ltemp)
            self.ltemp = []

        return Matrix(self.rez)


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
m1 = Matrix(a)
m2 = Matrix(b)
print(m1 + m2)
