maasAli = 5000
maasAhmet = 4000
vergi = 0.27

print (maasAli - (maasAli * vergi))
print (maasAhmet - (maasAhmet * vergi))

#Değişken tanımlama kuralları

#Rakam ile başlayamaz

number1 = 10
print(number1)

number1 = 20
print(number1)

number1 += 30
print(number1)

#Büyük harf küçük harf duyarlılığı

age = 20
AGE = 30

print(age)
print(AGE)

#Türkçe karakter kullanmayalım

yas = 20
_age = 20

x = 1 #int
y = 2.3 #float
name = 'Çınar' #string
isStudent = False #bool

# x, y, name, isStudent = (1, 2.3, "Çınar", False)

a = '10' 
b = '20'
print(a + b) #30 => 1020

firstName = "Sadık"
last_Name = " Turan"
print(firstName + last_Name) #Sadık Turan
