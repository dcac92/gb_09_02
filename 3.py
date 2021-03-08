import itertools
import sys
usl = []
hol = []
drez = {}

fu = open('users.csv','r', encoding='utf-8')
fh = open('hobby.csv', 'r', encoding='utf-8')
for i in fu:
    usl.append(i.strip())
for i in fh:
    hol.append(i.strip())

print(usl)
print(hol)
fu.close()
fh.close()

if len(usl) > len(hol):
    rez = itertools.zip_longest(usl, hol, fillvalue='none')
else:
    sys.exit(1)
rez1 = tuple(rez)
drez = dict(rez1)
#print(drez)

frez = open('rez.csv', 'w', encoding='utf-8')
for i, k in drez.items():
    frez.write(f'{i}:{k} \n')
frez.close()