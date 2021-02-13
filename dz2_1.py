a = 15 * 3
st = "15 * 3"
type1 = str(type(a))
l = len(type1)

stout = ''
num = type1.index("'")

for i in range(num + 1,l - 2, 1):
    stout += type1[i]

msg = f'Выражение {st} имеет результат {a} который имеет тип {stout}'
print(msg)

a = 15 / 3
st = "15 / 3"
type1 = str(type(a))
l = len(type1)

stout = ''
num = type1.index("'")

for i in range(num + 1,l - 2, 1):
    stout += type1[i]

msg = f'Выражение {st} имеет результат {a} который имеет тип {stout}'
print(msg)

a = 15 // 3
st = "15 // 3"
type1 = str(type(a))
l = len(type1)

stout = ''
num = type1.index("'")

for i in range(num + 1,l - 2, 1):
    stout += type1[i]
msg = f'Выражение {st} имеет результат {a} который имеет тип {stout}'
print(msg)


a = 15 ** 3
st = "15 ** 3"
type1 = str(type(a))
l = len(type1)

stout = ''
num = type1.index("'")

for i in range(num + 1,l - 2, 1):
    stout += type1[i]
msg = f'Выражение {st} имеет результат {a} который имеет тип {stout}'
print(msg)