class Int_Only(Exception):
    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def run():
        l = []
        while True:
            try:
                st = input('Введите данные')
                if st.isdigit():
                    l.append(int(st))
                elif st == 'stop':
                    print(l)
                    exit(1)
                else:
                    raise Int_Only('Некорректные данные')
            except Int_Only as err:
                print(err)


Int_Only.run()



