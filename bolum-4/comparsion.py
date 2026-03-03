# a = int(input("a: "))
# b = int(input("b: "))

# result = (a > b)
# print(f'a: {a} b: {b} den büyüktür: {result}')


# vize1 = float(input("vize 1: "))
# vize2 = float(input("vize 2: "))
# final = float(input("final: "))

# ortalama = ((vize1 + vize2) / 2 * 0.6) + (final * 0.4)

# print(f'not ortalamanız: {ortalama} ve dersten geçme durumunuz: {ortalama >= 50}')


# sayi = int(input("sayı: "))

# tekcift = (sayi % 2 == 0)

# print(f'girilen sayının çift olma durumu: {tekcift}')


# sayi = int(input("sayı: "))
# pozitifmi = (sayi > 0)

# print(f'girilen sayının pozitif olma durumu: {pozitifmi}')


email = 'email@sadikturan.com'
password = 'abc123'

girilenEmail = input("email: ")
girilenPassword = input("parola: ")

isEmail = (email == girilenEmail.lower().strip())
isPassword = (password == girilenPassword.lower())

print(f'email bilgisi doğru mu: {isEmail} ve parola doğru mu: {isPassword}')