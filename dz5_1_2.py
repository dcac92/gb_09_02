def gen1(n):
    for i in range(1, n, 2):
        yield i

n = int(input('Введите n'))

# 1 задача с yield
g1 = gen1(n)
for i in g1:
    print(i)

# 2 задача без yield
gen = (i for i in range(1, n, 2))

for i in gen:
     print(i)
