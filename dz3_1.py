
def num_translate(st):

    bank = {
        "one" : "один",
        "two" : "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять"
    }


    if bank.get(st) == None:
        return "None"
    else:
        return bank[st]


st = input("Введите числительное")
print( num_translate(st) )

