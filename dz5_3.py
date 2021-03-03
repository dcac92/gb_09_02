tutors = [
    'Иван', 'Алексей', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', #'10А', '10Б', '9А', '11'
]

def gen1(a, b):

    lt = len(tutors)
    lk = len(klasses)

    if lt == lk :

        c = list(zip(a, b))

    elif lt < lk :

        for i in range(1, lk - lt, 1):
            tutors.append('None')
        c = list(zip(a, b))

    elif lt > lk :

        for i in range(1, lt - lk, 1):
            klasses.append('None')
        c = list(zip(a, b))

    for i in c:
        yield i

g = gen1(tutors, klasses)

print(type(g))
for i in range(100):
    print(next(g))


