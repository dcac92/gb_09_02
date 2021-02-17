
def name_surname_capitals(ns):
    temp = ns.split(" ")

    ncap = temp[0][0]
    scap = temp[1][0]
    rez = [ncap, scap]
    return rez
    #print(f" name = {n} surname = {s}")


def name_surname(ns):
    temp = ns.split(" ")

    n = temp[0]
    s = temp[1]
    rez = [n, s]
    return rez



def thesaurus_adv(*args):
    result_dict = {}
    result_dict_in = {}


    l = len(args)

    for i in range(0, l, 1):

        nscap = name_surname_capitals(args[i])
        ncap = nscap[0]
        scap = nscap[1]

        if result_dict.get(scap) == None:

            result_dict[scap] = {ncap : [args[i]]}

        else:
            if result_dict[scap].get(ncap) == None:
                result_dict[scap][ncap] = [args[i]]
            else:
                result_dict[scap][ncap].append(args[i])

    return  result_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))

