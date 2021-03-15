
def type_logger(func):
    log1 = {}
    def tl_wrapper(*args):

        nonlocal log1
        for i in args:

            log1.update({type(i):''})

        return log1

    return tl_wrapper


@type_logger
def sum_f(*args):
    return sum(args)

print(sum_f('sum', 2, 3, 4))
