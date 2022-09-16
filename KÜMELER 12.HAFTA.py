kume={1,2,3,45}
print(type(kume))
"""<<<class 'set'>"""

#LİSTELERKÜMEYE DÖNÜŞEBİLİR
l=["al","ver",1,2]
donus=set(l)
print(donus)
"""<<   {'ver', 2, 'al', 1}}"""

#KÜMEYE ELAMN EKLEME
kume1={"elma","armut","kiraz"}
kume1.add("erik")
print(kume1)
"""  {'armut', 'kiraz', 'elma', 'erik  """

#KÜMEDEN ELEMAN SİLME
kume2={1,2,3,4,5,8,9}
#kume2.remove(10) hata verir #ALFABETİK ELEMANLARI SİLER
kume2.discard(3)
print(kume2)

kume3={"ali","muhammed talha","eltoş","şükran"}
kume3.remove("şükran")
print(kume3)
"""<<<     {'eltoş', 'muhammed talha', 'ali'}  """

#İKİ KÜME FARKI   -
kumea={"a","b","c"}
kumeb={"a","b","c","d","e","f"}
fark=kumeb.difference(kumea) #fark1=kumeb-kumea aynı şey
print(fark)
"""<<<    {'f', 'e', 'd'}  """   

#KESİŞİM KÜMESİ BULMA &
kumea={"a","b","c"}
kumeb={"a","b","c","d","e","f"}
kesisim_a=kumea&kumeb #kesisim=kumea.intersection(kumeb) aynısı
print(kesisim_a)
"""<<  {'a', 'c', 'b'}   """
"""#### girdiğimiz kelime türkçe karakter barındırıyor mu
karakter="çğıöşüÇĞIÖŞÜ"
isim=input("isim giriniz:..")
if set(karakter)&set(isim):
    print("girdiğimiz kelime türkçe karakter barındırıyor")"""

#AYRIK KÜME
kume11={1,2,3,4}
kume22={4,5,6,7}
ayrikmi=kume11.isdisjoint(kume22)
print(ayrikmi) 
"""False"""

#ALT KÜME
kumeb={1,2,3}
kumec={1,2,3,4,5,6,7}
altkumemi=kumeb.issubset(kumec)
print(altkumemi)
"""True
>>> """

#KAPSAYAN KÜME
kapsar=kumec.issuperset(kumeb)
print(kapsar)
"""True"""

#BİRLEŞİM  |
#union()
kumex={1,2,3}
kumey={"ali","asya","sefa"}
birlesim=kumex.union(kumey) #birlesim2=kumex|kumey
print(birlesim)
"""<<  {1, 2, 3, 'ali', 'asya', 'sefa'}"""







    





