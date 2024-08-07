#Examples

#example 1
sayilar = [1,3,5,7,9,12,19,21]
# 1- sayilar listesindeki hangi sayılar 3'ün katıdır ?
# 2- sayilar listesinde sayıların toplamı kaçtır ?
# 3- sayilar listesindeki tek sayıların karesini alınız.
print('1- sayilar listesindeki hangi sayılar 3\'ün katıdır ?')
for sayi in sayilar:
    if sayi % 3 == 0:
        print(sayi)
print('2- sayilar listesinde sayıların toplamı kaçtır ?')
toplam=0
for sayi in sayilar:
    toplam += sayi
print(toplam)
print('3- sayilar listesindeki tek sayıların karesini alınız.')
for sayi in sayilar:
    if sayi % 2 != 0:
        print(sayi**2)

#example 2
sahirler=["İstanbul", "Ankara", "İzmir", "Bursa", "Antalya", "Adana", "Trabzon", "Samsun", "Erzurum", "Konya", "Diyarbakır", "Gaziantep", "Mersin", "Kayseri", "Malatya", "Kahramanmaraş", "Şanlıurfa", "Aydın", "Balıkesir", "Muğla", "Kütahya", "Afyonkarahisar", "Edirne", "Tekirdağ", "Kırklareli", "Çanakkale", "Kocaeli", "Sakarya", "Düzce", "Zonguldak", "Bolu", "Karabük", "Kastamonu", "Sinop", "Sivas", "Tokat", "Amasya", "Ordu", "Giresun", "Rize", "Artvin", "Ardahan", "Kars", "Iğdır", "Yalova", "Bilecik", "Eskişehir", "Aksaray", "Nevşehir", "Niğde", "Kırşehir", "Karaman", "Osmaniye", "Hatay", "Kilis", "Şırnak", "Batman", "Bitlis", "Van", "Muş", "Hakkari", "Şırnak"]
# 4- Şehirlerden hangileri en fazla 5 karakterlidir ?
# 5- Şehirlerden hangileri 'a' harfi ile başlar ve 'e' harfi ile biter ?
# 6- Şehirlerden sondan 3. harfi 'a' olan şehirler hangileridir ?

print('4- Şehirlerden hangileri en fazla 5 karakterlidir ?')
for sehir in sahirler:
    if len(sehir)<=5:
        print(sehir)

print('5- Şehirlerden hangileri \'a\' harfi ile başlar ve \'a\' harfi ile biter ?')
for sehir in sahirler:
    if sehir[0].lower()=='a' and sehir[-1].lower()=='a':
        print(sehir)

print('6- Şehirlerden sondan 3. harfi \'a\' olan şehirler hangileridir ?')
for sehir in sahirler:
    if sehir[-3].lower()=='a':
        print(sehir)

#example 3
urunler=[
    {'name':'Samsung S6', 'price':'3000'},
    {'name':'Samsung S7', 'price':'4000'},
    {'name':'Samsung S8', 'price':'5000'},
    {'name':'Samsung S9', 'price':'6000'},
    {'name':'Samsung S10', 'price':'7000'}
]
# 7 - Ürünlerin fiyatları toplamı nedir ?
# 8 - Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz.
# 9 - Ürünlerin fiyat ortalaması nedir ?

print('7 - Ürünlerin fiyatları toplamı nedir ?')
toplam=0
for urun in urunler:
    toplam += int(urun['price'])
print(toplam)

print('8 - Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz.')
for urun in urunler:
    if int(urun['price'])<=5000:
        print(urun['name'])

print('9 - Ürünlerin fiyat ortalaması nedir ?')
toplam=0
for urun in urunler:
    toplam += int(urun['price'])
print(toplam/len(urunler))

#example 4
# 10 - Başlangıç ve bitişi kullanıcıdan alın ve bu aralıktaki tek sayıları ekrana yazdırın.
# 11 - 1-100 arasındaki sayıları azalan şekilde yazdırın.
# 12 - Kullanıcıdan alınan sayıya kadar olan sayıların toplamını gösterin.

print('10 - Başlangıç ve bitişi kullanıcıdan alın ve bu aralıktaki tek sayıları ekrana yazdırın.')  
baslangic = int(input('Başlangıç: '))
bitis = int(input('Bitiş: '))
for i in range(baslangic, bitis):
    if i%2!=0:
        print(i)

print('11 - 1-100 arasındaki sayıları azalan şekilde yazdırın.')
for i in range(100,0,-1):
    print(i)

print('12 - Kullanıcıdan alınan sayıya kadar olan sayıların toplamını gösterin.')
sayi = int(input('Sayı: '))
toplam=0
for i in range(sayi+1):
    toplam += i
print(toplam)

#example 5
# 13 - Kullanıcıdan alınan bir sayının mükemmel olup olmadığını bulun. Bir sayı eğer kendisi hariç bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır.

# 14 - Kullanıcıdan alınan 5 sayının küçükten büyüğe sıralanmış halini yazdırın.

# 15 - Kullanıcıdan alınan sınırsız ürün bilgisini urunler listesi içinde saklayınız. (name, price) Ürün sayısını kullanıcıya sorun. Ürünleri while ile bu listeleyin.

print("13 - Kullanıcıdan alınan bir sayının mükemmel olup olmadığını bulun. Bir sayı eğer kendisi hariç bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır.")
sayi = int(input('Sayı: '))
bolenler=[]
for i in range(1,sayi):
    if sayi%i==0:
        bolenler.append(i)
if sum(bolenler)==sayi:
    print('Mükemmel sayıdır.')
else:
    print('Mükemmel sayı değildir.')

print("14 - Kullanıcıdan alınan 5 sayının küçükten büyüğe sıralanmış halini yazdırın.")
sayilar=[]
for i in range(5):
    sayi = int(input('Sayı: '))
    sayilar.append(sayi)
sayilar.sort()
print(sayilar)

print("15 - Kullanıcıdan alınan sınırsız ürün bilgisini urunler listesi içinde saklayınız. (name, price) Ürün sayısını kullanıcıya sorun. Ürünleri while ile bu listeleyin.")
urunler=[]
adet = int(input('Kaç ürün eklemek istiyorsunuz ? '))
i=0
while i<adet:
    name = input('Ürün adı: ')
    price = input('Ürün fiyatı: ')
    urunler.append({
        'name':name,
        'price':price
    })
    i+=1
for urun in urunler:
    print(f'Ürün adı: {urun["name"]} - Ürün fiyatı: {urun["price"]}')


#example 6
#List Comprehension: Liste Üreteçleri
# 16 - 1-100 arasındaki sayıların 3'e bölünen sayılarını yazdırın.
# 17 - 1-100 arasındaki sayıların karesini alın ve karesi 100'den küçük olanları yazdırın.
# 18 - 1-100 arasındaki sayılardan sadece çift sayıları yazdırın.

print('16 - 1-100 arasındaki sayıların 3\'e bölünen sayılarını yazdırın.')
print([i for i in range(1,101) if i%3==0])

print('17 - 1-100 arasındaki sayıların karesini alın ve karesi 100\'den küçük olanları yazdırın.')
print([i**2 for i in range(1,101) if i**2<100])

print('18 - 1-100 arasındaki sayılardan sadece çift sayıları yazdırın.')
print([i for i in range(1,101) if i%2==0])
