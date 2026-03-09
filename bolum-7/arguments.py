# def changeName(n):
#     n = 'Ada'

# name = 'Yiğit'

# changeName(name)
# print(name)

# def change(n):
#     n[0] = 'istanbul'

# sehirler = ['ankara', 'izmir']

# change(sehirler[:])
# print(sehirler)



# def add(*params):
#     print(type(params))
#     sum = 0
#     for n in params:
#         sum += n
#     return sum

# print(add(10, 20, 50))
# print(add(10, 20, 30))
# print(add(10, 20, 30, 50, 60, 10, 20))



def displayUser(**args):
    print(type(args))
    for key, value in args.items():
        print('{} is {}'.format(key, value))

displayUser(name='Çınar', age=2, city='İstanbul')
displayUser(name='Ada', age=12, city='Kocaeli', phone='123456')
displayUser(name='Yiğit', age=14, city='Ankara', phone='9876543', email='yigit@gmail.com')

def myFunc(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10, 20, 30, 40, 50, 60, 70, key1='value1', key2='value2')