src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 2, 44]

rez = []
[rez.append(i) for i in src if i not in rez]
print(rez)


