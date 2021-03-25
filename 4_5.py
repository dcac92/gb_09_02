class Store:
    store_list = {
        'printer' : [0],
        'scaner' : [0],
        'xerox' : [0],
    }
    b = 5
    @staticmethod
    def take(*equipment):

        for equipment in equipment:
            Store.store_list[equipment.type].append((equipment.price, equipment.chrs))
            Store.store_list[equipment.type][0] += 1

class Equipment:
    def __init__(self, type, price, chrs):
        self.type = type
        self.price = price
        self.chrs = chrs


class Printer(Equipment):
    pass


class Xerox(Equipment):
    pass


class Scaner(Equipment):
    pass

p1 = Printer('printer', 150, 'some')
p2 = Printer('printer', 250, 'some2')
x1 = Xerox('xerox', 150, 'some')
Store.take(p1, p2, x1)
print(Store.store_list)


