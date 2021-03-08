
rez = ()
with open('nginx_logs.txt', 'r') as f:
    ftmp = open('tmp.txt','w')  #Записываем ip адреса всех запросов в tmp.txt
    for i in f:

        str1 = i
        strf = str1.split(' ')
        rez = (strf[0], strf[5], strf[6])
        print(rez)
        ftmp.write(strf[0] + '\n')

    ftmp.close()

f = open('tmp1.txt', 'w')
f.close()

with open('tmp.txt', 'r') as f:

    for i in f:

        ip = i
        print(ip.strip())
        flag = 0
        ftmp = open('tmp1.txt', 'r')   #записываем ip которые были в запросах

        for j in ftmp:

            if ip == j:

                flag = 1

        if flag == 0:

            ftmp.close()
            ftmp = open('tmp1.txt', 'a')
            ftmp.write(ip)
            ftmp.close()
        else:
            ftmp.close()
fw = open('tmprez.txt', 'w')
fw.close()
fw = open('tmprez.txt', 'a')
fr1 = open('tmp1.txt', 'r')


for i in fr1:
    print(i)
    count = 0
    fr = open('tmp.txt', 'r')
    for j in fr:

       if i == j :
           count += 1

    fw.write(i.strip() + ' ' + str(count)+'\n')
    fr.close()


fr1.close()
fw.close()

f = open('tmprez.txt', 'r')
max= 0
ip = 0
for i in f:

    lst = i.split(' ')
    if max < int(lst[1]):

        max = int(lst[1])
        ip = i
f.close()
print(f' Spamer ip = {ip} Requests = {max}')



# print(type(str))