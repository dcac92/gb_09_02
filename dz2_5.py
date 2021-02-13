list1 = [15.69, 25.05, 36, 50, 96.70, 4.25, 7.62]
num = 0
l = len(list1)

for i in range(l):

    temp = list1[i]

    if type(temp) is int:

        print(f'{temp} руб. 00 коп.')

    else:
        rub = int(temp)

        stkop = str(temp)
        l1 = len(stkop)

        for j in range(l1):
            if stkop[j] == ".":
                num = j

        if l1 - num == 2:
            print(f'{rub} руб. {stkop[num+1:]+"0"} коп.')
        else:
            print(f'{rub} руб. {stkop[num+1:]} коп.')

# B
print("id = ", id(list1))
list1.sort()
print(f"id = {id(list1)} "
      f" список в порядке возрастания {list1}")

#C
listnew = []
l = len(list1)

for i in range(l - 1,-1,-1):
    listnew.append(list1[i])
print(f'Список в порядке убывания {listnew}')
#D
print(f'5 самых дорогих товаров {listnew[:5]}')





