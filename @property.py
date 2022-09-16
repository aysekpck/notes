
"""personel listesindeki simi yalnızca şöyle bi komut vererek
değiştiremez miyiz?
cal1.isim="aslı" """

#bunun için @property adlı bezeyiciden yararlanacağız

class Çalışan():
     personel=[]
     def __init__(self,isim):
          self.isim=isim
          self.personel_ekle()
     def personel_ekle(self):
          self.personel.append(self.isim)
          print('{} adlı kişi personel listesine eklendi'.format(self.isim))
     @classmethod
     def personeli_görüntüle(cls):
          print("personel listesi")
          for kişi in cls.personel:
               print(kişi)
     @property
     def isim(self):
          return self.isim
     @isim.setter
     def isim(self,yeni_isim):
          kişi=self.personel.index(self.isim)
          self.personel(kişi)=yeni_isim
          print('yeni isim',yeni_isim
                
cal1=Çalışan("alı")               
cal2=Çalışan("ayse")
Çalışanipersoneli_görüntüle()
                
cal1.isim="nurcan" #ali yerine nurcan oldu
Çalışan.personeli_görüntüle()                



"""
@propert bezeyicisinin yaptığı en temel iş:
bir metotu nitelik gibi kullanılabilecek hale getirmek

"""
