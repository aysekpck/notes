#HATA AYIKLAMA
"""
Mantık Hataları (Logical errors)

a=9
a**1/2
>>4.5
-----------------------------
Kod yazım Hataları (Syntex errors)
Mesela, Pythonda girinti uygulamasına uyulmadıında,
print deyiminde parantezlerin unutulmasında
-----------------------------
Çalışma Zamanı hataları (RuntimeErrors)
-İstisna(exception) kelimesi ile ifade edilir.
Programın çalışması sırasında beklenmeyen bir durum sonucu
oluşan hatalardır.
-Mesela; dosya okumada okunacak dosyanın olmaması
-istenen verilerin bir çıkış birimine gönderilememesi
-bölme isleminde paydanın sıfır olması

Bu durumda program hata verir
bu tip hatalara karşı alınan önelm, hata yakalamadır.
"""
"""
a=3
b=0
a/b
#ZeroDivisionError: division by zero
"""
"""
a=[]
print(a[2])
#IndexError: list index out of range
"""
"""
Pytonda hata ayıklama dört sözcük ile yapılır
-try
-except
-else
-finally
hata ayıklamanın özünü try-except sözcükleri oluşturur.
"""
#HATA YAKALAMA BLOĞU
"""
try:
{
#Hataya sebep olacak kod
}
except Exception1:
{
#Eğer Exception1 tipinde hata oluşursa yapılacak işlemler.
}
else:
#istenirse hata oluşmadığında yapılacak işlemler bu bloğa yazılır

finally:
{
# istenirse her ne olursa olsun çalışacak kod buraya yazılır.
}
"""
"""
#ÖRNEK. Girilen bir sayının karesini alan program yazın.
#kullanıcı sayı haricinde karakter girdiğinde ısrarla sayı girmesini isteyecektir
while True: #sonsuz döngü
    try:
        x=int(input("Bir sayı giriniz.."))
        print("x^2=",x*x)
        break # sonlandır
    except ValueError : #Değer hatası
        print("Bu bir sayı değil, sayı giriniz !!")
#Eğer sayı girmezse, ValueError hatası oluşur
"""
#Örnek. Programda oluşan tüm hatalar için aynı mesajı veren kod
try:
    x=int(input("x="))
    y=int(input("y="))
    print(x/y)
except:
    print("HATA OLUŞTU")
    #standart hata mesajıı
finally:
    print("Hatasız günler dilerim !")



    


    








        
















