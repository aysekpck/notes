#Dosya işlemleri
#open(): open("dosya yolu", mod)
#dosya yolu, işlem ypacağım dosyanın bilgisayarımızdaki adresi
#örn. r"C:\Users\nurcan\Desktop\ornek.txt"
dosya=open(r"C:\Users\nurcan\Desktop\Hafta_11_YBS\ornek.txt",mode="r")
#readline(): satır olarak okur
print(dosya.readline())
print(dosya.readline())
dosya.close()
"""
ikinci parametre olan mode(mod),
dosyayı hangi yetki ile açacağımızı belirler.
"w" write:Eğer dosya yoksa oluşturur, aynı isimde dosya varsa
eskisini silerek üzerine yazılır, eski veriler kaybolur.

"a" append: Dosyayı veri ekleme modund açar.
Eğer dosya yoksa oluşturur, varsa da gönderilen veriler
dosyanının altına eklenir.

"r" read: Dosyayı vri okuma amaçlı açar.
Varolan veriler okunabilir, dosya yazma yapılamaz.

"""
# Dosya yolu yerine sadece dosya ismi yazılırsa,
#programın kayıtlı olduğu dizinde bir dosya oluşturulur."w"
dosya2=open("asya.txt",mode="w")
#Dosyaya veri yazma
dosya2.write("merhaba python")
dosya2.write("merhaba YBS")
dosya2.write("merhaba DOGUS")
dosya2.close()

dosya3=open("asya.txt",mode="w")
#Dosyaya veri yazma 
dosya3.write("merhaba python\n")
dosya3.write("merhaba YBS\n")
dosya3.write("merhaba DOGUS\n")
dosya3.close()

#DOSYA SONU VERİ EKLEME "a"
dosya1=open("asya.txt", mode="a")
dosya1.write("Dogus University")
dosya1.close()
#DOSYADAN VERİ OKUMA "r"
dosya=open("ornek.txt","r")
print(dosya.read())
dosya.close()
#Dosya içindeki herbir satırları
#bir liste üzerine okumak için
dosya=open("ornek.txt",mode="r")
satirlar=dosya.readlines()
for s in satirlar:
    print(s)
    
# "x" modu (create)  sadece dosya oluşturur,dosya zaten varsa hata verir
file=open("newfile.txt","x")
file.close()
















