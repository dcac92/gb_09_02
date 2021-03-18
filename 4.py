class Car:

    def __init__(self, speed, color, name, is_police):

        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):

        return self.speed

class TownCar(Car):

    def show_speed(self):

        if self.speed > 60:

            return f'overspeed'

        else:

            return self.speed

class SportCar(Car):

    pass

class WorkCar(Car):

    def show_speed(self):

        if self.speed > 40:

            return f'overspeed'

        else:

            return self.speed

class PoliceCar(Car):

    pass

a = WorkCar(60, 'red', 'yoriki', True)
b = PoliceCar(100, 'white', 'policecar', False)
c = SportCar(200, 'red', 'bingo', True)
d = TownCar(61, 'green', 'town', False)

print(d.show_speed())
print(c.show_speed())
print(a.show_speed())
print(b.show_speed())


