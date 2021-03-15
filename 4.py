def logger(funcval):
    def _logger(func):
        def wrapper(*args):

            if funcval(*args):
                rez = func(*args)

            else:

                raise ValueError

            return rez

        return wrapper

    return _logger

@logger(lambda x: x > 0)
def calc_cube(y):
    return y ** 3

y = -3
try:
    print(calc_cube(y))

except ValueError:
    print(f'ValueError {y}')
    exit(1)

