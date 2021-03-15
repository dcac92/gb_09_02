import re

def email_parse(s):

    rez_dict = {}
    RE_DATE = re.compile(r'(\w+)@(\w+)')
    try:

        assert RE_DATE.findall(s)

    except AssertionError as e:

        raise ValueError

    else:

        rez = RE_DATE.findall(s)

    RE_DATE = re.compile(r'\w+@[a-zA-Z]+\.[a-zA-Z]')
    try:
        assert RE_DATE.match(s)

    except AssertionError as e:
        raise ValueError

    #print(RE_DATE.match(s))

    rez_dict = {rez[0][0] : rez[0][1]}

    return rez_dict

try:

    print(email_parse('fgnhtyugmail.com'))

except ValueError:

    print('ValueError')
    exit(1)

except Exception:

    print('Global Exception')
