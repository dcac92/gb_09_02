a = []

for i in range(1,1001,1):
    if i % 2 != 0:
        a.append(i ** 3)

bigsum = 0
for i in range(0, len(a), 1):
    temp = a[i]
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum = sum + digit
        temp = temp // 10
    if sum % 7 == 0:
        bigsum = bigsum + a[i]
       # print("num ",i," ",a[i] ," sum= ",sum,"\n bigsum = ", bigsum)
print("Первая сумма = ", bigsum)

#for i in range(0, len(a), 1):
 #   a[i] += 17

bigsum = 0
for i in range(0, len(a), 1):
    temp = a[i] + 17
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum = sum + digit
        temp = temp // 10
    if sum % 7 == 0:
        bigsum = bigsum + a[i] + 17

print("Вторая сумма = ", bigsum)