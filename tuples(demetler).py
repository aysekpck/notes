#DEMETLER (TUPLES)
#Demetler(tuples)listeler çok benzer ancak farkı oluşturulduktan sonra,
#üzerinde ekleme, silme, değiştirme, sıralama gibi işlemler yapılamamsıdır.
#Demetler sadece okunabilir listelerdir.

demet=tuple() # boş demet tanımlar
demet=() #boş  demet tanımlar
demet=tuple([1,2,3]) #içerisinde 1,2,3 değeri olan demet tanımlar
demet=("elma","armut","kiraz") # string demet
demet=(1,2,3,"elma","armut") #farklı türde elemanlardan oluşan bir demet


#DEMET ELEMANLARINA ERİŞİM
#demet elemanlarının 0'dan başlayan bir indis numarası vardır.
demet=(1,2,3)
a=demet[1]
print(a) # 2

# Demetlerin eleman değeri sonradan değiştirilemez
demet=(10,20,30,40)
demet[1]=2000 #TypeError: 'tuple' object does not support item assignmen#DEMET EKRANA YAZDIRMA
demet=(10,20,30,40,50,60)
print(demet)


#DEMET PARÇALAMA
#demet[başlngıç:bitiş:artış]
print(demet[1:5])


#DEMETTE ELEMAN VARLIĞINI KONTROL ETME
print(60 in demet)
print(70 not in demet)


#DEMET İÇİNDE BİR ELEMANIN KAÇ KEZ TEKRAR ETTİĞİNİ BULMA
demet2=(1,2,3,4,67,3,4,5,3,7,1,2,3)
print(demet2.count(3))


#DEMET EN BÜYÜK VE EN KÜÇÜK ELEMANI BULMA
b=max(demet2)
k=min(demet2)
print("En büyük eleman:",b,"En küçük eleman:",k)


#DEMET ELEMANLARINI TOPLATMAK İÇİN
topla=sum(demet2)
print(topla)
































