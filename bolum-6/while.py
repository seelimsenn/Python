#1-100 e kadar

# x = 1

# while (x <= 100):
#     if (x % 2 == 1):
#         print(f'sayı tek: {x}')
#     else:
#         print(f'sayı çift: {x}')
#     x += 1
# print("Döngü bitti")


name = '' #False
while (not name.strip()):
    name = input("Adınızı giriniz: ")
print(f'Merhaba {name}')