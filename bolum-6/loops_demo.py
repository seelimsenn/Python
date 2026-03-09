import random

sayi = random.randint(1, 100)
can = int(input("Kaç hak istiyorsunuz? "))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("Tahmininizi giriniz: "))

    if sayi == tahmin:
        print(f"Tebrikler! {sayac}. denemede bildiniz. Toplam puanınız: {100 - (100/can) * (sayac - 1)} ")
        break
    elif sayi > tahmin:
        print("yukarı")
    else:
        print("aşağı")
    if hak == 0:
        print(f"Hakkınız bitti, tutulan sayı: {sayi}")