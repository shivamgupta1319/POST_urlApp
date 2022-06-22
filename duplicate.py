import json


def duplicate():
    with open('Store.json') as f:
        data = json.loads(f.read())
        print(data)

    all = []
    for key, value in data.items():
        print(key)
        print(value)
        all.append(value)

    return all
