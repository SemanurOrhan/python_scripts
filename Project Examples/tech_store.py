while True:
    name=input("Isminizi giriniz: ")
    telNo=input("Telefon numaranizi giriniz: ")
    eposta=input("Eposta adresinizi giriniz: ")
    adres=input("Adres bilginizi giriniz: ")
    password=input("Sifrenizi giriniz: ")

    if name=="Harry Potter" and telNo=="1234567890" and eposta=="hrrypttr@gmail.com" and adres=="London" and password=="123456":
        break
    else:
        print("Lütfen tekrar deneyin!! ")
        continue

print("Hoşgeldin "+name)

urunler=["mouse","keyboard","kulaklik","camera","speaker","changeAdapter","changeCable","powerbank","usbHub","usbFlashDisk","sdCard","ssdDisk","hddDisk","ram","monitor","printer","scanner","projector"]
fiyatlar=["150","200","100","250","300","50","20","300","150","100","50","500","400","300","600","700","800","900"]

print("Urunlerimiz: ")

for i in range(len(urunler)):    # urunler listesindeki eleman sayisi kadar doner ve her bir elemani ekrana yazdirir.
    print(urunler[i],":",fiyatlar[i])
toplam=0

while True:     # print fonksiyonu ile ekrana yazdirilan urunlerden secim yapilir ve secilen urunun fiyati toplam degiskenine eklenir.
    secilen=input("Almak istediginiz urunu seciniz: ")
    if secilen in urunler:      # secilen urunun urunler listesinde olup olmadigini kontrol eder.
        index=urunler.index(secilen)        # secilen urunun indexini bulur.
        toplam+=int(fiyatlar[index])            # secilen urunun fiyatini toplam degiskenine ekler.
        print(secilen,"urununu sepetinize eklediniz. ")
        devam=input("Alisverise devam etmek istiyor musunuz? (E/H): ")
        if devam.lower() =="h":
            print("Mağazadan çıkılıyor... Hoşçakalın... ")
            break
    else:
        print("Boyle bir urun bulunmamaktadir. ")

print("Toplam tutar: ",toplam)
print("Odeme islemleri basliyor... ")
print("Odeme islemleri basariyla gerceklesti. Tesekkurler... ")
print("Urunleriniz 3 gun icinde adresinize teslim edilecektir. ")
print("Iyi gunler dileriz... ")




