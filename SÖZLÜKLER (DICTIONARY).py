#SÖZLÜKLER (DICTIONARY)

#SÖZLÜK ELEMANLARINA ERİŞİM
#İngilizce-Türkçe sözlük tanımla
sozluk={"apple":"elma", "computer":"bilgisayar","book":"kitap","school":"okul"}
print(sozluk["computer"])  # çağırmak için anahtar sözcük kullanılır
<<<bilgisayar

#GET(KEY) KOMUTU
#get() komutu parantez içerisine yazılan anahtara ait değeri bulmamızı sağlar.
#Ancak anahtar yoksa Keyerror üretmez. none sonucu üretir

sozluk={"apple":"elma", "computer":"bilgisayar","book":"kitap","school":"okul"}
print(sozluk.get("computer"))
<<<bilgisayar
#örnek:
kelime=input("Bir kelime girin :")
sozluk ={"Computer":"Bilgisayar",
         "Driver":"Sürücü",
         "Memory":"Hafıza",
         "Output":"Çıktı",
         "Software":"Yazılım",
         "Printer":"Yazıcı"}
print(sozluk.get(kelime,"Aradığınız kelime Sözlük içinde bulunmamaktadır"))
<<<Bir kelime girin :Software
<<<Yazılım
<<<Bir kelime girin :Book
<<<Aradığınız kelime Sözlük içinde bulunmamaktadır

#SÖZLÜĞE ELEMAN EKLEME
#Var olan sözlüğe yeni eleman ekleme
sozluk["rose"]="gül"
print(sozluk)


#SÖZLÜK ELEMANLARINI DÜZENLEME
#değeri değiştirilecek olan eleman bulunup, yeni değeri yazılır
sozluk={"apple":"elma","computer":"bilgisayar","book":"kitap","pen":"kalem"}
sozluk["pen"]="Dolma Kalem"
print(sozluk)


#SÖZLÜK ELEMANLARINI SİLME
#sozluk.pop("anahtar sözlük")
sozluk={"apple":"elma","computer":"bilgisayar","book":"kitap","pen":"kalem"}
sozluk.pop("pen")
print(sozluk)


SÖZLÜK TEMİZLEME
sozluk2={"apple":"elma","computer":"bilgisayar","book":"kitap","pen":"kalem"}
sozluk2.clear()
print(sozluk2)
#clear() komutunun çalışmasının ardından sözlük içindeki elemanlar
#temizlenir, ekrana boş sözlük yazılır.



#SÖZLÜK ELEMANLARINI LİSTELEME
sozluk={"apple":"elma","computer":"bilgisayar","book":"kitap","tea":"cay","coffee":"kahve"}
for k in sozluk:
    print("ingilizcesi:",k," Türkçe:",sozluk[k])


    
#İTEMS()
#items() komutu,bir sözcüğün içerisinde hem anahtar hem de değerlere aynı anda
#erişmemizi sağlar.

sozluk={"apple":"elma","computer":"bilgisayar","book":"kitap","tea":"cay","coffee":"kahve"}
print(sozluk.items())
<<<
dict_items([('apple', 'elma'), ('computer', 'bilgisayar'), ('book', 'kitap'), ('tea', 'cay'), ('coffee', 'kahve')])
>>> 

#item() komutu for dongusu ile birlikte şu şekilde kullanılır
sozluk2={"apple":"elma","computer":"bilgisayar","book":"kitap","pen":"kalem"}
for anahtar, deger in sozluk2.items():
    print("Anahtar:",anahtar,"Değer:",deger)
<<<    
Anahtar: apple Değer: elma
Anahtar: computer Değer: bilgisayar
Anahtar: book Değer: kitap
Anahtar: pen Değer: kalem
>>> 

#SÖZLÜK ANAHTAR VE DEĞERLERİNİN LİSTESİ
#Sözlüğe ait anahtar ve değerleri ayrı ayrı almak için keys() and values()
#KEYS()
sozluk2={"apple":"elma","computer":"bilgisayar","book":"kitap","pen":"kalem"}
for k in sozluk2.keys():
    print(k)
for k in sozluk2.values():
    print(k)
<<<
apple
computer
book
pen
elma
bilgisayar
kitap
kalem
<<<


#SÖZLÜK ELEMAN SAYISINI BULMA
sozluk={"apple":"elma","computer":"bilgisayar","book":"kitap","pen":"kalem"}
print(len(sozluk))

#ANAHTAR VARLIĞINI KONTROL ETME
sozluk3={"apple":"elma","computer":"bilgisayar","book":"kitap","pen":"kalem"}
print("apple" in sozluk3) # sözluk3 te apple var mı?
print("orange" not in sozluk3)


#SÖZLÜK KOPYALAMA
    
havadurumu={"Ankara":"bulutlu",
            "İstanbul":"yagmurlu",
            "İzmir":"günesli"}
tahmin=havadurumu
print(id(tahmin))
print(id(havadurumu))

havadurumu["Antalya"]="günesli"
print(tahmin)

#copy():bir sözlüğün içindeki elemanların kopyasını oluşturmak için
tahmin2=havadurumu.copy()
print(tahmin2)

print(id(havadurumu))
print(id(tahmin2))

#SÖZLÜK GÜNCELLEME
#update()
urun={"kalem":2,"defter":5,"makas":4}
yeni={"kalem":3,"defter":7,"makas":5,"boya":10}
urun.update(yeni)
print(urun)





















