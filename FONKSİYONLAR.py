#fonksiyonlar
"""
def topla(x,y):
    return x+y
print(topla(10,20))
"""
#lambda fonk. tek satırlık işlemler için kullanılır
"""
topla=lambda x,y:x+y
print(topla(30,20))
"""
#map fonksiyonu:bir grup veriye fonksiyonunun değerini objekt şekilde döndürür
#map(fonsiyonadı,liste)
"""
def kare(x):
    return x*x
sayilar=range(1,9)
map(kare,sayilar)
print(list(map(kare,sayilar)))

"""
#filter fonksiyonu:
#1 den 14e kadar olan tek sayıları filter komutu ile yazdıralım
"""
def teksayi(x):
    return x%2==1
sayilar=range(1,15)
print(list(filter(teksayi,sayilar)))

"""
 #fizz buzz oyunu
"""
def fizzbuzz():
    for i in range(1,101):
        if i%15==0:
            print("fizzbuzz",end=',')
        elif i%3==0:
            print("fizz",end=',')
        elif i%5==0:
            print("buzz",end=',')
        else:
            print(i,end=',')
fizzbuzz() 
"""

#string fonksiyonları
#replace() yer değiştirme
"""
str="python güçlü bir programlama dilidir"
print(str.replace("p","P"))
"""

#metin içinde elemann silme

"""
str="eleman"
print(str.replace("e",""))
print(str.replace("e","",1))
print(str.replace("e","",2)) #iki yerden de silme
"""
#küyük harfle yazdırma
"""
str="YÖNETİMBİLİŞİM"
print(str.lower())
"""

#büyük harf yapma
"""
str="nurcan"
print(str.upper())
"""
#capitalize() baş harf büyük yapma
"""
str="PYTHON Programlama"
print(str.capitalize())
Python programlama
"""
#title() fonksiyonu ilk harfleri büyük yapar

"""
str="python programlama dili"
print(str.title())
"""

#swapcase() büyük harfleri küçük , küçük harfleri büyük yapar
"""
str="HasAN"
print(str.swapcase())
"""

#strip() string ifadenin hem başındaki hem sonundaki gereksiz ifadeleri temizler
"""
str="  merhaba"
print(str.strip())
"""

#lstrip ve rstrip
"""
print(str.strip("a")) #üsttekiyle bağlantılı
""""

#startswith ve #endswith

#LİSTELER


