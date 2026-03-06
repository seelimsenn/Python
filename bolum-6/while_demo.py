# sayilar = [1, 3, 5, 7, 9, 12, 19, 21]
# i = 0
# while i < len(sayilar):
#     print(sayilar[i])
#     i += 1


# baslangic = int(input("Başlangıç değeri: "))
# bitis = int(input("Bitiş değeri: "))

# i = baslangic

# while i <= bitis:
#     if (i % 2 == 1):
#         print(i)
#     i += 1


# i = 100
# while i > 0:
#     print(i)
#     i -= 1


# numbers = []

# i = 0
# while i < 5:
#     sayi = int(input("Sayı: "))
#     numbers.append(sayi)
#     i += 1
# numbers.sort()
# print("Girilen sayılar: ", numbers)


urunler = []

adet = int(input("Kaç adet ürün eklemek istiyorsunuz?"))

i = 0
while i < adet:
    name = input("Ürün adı: ")
    price = float(input("Ürün fiyatı: "))
    urunler.append({"name": name, "price": price})
    i += 1

for urun in urunler:
    print(f"Ürün adı: {urun['name']}, Ürün fiyatı: {urun['price']}")