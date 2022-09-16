#DÖNGÜLER

#FOR

"""
names=["çınar","sadık","sena"]

for name in names:
    print(f'my name is {name}')
<<<my name is çınar
<<<my name is sadık
<<<my name is sena
"""
"""
sayilar=[1,2,3,4]
for i in sayilar:
    print('hello')
<<<hello
   hello
   hello
   hello
"""
"""
tuple=[(1,2),(1,3),(3,5),(6,7)]
for t in tuple:
    print(t)
(1, 2)
(1, 3)
(3, 5)
(6, 7)
>>>
"""
"""
tuple=[(1,2),(1,3),(3,5),(6,7)]
for a,b in tuple:
    print(a,b)
1 2
1 3
3 5
6 7
>>>
"""

#DİCTİONARY de FOR: dictionary için  .items() konmalı 

"""
d={'k1':1, 'k2':2 , 'k3':3}
for key,value in d.items():
    print(key,value)
<<<k1 1
<<<k2 2
<<<k3 3
"""

#WHİLE DÖNGÜSÜ

""" 0-dan 100 e kadar yazdırma
x=0
while x <= 100:
    print(x)
    x=x+1
print("bitti..")    
"""

"""
name=''
while not name:
    name=input('isminizi giriniz: ')
    print(f"merhaba {name}")
isminizi giriniz: ali
merhaba ali    
"""
"""
name=''
while not name.strip():  #baştan ve sondan boşluğu siler
    name=input('isminizi giriniz: ')
    print(f"merhaba {name}")
"""
#DEMOs

"""
sayilar=[1,3,5,7,9,12,19]
i=0
while i<len(sayilar):
    print(sayilar[i])
    i+=1
<<<    
1
3
5
7
9
12
19
"""

#BAŞLANGIÇ VE BİTİŞ DEĞERLERİNİN KULLANICIDAN ALIĞP ARADAKİ TÜM TEK SAYILARI YAZDIRIN

"""
baslangic=int(input("başlangıç için bir sayı giriniz: "))
              
bitis=int(input("bitiş için bir sayı giriniz: "))

i=baslangic
while i<bitis:
     i+=1
     if(i%2==1):
         print(i)
<<<17
19
21
23
25
27
29
31
33
35
37
39
41
43
"""
#100 den 0 a kadar yazdırma
"""
x=100
while x>0:
    x-=1
    print(x)
"""


#girilen beş sayıyı sıralı bir şekilde dizme
"""
numbers=[]
i=0
while i<5:
    sayi=int(input("sayi: "))
    numbers.append(sayi)
    i+=1
numbers.sort()
print(numbers)

  <<<  sayi: 1
       sayi: 15
       sayi: 11
       sayi: 45
       sayi: 55
       [1, 11, 15, 45, 55]

"""




###

"""
numbers=[x for x in range(6)]
print(numbers)

[0, 1, 2, 3, 4, 5]
"""

"""
yil=[1983,1996,2010,1027]
yas=[2021-yil for yil in yil]
print(yas)
<<<
[38, 25, 11, 994]
"""























