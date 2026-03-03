# sayi = float(input("sayı: "))

# result = (sayi > 0) and (sayi <= 100)
# print(f'sayı 0 ile 100 arasında mı: {result}')

# sayi = int(input("sayı: "))
# result = (sayi > 0) and (sayi % 2 == 0)
# print(f'girilen sayı pozitif çift sayı mı: {result}')

# email = 'email@sadikturan.com'
# password = 'abc123'

# girilenEmail = input("email: ")
# girilenPassword = input("password: ")

# result = (girilenEmail == email) and (girilenPassword == password)
# print(f'uygulamaya giriş başarılı mı: {result}')

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# result = (a > b) and (a > c)
# print(f'a en büyük sayıdır: {result}')

# result = (b > a) and (b > c)
# print(f'b en büyük sayıdır: {result}')

# result = (c > a) and (c > b)
# print(f'c en büyük sayıdır: {result}')


# vize1 = float(input("vize 1: "))
# vize2 = float(input("vize 2: "))
# final = float(input("final: "))

# ortalama = ((vize1 + vize2) / 2 * 0.6) + (final * 0.4)
# #result = (ortalama >= 50) and (final >= 50)
# result = (ortalama >= 50) or (final >= 70)

# print(f'not ortalamanız: {ortalama} ve dersten geçme durumunuz: {result}')


name = input("adınız: ")
kg = float(input("kilonuz: "))
hg = float(input("boyunuz: "))

index = kg / (hg ** 2)
zayif = (index >= 0) and (index <= 18.4)
normal = (index > 18.4) and (index <= 24.9)
kilolu = (index > 24.9) and (index <= 29.9)
obez = (index > 29.9) and (index <= 34.9)

print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {zayif}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen normal: {normal}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu: {kilolu}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen obez: {obez}')