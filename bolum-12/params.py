def toplama(a, b):
    return a + b
def cikarma(a, b):
    return a - b
def carpma(a, b):
    return a * b
def bolme(a, b):
    if b == 0:
        return "Sıfıra bölme hatası"
    return a / b

def islem(f1, f2, f3, f4, islem_adi):
    if islem_adi == "toplama":
        print(f1(10, 5))  # Output: 15
    elif islem_adi == "cikarma":
        print(f2(10, 5))  # Output: 5
    elif islem_adi == "carpma":
        print(f3(10, 5))  # Output: 50
    elif islem_adi == "bolme":
        print(f4(10, 5))  # Output: 2.0
    else:
        print("Geçersiz işlem adı")

islem(toplama, cikarma, carpma, bolme, "toplama")
islem(toplama, cikarma, carpma, bolme, "cikarma")
islem(toplama, cikarma, carpma, bolme, "carpma")
islem(toplama, cikarma, carpma, bolme, "bolme")
islem(toplama, cikarma, carpma, bolme, "mod")  # Output: Geçersiz işlem adı