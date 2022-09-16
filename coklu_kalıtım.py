#Çoklu kalıtım
"""
Pythonda bir alt sınıfın birden fazla üst sınıfı olabilir.
Bu durum çoklu kalıtım olarak adlandırılır.
Örneğin; evlat sınıfı kendi mal varlığına ek olarak,
Anne ve Baba üst sınıfından ayrı ayrı miras alabilir.
"""
#Örnek.
class Anne():
    #yapıcı metot ve parametreleri
    def __init__(self,mal1):
        self.mal1=mal1

    def __str__(self):
        return "Anneden:" + self.mal1

class Baba():
    #yapıcı metot ve parametreleri
    def __init__(self,mal2):
        self.mal2=mal2

    def __str__(self):
        return "Babadan:"+self.mal2

#ayse=Anne("ev")
#print(ayse.__str__())
#Anne ve Baba sınıfından çoklu kalıtımla Evlat sınıfı
class Evlat(Anne,Baba):
    def __init__(self,mal1,mal2,kendimalı):
        #Anne ve Baba sınıfından örnekler oluşturuldu
        Anne.__init__(self,mal1)
        Baba.__init__(self,mal2)
        self.kendimalı=kendimalı
    def __str__(self):
        return Anne.__str__(self)+ "\n"+Baba.__str__(self)+"\nKendi malı:"+ str(self.kendimalı) 
miras=Evlat("Ev","Arsa","Araba")
print(miras)



    


