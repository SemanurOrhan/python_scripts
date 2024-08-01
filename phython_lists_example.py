# Description: Lists in Python arrays are used to store multiple values in one single variable.

# Examples of lists:

# 1) ”Bmw, Mercedes, Opel, Mazda” elemanlarına sahip bir liste oluşturunuz.
cars=["Bmw", "Mercedes", "Opel", "Mazda"]
print("1)", cars)

# Liste Kaç elemanlıdır ?
print("2)", len(cars))

# Listenin ilk ve son elemanı nedir ?
print("3)", "İlk elemani:",cars[0],"/ Son elemani:", cars[-1])

# Mazda değerini Toyota ile değiştirin.
for car in cars:
    if car=="Mazda":
        cars[cars.index(car)]="Toyota"  

print("4)", cars)

# Mercedes listenin bir elemanı mıdır ?
if cars.count("Mercedes")>0:
    print("5)", "Mercedes listede bir elemandir.")
else:
    print("5)Mercedes listede yoktur...")

# Listenin -2 indeksindeki değer nedir ?
print("6)",cars[-2])

# Listenin ilk 3 elemanını alın.
print("7)", cars[:3])

# Listenin son 2 elemanı yerine "Totoya" ve "Renault” değerlerini ekleyin.
cars[-1]= "Toyota"
cars[-2]="Renault"
print("8)", cars)

# Listenin üzerine "Audi” ve "Nissan” değerlerini ekleyin.
cars.append("Audi")
cars.append("Nissan")
print("9)", cars)

# Listenin son elemanını silin.
cars.pop()
# del cars[-1] şeklinde de yapılabilir
print("10)",cars)

# Liste elemanlarını tersten yazdırınız.
print("11)", cars[::-1])

# Aşağıdaki verileri bir liste içinde saklayınız.
    # studentA:Yiğit Bilgi 2010,(70, 70)
    # studentB:Sena Turan 1999,(80, 80, 70)
    # studentC:Ahmet Turan 1998,(80, 70, 90)

studentA=["Pepe",2010,(70, 60, 70)]
studentB=["Şila",1999,(80, 80, 70)]
studentC=["Bebe",1998,(80, 70, 90)]
students=[studentA,studentB,studentC]
print ("12)",students)

#Liste elemanlarını ekrana yazdırın.
for student in students:
    print("13)",student)

#Öğrencilerin not ortalamalarını yazdırın.
for student in students:
    print("14)",student[0],"ortalamasi:",sum(student[2])/len(student[2]))

#Öğrencilerden en yüksek ve en düşük notu alanı yazdırın.
for student in students:
    print("15)",student[0],"en yuksek notu:",max(student[2]),"/ en dusuk notu:",min(student[2]))

#Öğrencilerin isimlerini ve doğum yıllarını ekrana yazdırın.
for student in students:
    print("16)",student[0],student[1])



