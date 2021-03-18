class Worker:

    def __init__(self, name, surname, income):

        self.name = name
        self.surname = surname
        self._wb = income
        self.wage = income['wage']
        self.bonus = income['bonus']

class Position(Worker):

    def get_fullname(self):

        return f' {self.name} {self.surname}'

    def get_total_income(self):

        return f'Wage + Bonus = {self.wage + self.bonus}'


wb = {
    'wage' : 123,
    'bonus': 50
}
#a = Worker("Ivan", "Noga", wb)
a = Position("Ivan", "Noga", wb)
print(a.get_fullname())
print(a.get_total_income())