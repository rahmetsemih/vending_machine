# encoding:utf-8
import random as r
import time

def urunHazırla():

    for i in range(1, 6):
        st = "-" * i + "%" + str(20 * i)

        print(st, end="\r")
        time.sleep(1)
bisküvi_adet = r.randint(0, 4)
maske_adet = r.randint(0, 4)
su_adet = r.randint(0, 4)
sakız_adet = r.randint(0, 4)

bisküvi = {
    "isim": "bisküvi",
    "adet": bisküvi_adet,
    "fiyat": 6
}
maske = {
    "isim": "maske",
    "adet": maske_adet,
    "fiyat": 1
}
su = {
    "isim": "su",
    "adet": su_adet,
    "fiyat": 1.5
}
sakız = {
    "isim": "sakız",
    "adet": sakız_adet,
    "fiyat": 0.5
}

otomat = {"bisküvi": bisküvi, "maske": maske, "su": su, "sakız": sakız}

secim = int(input("Merhabalar.. Otomata hoş geldiniz\nÜrün seçimi yapmak için 1'i tuşlayınız.\nAnlık olarak ne kadar ürün olduğunu görmek için 2'yi tuşlayınız.\nSeçiminizi tuşlayınız= "))

print("\n")
while secim == 1 or secim == 2:

    if secim == 2:

        if bisküvi_adet == 0:
            pass
        else:
            print(otomat["bisküvi"]["isim"] + " " + str(otomat["bisküvi"]["adet"]) + " " + "adet")
        if maske_adet == 0:
            pass
        else:
            print(otomat["maske"]["isim"] + " " + str(otomat["maske"]["adet"]) + " " + "adet")
        if su_adet == 0:
            pass
        else:
            print(otomat["su"]["isim"] + " " + str(otomat["su"]["adet"]) + " " + "adet")
        if sakız_adet == 0:
            pass
        else:
            print(otomat["sakız"]["isim"] + " " + str(otomat["sakız"]["adet"]) + " " + "adet\n\n")
        secim = secim - 1

        time.sleep(1)
    else:

        if (otomat["bisküvi"]["adet"]) > 0:
            print("bisküvi için 1 tuşuna basınız(6 TL)")
        else:
            pass
        if (otomat["maske"]["adet"]) > 0:
            print("maske için 2 tuşuna basınız(1 TL)")
        else:
            pass
        if (otomat["su"]["adet"]) > 0:
            print("su için 3 tuşuna basınız(1.5 TL)")
        else:
            pass
        if (otomat["sakız"]["adet"]) > 0:
            print("sakız için 4 tuşuna basınız(0.5 TL)\n")
        else:
            pass
        break
urun = input("Seçiminizi tuşlayınız=")
odemeAdımı = False
while True:
    if (urun == "1" and bisküvi_adet != 0) or (urun == "2" and maske_adet != 0) or (urun == "3" and su_adet != 0) or (
            urun == "4" and sakız_adet != 0) or (urun == "E"):
        if urun == "E":
            print("İŞLEM SONLANDI")
            break
        elif urun == "1":
            print("seçtiğiniz ürün:", otomat["bisküvi"]["isim"], "\nücreti=", otomat["bisküvi"]["fiyat"], "TL")
            urunfıyat = otomat["bisküvi"]["fiyat"]
            odemeAdımı = True
            break
        elif urun == "2":
            print("seçtiğiniz ürün:", otomat["maske"]["isim"], "\nücreti=", otomat["maske"]["fiyat"], "TL")
            urunfıyat = otomat["maske"]["fiyat"]
            odemeAdımı = True
            break
        elif urun == "3":
            print("seçtiğiniz ürün:", otomat["su"]["isim"], "\nücreti=", otomat["su"]["fiyat"], "TL")
            urunfıyat = otomat["su"]["fiyat"]
            odemeAdımı = True
            break
        else:
            print("seçtiğiniz ürün:", otomat["sakız"]["isim"], "\nücreti=", otomat["sakız"]["fiyat"], "TL")
            urunfıyat = otomat["sakız"]["fiyat"]
            odemeAdımı = True
            break
    else:
        print("Yanlış veya olmayan bir ürün seçtiniz. tekrar deneyiniz (veya işlemi sonlandırmak için E  / e yazınız)")
        urun = input("Seçiminizi tuşlayınız=")
        if urun in ["E", "e"]:

            print("işlem sonlandı")
            break
        elif urun == "1":
            continue
        elif urun == "2":
            continue
        elif urun == "3":
            continue
        elif urun == "4":
            continue
        else:
            print("hatalı giriş")
            continue
if odemeAdımı:
    guncelbakiye = 0
    isTest = True
    kabulTutar = [0.5, 1.0, 5.0, 10.0, 20.0]

    while isTest:

        girilentutar = float(input("Lütfen ödemeyi yapınız (Yalnızca 0.5 ,1,5,10,20TL geçerlidir..)="))
        if girilentutar not in kabulTutar:
            print("Güncel bakiyeniz=", guncelbakiye)
            print("Yetersiz veya yanlış ödeme.. Tekrar para atınız..")
            continue
        guncelbakiye += girilentutar
        if guncelbakiye < urunfıyat:
            print("Güncel bakiyeniz=", guncelbakiye)
            print("Yetersiz veya yanlış ödeme.. Tekrar para atınız..")
        else:
            isTest = False
            guncelbakiye -= urunfıyat
            print("Ürününüz hazırlanıyor …")
            urunHazırla()
            print("Sağlıklı günler dileriz :)")
            if guncelbakiye > 0:
                print("Para üstünüzü unutmayın.")
                print("Para üstü: " + str(guncelbakiye))
                print("Sağlıklı günler dileriz :)")
