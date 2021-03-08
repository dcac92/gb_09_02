# f = open('bakery.csv', 'w')
# f.close()
def main(ar):
    program, *args = ar
    if args == []:
        #print(args)

        sys.exit('no arguments')

        # f = open('bakery.csv', 'r')
        # for i in f:
        #     print(i.strip())
    else:
        f = open('bakery.csv', 'a')
        for i in args:
            f.write(i + '\n')
        f.close()

    return 0

import sys

main(sys.argv)