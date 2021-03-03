src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

l = len(src)
rez = [src[i] for i in range(1, l, 1) if src[i] > src[i - 1]]

print(rez)
