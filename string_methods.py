# Description: String methods

#text karakter dizisinde kaç karakter bulunur?

text= "Python is a programming language that lets you work quickly and integrate systems more effectively."
x= len(text)
print(x)


#text karakter dizisini tersten yazdırın.

y= text[::-1]
print(y)


#string formatlama yöntemiyle metni istenen hale getirin: My name is Harry Potter. I am 34 years old. I was born on 03.09.2000.

name, surname, age, date_of_birth= "Harry", "Potter", 34, '03.09.2000'
print("My name is {} {}. I am {} years old. I was born on {}.".format(name, surname, age, date_of_birth))


#text metninde kaç tane a harfi bulunduğunu hesaplayan algoritmayı yazınız.

repeat=0
for i in range( len(text) ):
    if text[i] == "a":
        repeat+=1
print(repeat)        
###
print(text.count("a")) #bu şekilde de yapılabilir.

#text metnindeki boşluklara - yazdırın.

newText= text.replace(" ","-")
print(newText)




#' Hello World ' karakter dizisinin baş ve sonundaki boşluk karakterini siliniz.
message = ' Hello World '.strip()
print(message)


# " Harry Potter Zümrüdüanka Yoldaşlığı " karakter dizisindeki tüm h,r,t ve l karakterlerini siliniz.
msg=" Harry Potter Zumruduanka Yoldasligi "
msg1=msg.replace("h","").replace("r","").replace("t","").replace("l","")
print(msg1)

# "SICAK HAVALAR GECSE DE BEN HALEN YANIYORUM" karakter dizisindeki tüm karakterleri küçük karaktere çeviriniz.
msg2="SICAK HAVALAR GECSE DE BEN HALEN YANIYORUM".lower()
print(msg2)

# "hello world" karakter dizisindeki tüm karakterleri büyük karaktere çeviriniz.
msg3="hello world".upper()
print(msg3)

# "Python Programlama Dili" karakter dizisindeki kelimelerin baş harflerini büyük yapınız.
msg4="Python Programlama Dili".title()
print(msg4)

# "Python Programlama Dili" karakter dizisindeki kelimelerin son harflerini büyük yapınız.
msg5="Python Programlama Dili".swapcase()
print(msg5)

# "Python gozkapagina sahip degildir." karakter dizisindeki g karakterinin sayısını yazdırınız.
msg6="Python gozkapagina sahip degildir.".count("g")
print(msg6)#3
