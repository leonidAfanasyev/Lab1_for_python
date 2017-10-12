sonya = {
    'name': 'sonya',
    'age': 34,
    'children': [{
        'name': 'vasja',
        'age': 12,
    }, {
        'name': 'petja',
        'age': 10,
    }],
}

daria = {
    'name': 'daria',
    'age': 41,
    'children': [{
        'name': 'kirill',
        'age': 21,
    }, {
        'name': 'pavel',
        'age': 15,
    }],
}

emps = [sonya, daria]


def hasAdultChildren (x):
    n = []
    for person in x:
            for childen in person['children']:
                if childen['age'] >= 18:
                    n.append(person['name'])
    return n

print (hasAdultChildren(emps))
