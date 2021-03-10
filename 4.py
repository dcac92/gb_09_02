import os

p1 = [item for item in os.walk(os.getcwd())]
print(os.getcwd())

rez_dict = {

}
zer_count = 0
ten_count = 0
hun_count = 0
ths_count = 0

for i in p1:
    #print(i)
    for files in i[2]:

        #print(os.stat(os.path.join(i[0], files)).st_size)
        if os.stat(os.path.join(i[0], files)).st_size == 0:
            zer_count += 1
        elif os.stat(os.path.join(i[0], files)).st_size > 10:
            ten_count += 1
        elif os.stat(os.path.join(i[0], files)).st_size > 100:
            hun_count += 1
        elif os.stat(os.path.join(i[0], files)).st_size > 1000:
            ths_count += 1

rez_dict.update({0:zer_count,
                 10:ten_count,
                 100:hun_count,
                 1000:ths_count
                 })
print(rez_dict)