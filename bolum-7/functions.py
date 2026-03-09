def sayHello(name = 'user'):
    return 'Hello ' + name

msg =sayHello('Çınar')
msg =sayHello('Ada')
print(msg)

def total(num1,num2):
    return num1 + num2

result = total(10,20)
result = total(15,20)
print(result)

def yasHesapla(dogumYili):
    return 2026 - dogumYili

ageCinar = yasHesapla(2017)
ageAda = yasHesapla(2010)
ageSena = yasHesapla(1999)
print(ageCinar, ageAda, ageSena)

def emekliligeKacYilKaldi(dogumYili, isim):

    '''
    DOCSTRİNG: Dogum yiliniza gore emekliliginize kac yil kaldi
    INPUT: Dogum Yili, Isim
    OUTPUT: Hesaplnan yil bilgisi
    '''

    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f'emekliliğinize {emeklilik} yıl kaldı.')
    else:
        print('Zaten emekli oldunuz.')

emekliligeKacYilKaldi(1983, 'Ali')
emekliligeKacYilKaldi(1950, 'Ahmet')
emekliligeKacYilKaldi(1974, 'Yağmur')

print(help(emekliligeKacYilKaldi))

list = [1,2,3]
print(help(list.append))