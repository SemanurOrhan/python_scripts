#ATM Sistemi Tasarımı
#işlemler:
#1. Hesap ekleme, silme, güncelleme, listeleme, ek hesap ekleme
#2. Bakiye Sorgulama
#3. Para Yatırma
#4. Para Çekme

#FUNCTIONS
def check_exit():
    answer = input("Başka hesap eklemek istiyor musunuz? (E/H)")
    if answer.upper()=="E":
        return 'continue'
    else:
        print("Cikis yapiliyor...")
        return 'break'
##process=1
def addAccount(accountDict, account_number, name, balance):
    if account_number not in accountDict:
        accountDict[account_number] = []
    accountDict[account_number].append({'name': name, 'balance': balance})
    return "Hesap eklendi."

##process=2
def deleteAccount(accountDict, account_number, name):
    if account_number in accountDict:
        accountDict[account_number] = [acc for acc in accountDict[account_number] if acc['name'] != name]
        if not accountDict[account_number]:  # Eğer hesap numarası altında başka hesap kalmadıysa
            del accountDict[account_number]  # Hesap numarasını tamamen kaldır
        else:
            print("Hesap numarası altında başka hesaplar bulunmaktadır.")
        return "Hesap silindi."
    return "Hesap bulunamadı."

##process=3
def updateAccount(accountDict, account_number, old_name, new_name, new_balance):
    if account_number in accountDict:
        for account in accountDict[account_number]:
            if account['name'] == old_name:
                account['name'] = new_name
                account['balance'] = new_balance
                return "Hesap güncellendi."
    return "Hesap bulunamadı."

##process=4
def listAccounts(accountDict):
    for account_number, accounts in accountDict.items():
        print(f"Hesap Numarası: {account_number}")
        for account in accounts:
            print(f"\tİsim: {account['name']}, Bakiye: {account['balance']}")
    return "Hesaplar listelendi."


##process=5
def addExtraAccount(accountDict, account_number, name, balance):
    if account_number in accountDict:
        accountDict[account_number].append({'name': name, 'balance': balance})
        return "Ek hesap eklendi."
    else:
        return "Hesap numarası bulunamadı."


##process=6
def checkBalance(accountDict, account_number, name):
    if account_number in accountDict:
        for account in accountDict[account_number]:
            if account['name'] == name:
                return f"İsim: {name}, Bakiye: {account['balance']}"
            else:
                print("Hesap bulunamadı.")
    else:
        print("Hesap bulunamadı")
    return "Hesap bulunamadı."


##process=7
def depositMoney(accountDict, account_number, name, amount):
    if account_number in accountDict:
        for account in accountDict[account_number]:
            if account['name'] == name:
                account['balance'] += amount
                return f"{amount} TL yatırıldı. Yeni Bakiye: {account['balance']}"
            else:
                print("Hesap bulunamadı.")
    else: 
        print("Hesap bulunamadı.")
    return "Hesap bulunamadı."


##process=8
def withdrawMoney(accountDict, account_number, name, amount):
    if account_number in accountDict:
        for account in accountDict[account_number]:
            if account['name'] == name:
                if account['balance'] >= amount:
                    account['balance'] -= amount
                    return f"{amount} TL çekildi. Yeni Bakiye: {account['balance']}"
                else:
                    return "Yetersiz bakiye!"
            else: 
                print("Hesap bulunamadı.")
    else: 
        print("Hesap bulunamadı.")
    return "Hesap bulunamadı."



#MAIN
accountDict = {}




#SYSTEM

def systemATM():
    while True:
        process = input("Yapmak istediğiniz işlem numarasını seçiniz:\n 1. Hesap Ekleme\n 2. Hesap Silme\n 3. Hesap Güncelleme\n 4. Hesap Listeleme\n 5. Ek Hesap Ekleme\n 6. Bakiye Sorgulama\n 7. Para Yatırma\n 8. Para Çekme\n 9. Çıkış")

        if process=="1":
            account_number = input("Hesap numarasını giriniz: ")
            name = input("Hesap adını giriniz: ")
            balance = int(input("Hesap bakiyesini giriniz: "))
            print(addAccount(accountDict, account_number, name, balance))

        elif process=="2":
            account_number = input("Silmek istediğiniz hesap numarasını giriniz: ")
            name = input("Silmek istediğiniz hesap ismini giriniz: ")
        
            if account_number in accountDict:
                print(deleteAccount(accountDict, account_number, name))
            else:
                print("Hesap bulunamadı.")

        elif process == "3":
            account_number = input("Hesap numarasını giriniz: ")
            old_name = input("Güncellemek istediğiniz hesap ismini giriniz: ")

            if account_number in accountDict:
                for account in accountDict[account_number]:
                    if account['name'] == old_name:
                        new_name = input("Yeni hesap adını giriniz: ")
                        new_balance = int(input("Yeni hesap bakiyesini giriniz: "))
                        print(updateAccount(accountDict, account_number, old_name, new_name, new_balance))
                        break
                else:
                    print("Hesap bulunamadı.")
            else:
                print("Hesap bulunamadı.")



        elif process=="4":
            account_number = input("Hesap numarasını giriniz: ")
            if account_number in accountDict:
                print(listAccounts(accountDict[account_number]))
            else:
                print("İlgili hesap numarasına ait kayıtlı hesap bulunmamaktadır.")

        elif process=="5":
            account['account_number'] = input("Eklemek istediğiniz hesap numarasını giriniz: ")
            if account['account_number'] in accountDict:
                account['name'] = input("Eklemek istediğiniz hesap ismini giriniz: ")
                if account['name'] in accountDict[account['name']]:
                    print("Bu isimde bir hesap zaten bulunmaktadır.")
                    return 'continue'
                else :
                    account[name]=account['name']
                    account['balance'] = int(input("Eklemek istediğiniz hesap bakiyesini giriniz: "))
                    print(addExtraAccount(accountDict, account_number, name, balance))
                    return check_exit()
            else:
                print("Hesap numarası bulunamadı.")
                return 'continue'

        elif process=="6":
            account_number = input("Bakiyesini sorgulamak istediğiniz hesap numarasını giriniz: ")
            name = input("Bakiyesini sorgulamak istediğiniz hesap ismini giriniz: ")
            if account_number and name in accountDict and accountDict[account_number[name]]:
                print(checkBalance(accountDict, account_number, name))
            else:
                print("Hesap bulunamadı.")

        elif process=="7":
            account_number = input("Para yatırmak istediğiniz hesap numarasını giriniz: ")
            name = input("Para yatırmak istediğiniz hesap ismini giriniz: ")
            amount = int(input("Yatırmak istediğiniz tutarı giriniz: "))
            if account_number and name in accountDict and accountDict[account_number[name]]:
                print(depositMoney(accountDict, account_number, name, amount))
            else:
                print("Hesap bulunamadı.")


            
        elif process=="8":
            account_number = input("Para çekmek istediğiniz hesap numarasını giriniz: ")
            name = input("Para çekmek istediğiniz hesap ismini giriniz: ")
            amount = int(input("Çekmek istediğiniz tutarı giriniz: "))
            if account_number and name in accountDict and accountDict[account_number[name]]:
                print(withdrawMoney(accountDict, account_number, name, amount))
            else:
                print("Hesap bulunamadı.")

        elif process=="9":
            return 'break'
        
        else:
            print("Geçersiz işlem.")

        if not check_exit() == 'continue':
            return 'break'




#SYSTEM

print("ATM Sistemine Hoşgeldiniz.")

while True:
    if systemATM() == 'break':
        break
