'''
ogrenciler={
    '59':{
        name:'Harry',
        surname:'Potter',
        grades:{'midterm': 70, 'final': 80, 'project': 85}
        phoneNumber:'55555555555'
    }
    '60':{
        name:'Ron',
        surname:'Wisley',
        grades:{'midterm': 70, 'final': 60, 'project': 75}
        phoneNumber:'55555555556'
    }
    '61':{
        name:'Hermione',
        surname:'Grenger',
        grades:{'midterm': 80, 'final': 70, 'project': 65}
        phoneNumber:'55555555557'
    }
}

1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.

2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.

'''

ogrenciler={}
while True:
    print('Öğrenci bilgilerini ekleyin: ')
    ogrenciNo= input('Öğrenci No: ')
    if ogrenciNo in ogrenciler:
        print('Bu numaraya sahip bir öğrenci zaten var. Lütfen başka bir numara girin.')
        continue

    name= input('Ad: ')
    surname= input('Soyad: ')
    grades= int(input('Midterm: ')), int( input('Final: ')), int(input('Proje: '))
    phoneNumber= input('Telefon Numarası: ')

    ogrenciler[ogrenciNo]={
        'name': name,
        'surname': surname,
        'grades': {'midterm': grades[0], 'final': grades[1], 'project': grades[2]},
        'phoneNumber': phoneNumber
    }

    adding= input('Başka öğrenci eklemek ister misiniz? (E/H): ')
    if adding.upper()=='E' :
        continue
    else:
        print ('Ekleme işlemi tamamlandı. Öğrenciler listeleniyor...')
        break

for ogrenciNo, ogrenciBilgileri in ogrenciler.items(): #items() metodu ile dictionary içindeki key ve value'ları aynı anda alabiliriz.
    print(f'\n    Öğrenci No: {ogrenciNo}')
    for key, value in ogrenciBilgileri.items():
        print(f'    {key}: {value}')
    print('***********************')

while True:
    search= input('Aradığınız öğrenci nosunu giriniz: ')
    if search in ogrenciler:
        print(f'{ogrenciler[search]["name"]} {ogrenciler[search]["surname"]} isimli öğrencinin notları:{ogrenciler[search]["grades"]}')
    else:
        print('Bu numaraya sahip bir öğrenci bulunamadı.')
        
    searchAgain= input('Başka bir öğrenci aramak ister misiniz? (E/H): ')

    if searchAgain.upper()=='E' :
        continue
    else:
        print('Öğrenci arama işlemi tamamlandı. İyi günler dileriz...')
        break