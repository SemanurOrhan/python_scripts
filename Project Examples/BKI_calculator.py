print("Beden Kitle İndeksinizi Hesaplayan Programa Hoşgeldiniz.")
boy= float(input("Boyunuzu cm cinsinden giriniz: "))/100
kilo= float(input("Kilonuzu giriniz: "))
bki= kilo /boy**2   
print("Beden Kitle İndeksiniz: {:.2f}".format(bki))
category= ""
if bki<18.5:
    category= "Zayıf"
elif bki>=18.5 and bki<25:
    category= "Normal"
elif bki>=25 and bki<30:
    category= "Fazla Kilolu"
else:
    category= "Obez"

print(f'{category} kategorisindesiniz.')
