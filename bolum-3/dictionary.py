#key - value

#41 =>kocaeli 34=> istanbul

# sehirler = ['kocaeli','istanbul']
# plakalar = [41,34]

# print(plakalar[sehirler.index('istanbul')])

#print(plakalar['kocaeli']) =>41
#print(plakalar['istanbul']) =>34

# plakalar = {'kocaeli':41,'istanbul':34}

# print(plakalar['kocaeli'])
# print(plakalar['istanbul'])

# plakalar['ankara'] = 6
# print(plakalar)
# plakalar['kocaeli'] = 'new value'
# print(plakalar)

users = {
    'sadikturan': {
        'age': 36,
        'roles': ['user'],
        'email': 'sadik@gmail.com',
        'address': 'kocaeli',
        'phone': '12345678'
    },
    'cinarturan': {
        'age': 25,
        'roles': ['admin', 'user'],
        'email': 'cinar@gmail.com',
        'address': 'istanbul',
        'phone': '098765434'
    }
}

print(users['sadikturan']["roles"][0])