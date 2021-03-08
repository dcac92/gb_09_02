def main(ar):
    program, *args =ar

    if len(args) == 0:

        f = open('bakery.csv', 'r')
        for i in f:
            print(i.strip())
        f.close()

    elif len(args) == 1:

        count = 0
        f = open('bakery.csv', 'r')

        for i in f:

            count += 1

            if count >= int(args[0]):
                print(i.strip())
        f.close()

    elif len(args) == 2:
        count = 0
        f = open('bakery.csv', 'r')

        for i in f:

            count += 1

            if count >= int(args[0]) and count <= int(args[1]):
                print(i.strip())
        f.close()

    return 0

import sys

main(sys.argv)