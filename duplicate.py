import json


def duplicate():
    with open('Store.json') as f:
        data = json.loads(f.read())

    all = []
    for key, value in data.items():
        v = str(value)
        print(v)
        all.append(v)


def check(a):
    a = a.strip(')])').lstrip('ImmutableMultiDict([(').replace(",", ":")
    a = "{"+a+"}"
    for i in all:
        if i in a:
            return True
        else:
            return False
