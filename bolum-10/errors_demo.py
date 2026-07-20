liste = ["1","2","5a","10b","abc","10","50"]

# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue

# while True:
#     sayi = input("Bir sayı giriniz: ")
#     if sayi == "q":
#         print("Programdan çıkılıyor...")
#         break
#     try:
#         result = float(sayi)
#         print(f"Girilen sayı: {result}")
#         break
#     except ValueError:
#         print("Geçersiz bir sayı girdiniz.")
#         continue

# def checkPassword(parola):
#     turkce_karakterler = "şçöğüıŞÇÖĞÜİ"

#     for i in parola:
#         if i in turkce_karakterler:
#             raise TypeError("Parola türkçe karakter içeremez")
#     print("Parola geçerli")
# parola = input("Parola: ")
# try:
#     checkPassword(parola)
# except TypeError as err:
#     print(err)

def faktöriyel(x):
    if not isinstance(x, int):
        raise ValueError("Girdi tam sayı olmalıdır")
    if x < 0:
        raise ValueError("Negatif sayıların faktöriyeli hesaplanamaz")
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

for x in [5,10, 20, -3, "10a"]:
    try:
        y = faktöriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)
