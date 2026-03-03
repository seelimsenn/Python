# isim = input("isminiz: ")
# yas = int(input("yaşınız: "))
# egitim = input("eğitim durumunuz: ")

# if (yas >= 18):
#     if (egitim == "lise" or egitim == "üniversite"):
#         print(f"{isim} ehliyet alabilirsiniz.")
#     else:
#         print(f"{isim} ehliyet alamazsınız, eğitim durumunuz yetersiz.")
# else:
#     print(f"{isim} ehliyet alamazsınız, yaşınız tutmuyor.")


# yazili1= int(input("1. yazılı: "))
# yazili2= int(input("2. yazılı: "))
# sozlu= int(input("sözlü: "))

# ortalama = (yazili1 + yazili2 + sozlu) / 3

# if (ortalama >= 0) and (ortalama < 25):
#     print(f"ortalamanız: {ortalama} notunuz: 0")
# elif (ortalama >= 25) and (ortalama < 45):
#     print(f"ortalamanız: {ortalama} notunuz: 1")
# elif (ortalama >= 45) and (ortalama < 55):
#     print(f"ortalamanız: {ortalama} notunuz: 2")
# elif (ortalama >= 55) and (ortalama < 70):
#     print(f"ortalamanız: {ortalama} notunuz: 3")
# elif (ortalama >= 70) and (ortalama < 85):
#     print(f"ortalamanız: {ortalama} notunuz: 4")
# elif (ortalama >= 85) and (ortalama <= 100):
#     print(f"ortalamanız: {ortalama} notunuz: 5")
# else:
#     print("geçersiz not girdiniz.")


import datetime

tarih = input('aracınız hangi tarihte trafiğe çıktı (gg/aa/yyyy): ')
tarih = tarih.split('/')
trafigeCkis = datetime.datetime(int(tarih[2]), int(tarih[1]), int(tarih[0]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCkis
days = fark.days

if (days <= 365):
    print("aracınız 1. servis aralığında.")
elif (days > 365) and (days <= 365*2):
    print("aracınız 2. servis aralığında.")
elif (days > 365*2) and (days <= 365*3):
    print("aracınız 3. servis aralığında.")
else:
    print('hatalı süre girdiniz.')