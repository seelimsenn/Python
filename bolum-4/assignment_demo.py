x, y, z = 2, 5 ,10

numbers = 1, 5, 7, 10, 6

a = int(input("1. Sayı: "))
b = int(input("2. Sayı: "))

result1 = (a * b) - (x+y+z)
print(result1)

result2 = y // x
print(result2)

toplam = x + y + z
result3 = toplam % 3
print(result3)

result4 = y ** x
print(result4)

numbers = 1, 5, 7, 10, 6
x, *y, z = numbers
result5 = z ** 3
print(result5)

numbers = 1, 5, 7, 10, 6
x, *y, z = numbers
result6 = y[0] + y[1] + y[2]
print(result6)