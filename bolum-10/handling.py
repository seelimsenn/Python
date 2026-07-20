# error handling => hata yönetimi

try:
    x = int(input("Bir sayı girin: "))
    y = int(input("Bir başka sayı girin: "))
    print(x/y)
# except ZeroDivisionError:
#     print("Sıfıra bölme hatası! Lütfen sıfırdan farklı bir sayı girin.")
# except ValueError:
#     print("Geçersiz giriş! Lütfen bir sayı girin.")
except (ZeroDivisionError, ValueError) as e:
    print("Yanlış bilgi girdiniz.")
    print(e)

while True:
    try:
        x = int(input("Bir sayı girin: "))
        y = int(input("Bir başka sayı girin: "))
        print(x/y)
    except Exception as ex:
        print("Yanlış bilgi girdiniz.", ex)
    else:
        break
    finally:
        print("try/except sonlandı.")
