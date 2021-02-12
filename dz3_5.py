list1 = [15.69, 25.50, 36, 50, 96.70, 4.25, 7.62]
num = 0
l = len(list1)

for i in range(l):
    temp = list1[i]
    if type(temp) is int:
        print('int')
    else:
        st = str(temp)
        l1 = len(st)
        for j in range(l1):
            if st[j] == ".":
                num = j
        print(st[:num])



