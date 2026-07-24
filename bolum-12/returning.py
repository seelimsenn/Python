# def us_alma(number):
#     def inner(power):
#         return number ** power
#     return inner

# two = us_alma(2)
# three = us_alma(3)

# print(two(3))
# print(three(4))


# def yetki_sorgula(page):
#     def inner(role):
#         if role == "Admin":
#             return f"{role} yetkisi ile {page} sayfasına erişebilirsiniz."
#         else:
#             return f"{role} yetkisi ile {page} sayfasına erişemezsiniz."
#     return inner

# user1 = yetki_sorgula("Dashboard")
# print(user1("Admin"))  # Output: Admin yetkisi ile Dashboard sayfasına erişebilirsiniz.
# print(user1("User"))   # Output: User yetkisi ile Dashboard sayfasına erişemezsiniz.


def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    
    if islem_adi == "toplama":
        return toplam
    elif islem_adi == "carpma":
        return carpma
    
toplama = islem("toplama")
print(toplama(1, 2, 3, 4))  # Output: 10
carpma = islem("carpma")
print(carpma(1, 2, 3, 4, 5))    # Output: 120