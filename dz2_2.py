list1 = ['в', '5', 'часов', '17', 'минут', 'температура',
         'воздуха', 'была', '+5', 'градусов']

list2 = []

for i in range( len(list1) ):
    dig = True

    temp = list1[i]

    if temp[0] == "+":

        temp = temp.replace('+', '')

        l = len(temp)
        for j in range(1,l,1):

            if temp[j].isdigit() != True:
                dig = False

        if dig == True and l < 2:
            #print(temp," ")
            temp1 = "+" + '0' + temp
            list2.append("'")
            list2.append(temp1)
            list2.append("'")

        elif dig == True and l > 2:
            temp1 = "+" + temp
            list2.append("'")
            list2.append(temp1)
            list2.append("'")

    elif temp[0] == "-":

        temp = temp.replace('-', '')

        l = len(temp)
        for j in range(1,l,1):

            if temp[j].isdigit() != True:
                dig = False

        if dig == True and l < 2:
            #print(temp," ")
            temp1 = "-" + '0' + temp
            list2.append("'")
            list2.append(temp1)
            list2.append("'")

        elif dig == True and l > 2:
            temp1 = "-" + temp
            list2.append("'")
            list2.append(temp1)
            list2.append("'")
    else:
        l = len(temp)
        for j in range(0, l, 1):

            if temp[j].isdigit() != True:
                dig = False

        if dig == True and l < 2:
            #print(temp, " ")
            temp1 = '0' + temp
            list2.append("'")
            list2.append(temp1)
            list2.append("'")
        else:
            temp1 = temp
            list2.append(temp1)


    print(temp1)

print(list2)





