# with open("bolum-11/newfile.txt", "r+", encoding="utf-8") as file:
#     file.seek(20)
#     file.write("deneme")

# with open("bolum-11/newfile.txt", "r+", encoding="utf-8") as file:
#     print(file.read())

# ***Sayfa sonunda güncelleme***

# with open("bolum-11/newfile.txt", "a", encoding="utf-8") as file:
#     file.write("\nEbrar Güven")

# with open("bolum-11/newfile.txt", "r", encoding="utf-8") as file:
#     print(file.read())

# ***Sayfa başında güncelleme***

# with open("bolum-11/newfile.txt", "r+", encoding="utf-8") as file:
#     content = file.read()
#     content = "Meliha Şen\n" + content
#     file.seek(0)
#     file.write(content)

# with open("bolum-11/newfile.txt", "r", encoding="utf-8") as file:
#     print(file.read())

# *** Sayfa ortasında güncelleme ***

with open("bolum-11/newfile.txt", "r+", encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1, "Meliha Şen\n")
    file.seek(0)
    file.writelines(list)

with open("bolum-11/newfile.txt", "r", encoding="utf-8") as file:
    print(file.read())