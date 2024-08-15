#ATM Sistemi Tasarımı
#işlemler:
#1. Hesap ekleme, silme, güncelleme, listeleme, ek hesap ekleme
#2. Bakiye Sorgulama
#3. Para Yatırma
#4. Para Çekme

#CLASS
class ATMSystem:

    #CONTROL FUNCTIONS
    def __init__(self):
        self.accountDict = {}
    
    def validate_account_number(self, account_number):
        if account_number.isdigit():
            return True
        return False
    
    def validate_balance(self, balance):
        if balance >=0:
            return True
        return False
    
    def validate_amount(self, amount):
        if amount >=0:
            return True
        return False

    #FUNCTIONS
    def check_exit(self):
        answer = input("Başka işlem yapmak istiyor musunuz? (E/H)")
        if answer.upper()=="E":
            return 'continue'
        else:
            print("Cikis yapiliyor...")
            return 'break'
        
    ##process=1
    def addAccount(self, account_number, name, balance):
        if self.validate_account_number(account_number) and self.validate_balance(balance):
            if account_number not in self.accountDict:
                self.accountDict[account_number] = []
            self.accountDict[account_number].append({'name': name, 'balance': balance})
            return "Hesap ekleme başarılı."
        return "Hesap numarası veya bakiye hatalı."

    ##process=2
    def deleteAccount(self, account_number, name):
        if self.validate_account_number(account_number):
            if account_number in self.accountDict:
                self.accountDict[account_number] = [acc for acc in self.accountDict[account_number] if acc['name'] != name]
                if not self.accountDict[account_number]:
                    del self.accountDict[account_number]
                else:
                    print("Hesap numarası altında başka hesaplar bulunmaktadır.")
                return "Hesap silindi."
            return "Hesap bulunamadı."
        return "Hesap numarası hatalı."

    ##process=3
    def updateAccount(self, account_number, name, new_name, new_balance):
        if self.validate_account_number(account_number) and self.validate_balance(new_balance):
            if account_number in self.accountDict:
                for account in self.accountDict[account_number]:
                    if account['name'] == name:
                        account['name'] = new_name
                        account['balance'] = new_balance
                        return "Hesap güncellendi."
            return "Hesap bulunamadı."
        return "Hesap numarası veya girilen bakiye hatalı."

    ##process=4
    def listAccounts(self, account_number):
        if self.validate_account_number(account_number):
            if account_number in self.accountDict:
                print(f"Hesap Numarası: {account_number}")
                for account in self.accountDict[account_number]:
                    print(f"\tİsim: {account['name']}, Bakiye: {account['balance']}")
                return "Hesaplar listelendi."
            return "Hesap bulunamadı."
        return "Hesap numarası hatalı."


    ##process=5
    def addExtraAccount(self, account_number, name, balance):
        if self.validate_account_number(account_number) and self.validate_balance(balance):
            if account_number in self.accountDict:
                if any(acc['name']== name for acc in self.accountDict[account_number]):
                    return "Bu isimde bir hesap zaten bulunmaktadır."
                
                self.accountDict[account_number].append({'name': name, 'balance': balance})
                return "Ek hesap eklendi."
            else:
                return "Hesap numarası bulunamadı."
        return "Hesap numarası veya bakiye hatalı."


    ##process=6
    def checkBalance(self, account_number, name):
        if self.validate_account_number(account_number):
            if account_number in self.accountDict:
                for account in self.accountDict[account_number]:
                    if account['name'] == name:
                        return f"İsim: {name}, Bakiye: {account['balance']}"
                return "Hesap ismi bulunamadı."
            else:
                return "Hesap numarası bulunamadı."
        return "Hesap numarası hatalı."


    ##process=7
    def depositMoney(self, account_number, name, amount):
        if self.validate_account_number(account_number) and self.validate_amount(amount):
            if account_number in self.accountDict:
                for account in self.accountDict[account_number]:
                    if account['name'] == name:
                        account['balance'] += amount
                        return f"{amount} TL yatırıldı. Yeni Bakiye: {account['balance']}"
                return "Hesap ismi bulunamadı."
            else:
                return "Hesap numarası bulunamadı."
        return "Hesap numarası veya girilen tutar hatalı."


    ##process=8
    def withdrawMoney(self, account_number, name, amount):
        if self.validate_account_number(account_number) and self.validate_amount(amount):
            if account_number in self.accountDict:
                for account in self.accountDict[account_number]:
                    if account['name'] == name:
                        if account['balance'] >= amount:
                            account['balance'] -= amount
                            return f"{amount} TL çekildi. Yeni Bakiye: {account['balance']}"
                        else:
                            return "Yetersiz bakiye!"
                return "Hesap ismi bulunamadı."
            else:
                return "Hesap numarası bulunamadı."
        return "Hesap numarası veya girilen tutar hatalı."

#SYSTEM

def systemATM():
    atm=ATMSystem()
    print("ATM Sistemine Hoşgeldiniz.")

    while True:
        process = input("Yapmak istediğiniz işlem numarasını seçiniz:\n"
                        " 1. Hesap Ekleme\n"
                        " 2. Hesap Silme\n"
                        " 3. Hesap Güncelleme\n"
                        " 4. Hesap Listeleme\n"
                        " 5. Ek Hesap Ekleme\n"
                        " 6. Bakiye Sorgulama\n"
                        " 7. Para Yatırma\n"
                        " 8. Para Çekme\n"
                        " 9. Çıkış\n Seçiminiz:")
        
        if process in ['1', '2', '3', '4', '5', '6', '7', '8']:
            account_number = input("Hesap numarasını giriniz: ")
            name= None
            if process in ['1', '2', '3', '5', '6', '7', '8']:
                name = input("Hesap adını giriniz: ")

        if process=="1":
            balance = int(input("Hesap bakiyesini giriniz: "))
            print(atm.addAccount( account_number, name, balance))

        elif process=="2":
            print(atm.deleteAccount( account_number, name))

        elif process == "3":
            new_name = input("Yeni hesap ismini giriniz: ")
            new_balance = int(input("Yeni hesap bakiyesini giriniz: "))
            print(atm.updateAccount( account_number, name, new_name, new_balance))

        elif process=="4":
            print(atm.listAccounts( account_number))
            

        elif process=="5":
            balance = int(input("Ek hesap bakiyesini giriniz: "))
            print(atm.addExtraAccount( account_number, name, balance))
            
            

        elif process=="6":
            print(atm.checkBalance( account_number, name))
            

        elif process=="7":
            amount = int(input("Yatırmak istediğiniz tutarı giriniz: "))
            print(atm.depositMoney( account_number, name, amount))
            

            
        elif process=="8":
            amount = int(input("Çekmek istediğiniz tutarı giriniz: "))
            print(atm.withdrawMoney( account_number, name, amount))
            

        elif process=="9":
            print("Çıkış yapılıyor...")
            break
        
        else:
            print("Geçersiz işlem.")

        if atm.check_exit() == 'break':
            break 


#SYSTEM
systemATM()
