#function examples

#Kullanıcıdan kelime ve kaç kez tekrar edileceğini alıp fonksiyona gönderme ve sonucu ekrana basma

# def print_word(word, count):
#     for i in range(count):
#         print(word)
#     return "Kelime "+str(count)+" kez tekrar edildi."

# word=input("Tekrar edilecek kelimeyi giriniz: ")
# count=int(input("Kaç kez tekrar edileceğini giriniz: "))
# print(print_word(word, count))

#Kendine gönderilen sınırsız sayıdaki parametreleri bir listeye çeviren fonksiyon

# def convert_to_list(*args):
#     return args

# result= convert_to_list(input("Listeye çevirmek istediğiniz sayılar arasına boşluk ekleyerek giriniz: "))
# print(result)

#Gönderilen iki sayı arasındaki asal sayıları bulmak
def prNumbers(a,b):
    for i in range(2,b+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            if i>=a:
                print(i)
    return "Asal sayılar yazdırıldı."

a=int(input("İlk sayıyı giriniz: "))
b=int(input("İkinci sayıyı giriniz: "))
prNumbers(a,b)


#Gönderilen bir sayının tam bölenlerini bulan ve bunları liste şeklinde döndüren fonksiyon
def devisor(n):
    devisors=[]
    for i in range(1,n+1):
        if n%i==0:
            devisors.append(i)
    return devisors

n=int(input("Bir sayı giriniz: "))
print(devisor(n))
