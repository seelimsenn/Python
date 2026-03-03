# sayi = int(input("sayı: "))

# if (sayi > 0):
#     if (sayi % 2 == 0):
#         print("girilen sayı pozitif çift sayıdır.")
#     else:
#         print("girilen say pozitif ancak tek sayıdır.")
# else:
#     print("girilen sayı negatif bir sayıdır.")



# email = 'email@sadikturan.com'
# password = 'abc123'

# girilenEmail = input("email: ")
# girilenPassword = input("password: ")

# if (girilenEmail == email):
#     if (girilenPassword == password):
#         print("giriş başarılı")
#     else:
#         print("parola yanlış")
# else:
#     print("email yanlış")



# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# if (a > b and a > c):
#     print("en büyük a sayısıdır.")
# elif (b > a and b > c):
#     print("en büyük b sayısıdır.")
# elif (c > a and c > b):
#     print("en büyük c sayısıdır.")
# else:
#     print("en büyük sayı bulunamadı.")



# vize1 = int(input("vize1: "))
# vize2 = int(input("vize2: "))
# final = int(input("final: "))

# ortalama = (vize1 + vize2) /2 *0.6 + (final * 0.4)

#1. durum
# if (ortalama >= 50):
#     if (final >= 50):
#         print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu başarılı')
#     else:
#         print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu başarısız, finalden en az 50 almalısınız.')
# else:
#     print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu başarısız')

#2. durum
# if (ortalama >= 50):
#     print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu başarılı')
# else:
#     if (final >= 70):
#         print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu başarılı, finalden en az 70 aldığınız için geçtiniz.')
#     else:
#         print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu başarısız')



name = input("adınız: "),
kg = float(input("kilonuz: "))
hg = float(input("boyunuz: "))

index = kg / (hg ** 2)

if (index >= 0 and index < 18.4):
    print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf.')
elif (index >= 18.5 and index < 24.9):
    print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen normal.')
elif (index >= 25 and index < 29.9):
    print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu.')
elif (index >= 30 and index < 34.9):
    print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen obez.')
else:
    print('bilgileriniz yanlış.')