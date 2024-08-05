print("Beden Kitle İndeksinizi Hesaplayan Programa Hoşgeldiniz.")
boy= float(input("Boyunuzu cm cinsinden giriniz: "))
kilo= float(input("Kilonuzu giriniz: "))
bki= kilo /boy**2   
print("Beden Kitle İndeksiniz: ", bki)
if bki<18.5:
    print("Zayıf")
elif bki>=18.5 and bki<25:
    print("Normal")
elif bki>=25 and bki<30:
    print("Fazla Kilolu")
else:
    print("Obez")
