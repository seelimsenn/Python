def ortalama_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")
    ad_soyad = liste[0]
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3

    if ortalama >= 90 and ortalama <= 100:
        harf_notu = "AA"
    elif ortalama >= 85 and ortalama < 90:
        harf_notu = "BA"
    elif ortalama >= 80 and ortalama < 85:
        harf_notu = "BB"
    elif ortalama >= 75 and ortalama < 80:
        harf_notu = "CB"
    elif ortalama >= 70 and ortalama < 75:
        harf_notu = "CC"
    elif ortalama >= 65 and ortalama < 70:
        harf_notu = "DC"
    elif ortalama >= 60 and ortalama < 65:
        harf_notu = "DD"
    elif ortalama >= 50 and ortalama < 60:
        harf_notu = "FD"
    else:
        harf_notu = "FF"

    return ad_soyad + " " + harf_notu + "\n"

def ortalamalari_oku():
    with open("bolum-11/notlar.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(ortalama_hesapla(satir))

def notlari_gir():
    ad = input("Ad: ")
    soyad = input("Soyad: ")
    not1 = input("Not 1: ")
    not2 = input("Not 2: ")
    not3 = input("Not 3: ")

    with open("bolum-11/notlar.txt", "a", encoding="utf-8") as file:
        file.write(ad + " " + soyad + ":" + not1 + "," + not2 + "," + not3 + "\n")

def notlari_kaydet():
    with open("bolum-11/notlar.txt", "r", encoding="utf-8") as file:
        liste = []
        for i in file:
            liste.append(ortalama_hesapla(i))

        with open("bolum-11/sonuclar.txt", "w", encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)

while True:
    islem = input("1- Ortalamaları Oku\n2- Notları Gir\n3- Notları Kaydet\n4- Çıkış\nSeçiminiz: ")

    if islem == "1":
        print("Notlar ve Ortalamalar:")
        ortalamalari_oku()
    elif islem == "2":
        print("Notları Giriniz:")
        notlari_gir()
    elif islem == "3":
        print("Notlar kaydedildi.")
        notlari_kaydet()
    elif islem == "4":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz işlem. Lütfen tekrar deneyin.")