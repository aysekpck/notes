#stamp(damga/kaşe) ile ekrana dokuz sarmalı çizdiren programı yazınız
"""
from turtle import *
#shape("circle") # damga şekli daire olsun
shape("turtle")
penup() # kalemi kaldır
# 47 adet damga bas (-1,...,45)
for i in range(45,-1,-1):
    stamp() # mevcut damgayı bas
    right(i)  # sağa dön
    backward(15)  # 15 birim geriye git
 """
#Çokgen çizimi
"""
from turtle import *
kenar=int(input("Kenar sayısı: "))
aci=360/kenar
pensize(3)
for i in range(kenar):
    forward(50)
    left(aci)
"""
#Çokgen çizimi
"""
from turtle import *
kenar=int(textinput(" ","Kenar sayısı:"))
aci=360/kenar
pensize(2)
color("blue")
shape("square")
bgcolor('yellow')
for i in range(kenar):
    circle(50,aci,1)
"""
"""
textinput("başlık","mesaj"):  Bir iletişim (diyalog) kutusu içerisinde
veri girilmesini bekler.
"""




