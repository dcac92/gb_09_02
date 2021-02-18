from random import randrange

def getjokes(n, flag):

    """Argument 'n' - number of jokes
       Arg 'flag' If flag == 1 do not repeat words else: repeat  """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]




    if flag == 1:

        nouns1 = nouns
        adverbs1 = adverbs
        adjectives1 = adjectives

        for i in range(n):

            result = ""

            l = len(nouns1)
            rand = randrange(l)
            result += nouns1[rand] + ' '
            nouns1.remove(nouns1[rand])

            l = len(adverbs1)
            rand = randrange(l)
            result += adverbs1[rand] + ' '
            adverbs1.remove(adverbs1[rand])

            l = len(nouns1)
            rand = randrange(l)
            result += adjectives1[rand] + ' '
            adjectives1.remove(adjectives1[rand])

            print(f'{result}')
    else:

        for i in range(n):
            result = ""

            l = len(nouns)
            rand = randrange(l)
            result += nouns[rand] + ' '

            l = len(adverbs)
            rand = randrange(l)
            result += adverbs[rand] + ' '

            l = len(nouns)
            rand = randrange(l)
            result += adjectives[rand] + ' '

            print(f'{result}')

n = int(input("Введите количество шуток"))
flag = int(input("Чтобы слова не повторялись введите - 1 "
                 "или любой символ если нет"))
getjokes(n, flag)




