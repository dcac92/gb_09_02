class Stationery:

    def __init__(self):

        self.title = ''

    def draw(self):

        pass

class Pen(Stationery):

    def draw(self):

        self.title = 'Pen'
        print(f'{self.title}')

class Pencil(Stationery):

    def draw(self):

        self.title = 'Pencil'
        print(f'{self.title}')

class Handle(Stationery):

    def draw(self):

        self.title = 'Handle'
        print(f'{self.title}')

p = Pen()
p1 = Pencil()
p2 = Handle()

p.draw()
p1.draw()
p2.draw()