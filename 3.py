
number = int(input("Введите число"))

if number == 1  :
    print('1 процент')
elif number == 2 or number == 3 or number == 4 :
    print(number," процента")
else:
    print(number," процентов")

for i in range(1,21,1):
    number = i
    if number == 1:
        print('1 процент')
    elif number == 2 or number == 3 or number == 4:
        print(number, " процента")
    else:
        print(number, " процентов")
