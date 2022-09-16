#matplotlib kütüphanesi
"""
*Grafik çizim paketidir.
*Verilr etkileşimli olarak görselleştirilir.
"""
"""
import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5], [1,4,9,16,25])
plt.show() # plt.ion() komutu da kullanlabilir. (interactive on)
"""
#Örnek.
"""
#y=exp^(-x)*sin(3*x) fonksiyonunu x in [-1,5] aralığında adım uzunluğu= 0.1 olsun.
import matplotlib.pyplot as plt
from math import exp, sin
# -1, -1 + 0.1, -1+ 0.1*2, -1 + 0.1*3, -1 +0.1*4,...5    x değerleri
x=[-1+ 0.1*z for z in range(60)]
y=[exp(-z)*sin(3*z) for z in x]
plt.plot(x,y)
plt.show()
"""
"""
import matplotlib.pyplot as plt
import numpy as np
from math import exp, sin
x=np.arange(-1,5,0.1)  # 5 dahil olmaz
y=np.exp(-x)*np.sin(3*x)
plt.plot(x,y)
plt.show()
"""
"""
Matplotlib içerisinde hem pyplot hem de numpy modüllerinin birleşimi
pylab modülü var. Böylece daha kısa yazmak mümkün.
"""
from pylab import *
x=arange(-1,5,0.1)
y=exp(-x)*sin(3*x)
plot(x,y)
title("$e^{-x}\sin(3x)$ eğrisinin grafiği")
xlabel("Yatay eksen")
ylabel("Dikey eksen")
#xticks([0, 0.5, 2, 4.5])  # x ekseninde gözükmesini istediğim değerler
#yticks(arange(-2,2,0.5))  #y ekseninde gözükmesini istediğim değerler
#eksen sınırlarını değiştirmek
#axis(xmin=1,xmax=2,ymin=-1.5,ymax=0.5) # eksen sınırlarını değiştrme için, beliri kesitini almak için
#axis("off")
#axis("equal") #veri aralığını ölçekler eşitlemek için
#axis("scaled") # sekil kutusunun büyüklğünü değiştirerek ölçekleri eşitlemek
axis("tight") #bütün verileri tam sığaak sekilde ayarlamak.
grid(True)
#figure(figsize=(10,8)) #10 inç genişlik, 8 inç yükseklik
show()
#savefig("mygrafh.eps",dpi=300) #(bir inçte 300 nokta) çözünürlük











