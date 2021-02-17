
def num_translate_adv(st):

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

    if st.istitle() == True:

        st = st.lower()

        if bank.get(st) == None:
            return "None"
        else:
            return bank[st].capitalize()
    else:

        if bank.get(st) == None:
            return "None"
        else:
            return bank[st]

st = input("Введите числительное")
print(num_translate_adv(st))
