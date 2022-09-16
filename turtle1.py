#turtle ile çizim

"""
*Turtle grafik ekranı bildiğimiz matematiksel (kartezyen)
koordinat ile aynıdır.
*turtle grafik ekranının tam orta noktası,
koordinat sisteminin merkezini oluşturur.
*sağa doğru uzanan yatay çizgi pozitif x
*sola doğru uzanan yatay çizgi negatif x
*merkezden yukarı doğru uzanan dikey çizgi pozitif y
*merkezden aşağı doğru uzanan dikey çizgi negatif y
değerlerini içerir.
*Python koordinat sisteminin ölçü birimi olarak piksel kullanılır.
*Piksel bir grafiksel örüntüyü oluşturan noktalardan her biridir.
*turtle grafik ekranının başlangıç noktası (0,0) noktasıdır.
*Ekranın herhangi bir noktasını konumlamak için
goto(x,y), setposition(x,y) veya setpos(x,y) dan biri kullanılır.
*Ekranın sol üst köşesine konumlamak için: setposition(-950,500)
*Tekrar başlangıç noktasına konumlamak için: reset() kullanılır.
*Sadece x ekseninin konumunu değiştirmek için setx(x)
*Sadece y ekseninin konumunu değiştirmek için setx(y) kullanılır. 
"""
#kare çizimi
"""
from turtle import *
forward(100) #-
left(90)
forward(100) #|
left(90)
forward(100)#-
left(90)
forward(100) #|
"""
# kaplumbağa robota üçgensel hareket yaptıran uygulama
"""
from turtle import *
reset()
shape("turtle")
forward(100)#-
left(120)
forward(100)
left(120)
forward(100)
"""
#kaplumbağa robotunu 5 basamak aşağıya indiren br uygulama
"""
from turtle import *
reset()
shape("turtle")
for i in range(5):
    forward(50)
    right(90)
    forward(50)
    left(90)
"""
#2017 yılı itibari ile Erzincan,Erzurum,Eskşehir, Tokat,Sakarya
#illerinin yaklaşık nüfusu sırası ile
#231.511,760.476,860.620,602.086 ve 990.214 olarak sayılmıştır.
#Bu illerin nüfusunu bar grafik olarak çizin.
"""
from turtle import *
nfs=[231.511,760.476,860.620,602.086,990.214 ]
goto(0,-200)

def cizBar(height):
    left(90) #sola dön
    forward(height/10) # sol kenarı çiz
    #nüfus değerlerini yaz
    write("" +str(height))
    right(90) # sağa dön
    forward(44) # sağ kenar: bar genişliği
    right(90)
    forward(height/10) # sağ kenarı çiz
    left(90) #sola dön

pensize(3) #çizgi kalınlığı
begin_fill() # boyamaya başla
color("blue", "red") #mavi çerçeve, kırmızı da içi
write("Erzincan-Erzurum-Eskişehir- Tokat-Sakarya")
for v in nfs:
    cizBar(v)
end_fill()
"""
#Bir mimara her elemanı kendisinden önceki iki elemanın toplamı şeklinde
#ifade edilen fibonacci serisinin değerlerini kullanarak kare odalı bir ev planı
#çizdirecek programı yazınız.
"""
from turtle import *
#Fibonaci serisi
fibN=[1,1,2,3,5,8,13,21,34,55]
uz=len(fibN)
k=5 #genişletme katsayısı
pensize(2) # kalem kalınlığı

#kare şeklinde oda çizen fonksiyon
def kareCiz(kenarUz):
    for i in range(6):
        forward(kenarUz)
        right(90)
#ev planı
for i in range(uz-1):
    left(90)
    kareCiz(fibN[i]*k) # kenar uzunluğu fibonacci sayısı*k olan kare
"""
#Ekrana çizgi rengi kırmızı, dolgu rengi beyaz olan bir yıldız çizdiren program
"""
from turtle import *
shape("blank") # ok kullanmamak için
pensize(3)
for i in range(5):
    color("red")
    forward(100)
    right(144)
"""
#Dairesel çizim ve dairesel hareketler
#circle(yarıçap, açı,adım) metodu kullanılır.
#yarıçap zorunlu, diğerleri zorunlu değildir.
"""
from turtle import *
#circle(-100) #100 brm çaplı saat yönünde hareket eden daire
#circle(50) #50 brm saat yönünün tersine hareket eden daire
#circle(100,180) #yarım daire
#circle(-100,110) #100 brm yarıçaplı, 110 derecelik yay çizer.

#for i in range(3):
#    circle(100,120,2)#Altıgen
#(100 brm çaplı,120 derecelik açıya sahip 2 şer adımlı)
"""
"""
from turtle import *
#çerçeve boyutu belirleme
setup(900,500)
#resim dosyası
bgpic("kedi.gif")
#başlık
title("kediler çok sevimli")
"""

        
    






























