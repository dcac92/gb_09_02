class Data:
    def __init__(self, st):
        self.st = st

    @classmethod
    def st_parse_1(cls, st):
        sttemp = st.split('-')
        d = int(sttemp[0])
        sttemp[0] = d
        m = int(sttemp[1])
        sttemp[1] = m
        y = int(sttemp[2])
        sttemp[2] = y
        return  sttemp

    @staticmethod
    def data_validation(st):
        k = True
        if (st[0] > 0) and (1 <= st[0] <= 31):
            pass
        else:
            print('Day format is not correct')
            k = False

        if (st[1] > 0) and (1 <= st[1] <= 12):
           pass
        else:
            print('Month format is not correct')
            k = False

        if (st[2] > 0) and (1975 <= st[2] <= 2099):
           pass
        else:
            print('Month format is not correct')
            k = False

        if k == False:
            return False
        else:
            return True




st = '01-02-2020'
print(Data.st_parse_1(st))
st = Data.st_parse_1(st)
Data.data_validation(st)