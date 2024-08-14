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

def addAccount(accountDict, account_number, name, balance):
    if account_number not in accountDict:
        accountDict[account_number] = []
    accountDict[account_number].append({'name': name, 'balance': balance})
    return "Hesap eklendi."

def deleteAccount(accountDict, account_number, name):
    if account_number in accountDict:
        accountDict[account_number] = [acc for acc in accountDict[account_number] if acc['name'] != name]
        if not accountDict[account_number]:  # Eğer hesap numarası altında başka hesap kalmadıysa
            del accountDict[account_number]  # Hesap numarasını tamamen kaldır
        return "Hesap silindi."
    return "Hesap bulunamadı."

def updateAccount(accountDict, account_number, old_name, new_name, new_balance):
    if account_number in accountDict:
        for account in accountDict[account_number]:
            if account['name'] == old_name:
                account['name'] = new_name
                account['balance'] = new_balance
                return "Hesap güncellendi."
    return "Hesap bulunamadı."

def listAccounts(accountDict):
    for account_number, accounts in accountDict.items():
        print(f"Hesap Numarası: {account_number}")
        for account in accounts:
            print(f"\tİsim: {account['name']}, Bakiye: {account['balance']}")
    return "Hesaplar listelendi."

def addExtraAccount(accountList, account):
    accountList.append(account)
    return "Ek hesap eklendi."

def checkBalance(accountDict, account_number, name):
    if account_number in accountDict:
        for account in accountDict[account_number]:
            if account['name'] == name:
                return f"İsim: {name}, Bakiye: {account['balance']}"
    return "Hesap bulunamadı."

def depositMoney(accountDict, account_number, name, amount):
    if account_number in accountDict:
        for account in accountDict[account_number]:
            if account['name'] == name:
                account['balance'] += amount
                return f"{amount} TL yatırıldı. Yeni Bakiye: {account['balance']}"
    return "Hesap bulunamadı."

def withdrawMoney(accountDict, account_number, name, amount):
    if account_number in accountDict:
        for account in accountDict[account_number]:
            if account['name'] == name:
                if account['balance'] >= amount:
                    account['balance'] -= amount
                    return f"{amount} TL çekildi. Yeni Bakiye: {account['balance']}"
                else:
                    return "Yetersiz bakiye!"
    return "Hesap bulunamadı."

#CLASSES
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Name: {self.name} Balance: {self.balance}"

#MAIN
accountDict = {}
# account1 = Account("Harry Potter", 1000)
# account2 = Account("Ron Weasley", 2000)
# account3 = Account("Hermione Granger", 3000)
# account4 = Account("Draco Malfoy", 4000)

# accountList = [account1, account2, account3, account4]


#SYSTEM

def systemATM():
    process = input("Yapmak istediğiniz işlem numarasını seçiniz:\n 1. Hesap Ekleme\n 2. Hesap Silme\n 3. Hesap Güncelleme\n 4. Hesap Listeleme\n 5. Ek Hesap Ekleme\n 6. Bakiye Sorgulama\n 7. Para Yatırma\n 8. Para Çekme\n 9. Çıkış")

    if process=="1" or process=="5":
        account_number = input("Hesap numarasını giriniz: ")
        name = input("Hesap adını giriniz: ")
        balance = int(input("Hesap bakiyesini giriniz: "))
        print(addAccount(accountDict, account_number, name, balance))

    elif process=="2":
        account_number = input("Silmek istediğiniz hesap numarasını giriniz: ")
        name = input("Silmek istediğiniz hesap ismini giriniz: ")
    
        if account:
            print(deleteAccount(accountDict, account_number, name))
        else:
            print("Hesap bulunamadı.")

    elif process=="3":
        name = input("Güncellemek istediğiniz hesap ismi giriniz: ")
        account_number = input("Hesap numarasını giriniz: ")
        old_account = next((acc for acc in accountDict if acc.name == name), None)
        if old_account:
            new_name = input("Yeni hesap adını giriniz: ")
            new_balance = int(input("Yeni hesap bakiyesini giriniz: "))
            print(updateAccount(old_account, new_name, new_balance))
        else:
            print("Hesap bulunamadı.")

    elif process=="4":
        print(listAccounts(accountDict))

    # elif process=="5":
    #     name= input("Ek hesap adını giriniz: ")
    #     balance= int(input("Ek hesap için başlangıç bakiyesini giriniz: "))
    #     account = Account(name, balance)
    #     print(addExtraAccount(accountList, account))

    elif process=="6":
        account_number = input("Bakiyesini sorgulamak istediğiniz hesap numarasını giriniz: ")
        name = input("Bakiyesini sorgulamak istediğiniz hesap ismini giriniz: ")
        account = next((acc for acc in accountDict if acc.name == name), None)
        if account:
            print(checkBalance(accountDict, account_number, name))
        else:
            print("Hesap bulunamadı.")

    elif process=="7":
        name = input("Para yatırmak istediğiniz hesap ismi giriniz: ")
        account = next((acc for acc in accountDict if acc.name == name), None)
        if account:
            print(depositMoney(account))
        else:
            print("Hesap bulunamadı.")

        
    elif process=="8":
        name = input("Para çekmek istediğiniz hesap ismi giriniz: ")
        account = next((acc for acc in accountList if acc.name == name), None)
        if account:
            print(withdrawMoney(account))
        else:
            print("Hesap bulunamadı.")

    elif process=="9":
        return 'break'
    
    else:
        print("Geçersiz işlem.")

    return check_exit()

#SYSTEM

print("ATM Sistemine Hoşgeldiniz.")

while True:
    if systemATM() == 'break':
        break
