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

# content1 = file.read()
# print("içerik1: ", content1)

# file = open("bolum-11/newfile.txt", "r", encoding="utf-8")
# content2 = file.read()
# print("içerik2: ", content2)

content = file.read(5)  # 5 karakter oku
content = file.read(3)  # 3 karakter oku
content = file.read(3)  # 3 karakter oku

print(content)

file.close()