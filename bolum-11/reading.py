# "r"  -> okuma (read, varsayılan)
# try:
#     file = open("bolum-11/newfile.txt", "r", encoding="utf-8")
#     print(file)
# except FileNotFoundError:
#     print("Dosya bulunamadı.")
# finally:
#     file.close()

file = open("bolum-11/newfile.txt", "r", encoding="utf-8")

# for i in file:
#     print(i, end="")
# file.close()

# ***read() fonksiyonu***

# content1 = file.read()
# print("içerik1: ", content1)

# file = open("bolum-11/newfile.txt", "r", encoding="utf-8")
# content2 = file.read()
# print("içerik2: ", content2)

# content = file.read(5)  # 5 karakter oku
# content = file.read(3)  # 3 karakter oku
# content = file.read(3)  # 3 karakter oku

# print(content)

# ***readline() fonksiyonu***

# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline())
# print(file.readline())
# print(file.readline())

# ***readlines() fonksiyonu***

liste = file.readlines()
print(liste)
print(liste[0])
print(liste[1])
print(liste[2])

file.close()