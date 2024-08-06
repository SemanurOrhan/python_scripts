print("Ders Geçme Notu Hesaplayan Programa Hoşgeldiniz.")

minAverage= float(input("Dersi geçmeniz için gerekli en düşük ortalama notunu giriniz:"))
average=0
while True:
    mtNumber= input("Kaç adet vizeniz var? (1/2): ")
    if mtNumber!="1" and mtNumber!="2":
        print("Hatalı vize sayısı girdiniz. Lütfen tekrar deneyiniz.")
        continue
    if mtNumber=="1":
        while True:
            mRate= float(input("Vize notunun etki yüzdesini giriniz: "))/100
            fRate= float(input("Final notunun etki yüzdesini giriniz: "))/100
            rate= mRate+fRate
        
            if rate!=1:
                print("Hata: Vize ve final yüzdelerinin toplamı 100 olmalıdır.\nLütfen tekrar deneyiniz.")
                continue
            else:
                midterm_1= float(input("Vize notunuzu giriniz: "))
                final= float(input("Final notunuzu giriniz: "))
                average= midterm_1*mRate + final*fRate
                print("Ortalamanız: ", average)
            break
    elif mtNumber=="2":
        while True:
            mRate= float(input("Vize notunun etki yüzdesini giriniz: "))/200
            fRate= float(input("Final notunun etki yüzdesini giriniz: "))/100
            rate= (mRate*2)+fRate
        
            if rate!=1:
                print("Hata: Vize ve final yüzdelerinin toplamı 100 olmalıdır.\nLütfen tekrar deneyiniz.")
                continue
            else:
                midterm_1= float(input("1. Vize Notunuzu Giriniz: "))
                midterm_2= float(input("2. Vize Notunuzu Giriniz: "))
                final= float(input("Final Notunuzu Giriniz: "))
                average= midterm_1*mRate + midterm_2*mRate + final*fRate
                print("Ortalamanız: ", average)
            break
    if average>=minAverage:
        print("Tebrikler, dersi geçtiniz.")
    else:
        print("Üzgünüm, dersi geçemediniz.")
    
    cp=input("Not hesaplamaya devam etmek istiyor musunuz? (E/H): ")
    if cp.upper()=="E":
        continue
    break