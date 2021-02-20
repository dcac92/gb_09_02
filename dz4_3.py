import requests as rq
import datetime

def currency_rates(money_code):

    money_code = money_code.upper()

    r = rq.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    date_num = r.find('Date=') + len('Date=')

    date = r[date_num + 1: date_num + 11: 1]
    day = int(date[0:2:1])
    month = int(date[3:5:1])
    year = int(date[6:10:1])
    date = datetime.date(year, month, day)
    #print(type(date))
    #print(date)

    r_splitChar = r.split('CharCode>')
    r_splitValue = r.split('Value>')

    num = 0
    numf = -1
    for i in r_splitChar:

        num = num + 1

        if i[0:3:1] == money_code:
            numf = num

    num = 0
    for i in r_splitValue:

        num = num + 1

        if num == numf :

           l = i.find("</")
           result = i[0:l:1]
           num = result.find(',')
           l = len(result)
           result = result[0:num:1] + '.' + result[num + 1:l:1]
           break
           result = float(result)

        else:
            result = 'Данный код валюты не найден'

    #print(result)

    return [result, date]

mcode = input('Введите код валюты(любой регистр)')
print(currency_rates(mcode))
