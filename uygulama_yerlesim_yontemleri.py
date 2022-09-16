"""
Yerleşim(layout ) Yöntemi:
Bir çerçeve içerisine kontrol nesnesini (buttonlar, etiketler vb)
hangi boyutlarda, nereye yerleştirileceğine karar verir.
1)
pack() metodu: Kontrol bileşenleri paketlenip cerceve içerisinde uygun
boşluklara yerleştirilir.
parametreleri:
LEFT, RIGHT, TOP BOTTOM
fill:X Y BOTH NONE (fill=NONE) olmak üzere widgetların büyüme yönünü belirtir.
expand: 1/0 YES/NO veya True/False değerlere bağlı
widget ın çerçece boyunca genişlemesine onay verir ya da vermez.
"""
"""
from tkinter import *
gui=Tk()
#Label çerçeve ortasına yerleşti
Label(gui,text="Pack metodu örneği").pack()
#Başlık genişliği çerçevini ortasına yerleşti
Button(gui,text="genişlet bakalım").pack(expand=1)
#A butonu y eksenine uzatıldı ve sola yerleşti
Button(gui,text="A").pack(side=LEFT,fill=Y)
#B butonu x eksenine uzatıldı ve yukarı yerleşti
Button(gui,text="B").pack(side=TOP,fill=X)
#C buton uzatılmadan sağa yerleştirildi
Button(gui,text="C").pack(side=RIGHT,fill=NONE)
#D botonu her iki yana uzatıldı ve Aşağıya yerleşti
Button(gui,text="D").pack(side=TOP,fill=BOTH)
mainloop()
"""
"""
2) grid() metodu kullanımı:
-Kontrol nesneleri excel tablosuna benzer şekilde
hücrelere yerleştirilir(satır-sütun)
-en sık tercih edilendir
Parametreleri :
row(satır) column(sütun) sticky 
-ilk satır ve sütun için row=0, column=0
-sticky: N(kuzey), S(güney), E(doğu) W(batı) NW
NE SE SW
"""
"""
from tkinter import *
gui=Tk()
#kullanıcı adı etiketi row=0, column=0 sticky =W
Label(gui,text="Kullanıcı adı").grid(row=0,column=0,sticky=W)
#Sifte etiketi yazdır
Label(gui,text="Şifre").grid(row=1,column=0,sticky=W)
#Veri giriş kutusu 0.satır ve 1.sütun ve Sticky E
Entry(gui).grid(row=0,column=1,sticky=E)
Entry(gui).grid(row=1,column=1,sticky=E)
#Giriş butonu 2.satır ve 1. sütun ve kuzeybatı (NW)da
Button(gui,text="Giriş").grid(row=2,column=1,sticky=N)
"""
"""
place() metodu:
Kontrol nesneleri tüm parametre değerleri verilerek (x,y koordinatları
genişlik-Yükseklik, yön değerleri gibi) hassas şekilde
yerleştirilir.
-sticky nin yerine anchor alıyor.
"""
from tkinter import *
gui=Tk()
Button(gui,text="Hassas").place(x=20,y=10)
Entry(gui).place(x=90,y=10)
Button(gui,text="Tahmini").place(x=110,y=50,anchor=NE)
mainloop()









