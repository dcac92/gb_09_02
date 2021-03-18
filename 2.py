class Road:

    def __init__(self, width, length):

        self.__width = width
        self.__length = length

    def calc(self, thick):
        rez = self.__length * self.__width * thick
        print(rez)

a = Road(3, 150)
a.calc(0.5)
