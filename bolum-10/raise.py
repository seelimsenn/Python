# x = 10

# if x > 5:
#     raise Exception("x 5'ten büyük olamaz")

# def check_password(psw):
#     import re

#     if len(psw) < 8:
#         raise Exception("Parola en az 8 karakter olmalıdır")
#     elif not re.search("[a-z]", psw):
#         raise Exception("Parola küçük harf içermelidir")
#     elif not re.search("[A-Z]", psw):
#         raise Exception("Parola büyük harf içermelidir")
#     elif not re.search("[0-9]", psw):
#         raise Exception("Parola rakam içermelidir")
#     elif not re.search("[_$#]", psw):
#         raise Exception("Parola alpha numeric karakter içermelidir")
#     elif re.search("\s", psw):
#         raise Exception("Parola boşluk karakteri içermemelidir")
#     else:
#         print("Geçerli parola")
    
# password = "12345678aA_"

# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("Parola geçerli: else")
# finally:
#     print("Validation tamamlandı")

class Person:
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception("Name alanı 10 karakterden uzun olamaz")
        else:
            self.name = name
            self.year = year

p = Person("Aliii", 1999)