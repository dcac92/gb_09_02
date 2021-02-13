list1 = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
         'токарь высшего разряда нИКОЛАй', 'директор аэлита']
num_space = 0
l = len(list1)

for i in range(l):

    st = ''
    temp = list1[i]
    l1 = len( temp )

    for j in range(l1):
        if temp[j] == ' ':
            num_space = j

    for j in range(num_space + 1, l1, 1):
        st = st + temp[j]

        st = st.capitalize()
    print(st, ' ')


