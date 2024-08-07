import random
while True:
    entry = input("Sayi Tahmin Oyununa Hosgeldiniz. \n Oyundan cikmak icin 'Q' tusuna basiniz. \n Oyuna baslamak icin 'E' tusuna basiniz. \n Seciminiz: ")

    if entry.upper() == 'Q':
        print('Oyundan cikiyorsunuz...')
        break
    elif entry.upper() == 'E':
        while True:
            score= 100
            number = random.randint(1, 100)
            claim = int(input('Oyun basliyor...\n 1 ile 100 arasinda rastgele bir sayi seçildi.\n Tahmin icin kac deneme hakki istersiniz?'))
            scoreDown = int(100/claim)
            print(f'{claim} hakkiniz var. Tahminleriniz basliyor...')
            i = 0
            while i < claim:
                guess = int(input(f'{i+1}. tahmininizi giriniz: '))
                if guess == number:
                    print(f'Tebrikler, {i+1}. tahminde dogru bildiniz. Puaniniz: {score}')
                    break
                elif guess < number:
                    print('Daha buyuk bir sayi giriniz.')
                    score -= scoreDown
                else:
                    print('Daha kucuk bir sayi giriniz.')
                    score -= scoreDown
                i += 1
            if i == claim:
                print(f'Hakkiniz bitti. Tutulan sayi: {number}')
                break
            answer = input("Tekrar oynamak ister misiniz?(E/H)")
            if answer.upper() == 'H':
                print('Oyundan cikiliyor...')
                break
            else:
                continue
    else:
        continue
    