import random as rnd    #Burada random a artik rnd diyecegimizi belirtiyoruz.
#import asdfghjklşls as A  #Goruldugu gibi uzun degisken isimlerini istedigimiz gibi kisaltabiliyoruz.
print(rnd.randint(5,10))


Bolumler=["Bilgisayar","Elektronik","Makine","Ziraat","Yazılım"]

import random as rnd

def BolumAra(Bolumler):
    index=rnd.randint(0,len(Bolumler)-1)
    return Bolumler[index]

sonuc=BolumAra(Bolumler)
print(sonuc)

def CarpimT(sayi):
    sayiListesi=[1,2,3,4,5]
    sonucListesi=[]

    for carp in sayiListesi:
        sonucListesi.append(sayi*carp)
        return sonucListesi

sonuc=CarpimT(8)            #listede bize sadece 8 sayisini verir ilk return den sonra fonk.durur.           
print(list(sonuc))

def fonksiyon(sayi):
    liste=[2,3,4]

    for item in liste:
        yield sayi**item

result=fonksiyon(2)           #4,8,16 donderecek...
print(list(result))


def Hesaplama(sayi):
    yield sayi+2
    yield sayi-2
    yield sayi*2
    yield sayi/2

sonuc=Hesaplama(5)
print(list(sonuc))

def Hesaplama2(sayi):
    return sayi+2
    return sayi-2
    return sayi*2
    return sayi/2

sonuc2=Hesaplama2(8)
print(sonuc2)          #Sadece 10 sayisini donderecek..



