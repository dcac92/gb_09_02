class DivZero(Exception):
    def __init__(self, txt):
        self.t = txt


while True:
    try:
        a = int(input('Введите a, a / b'))
        b = int(input('Введите b'))

        if b == 0:
            raise DivZero('Деление на ноль')
        else:
            c = a / b
            print(c)
    except DivZero as er:
        print(er)



