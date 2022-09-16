#NumPy lineer cebir işlemleri:
import numpy as np
import pandas as pd
#uygulama 1: NumPy matris oluşturma
matrix=np.array([[1, 2],
                 [3,4],
                 [5,6]])
print(matrix)
#max, min değer bulma
print(matrix.min())
print(matrix.max())
#matris boyutu
print(matrix.size)
print(matrix.shape) # kaça kaçlık matris old. söyler (3,2)
#boyut sayısı
print(matrix.ndim)
#matrisin ortalamasının bulunması
print(matrix.mean())
#matrisin varyans hesabı
print(matrix.var())
#matrisin standart sapması
print(matrix.std())
#bir elemanına erişim- 4 e erişelim
print(matrix[1][1])
print(matrix[2][1])
#bir satırdaki tüm elemanlara erişmek
print(matrix[2,:])
#bir sütundaki tüm elemanlara erişmek
print(matrix[:,1])
#İki matrisin toplanması
matris1=np.array([[10,20,30],
                  [5,6,7],
                  [0,2,45]])
matris2=np.array([[1,2,5],
                  [10,15,20],
                 [0,5,15]])
toplam=np.add(matris1,matris2)
print(toplam)
#matris toplamı için boyutları aynı olması gereklidir
#matrsilerde çıkarma için de geçerli bu
print(np.subtract(matris1,matris2))
#matris çarpımı: ilk matrisin sütun sayısı ikincinin
#satır sayısı ile aynı olmalı
#3x2 * 2x5 = 3x5 çarpılabilir
mat1=np.array([[12,11],
               [1,2],
               [10,20]])
mat2=np.array([[1,2,3,4,5],
               [10,20,30,40,50]])
carpım=np.dot(mat1,mat2)
print(carpım)
#matrisin tersini bulma
mat_iki=np.array([[1,3],
                  [2,2]])
print(mat_iki)
print(np.linalg.inv(mat_iki))
"""
-1/4*[2 -3,
      -2 1] =[-0.5 0.75
              0.5 -0.25]
"""
#matris skaler çarpımı
print(mat_iki*2)
#determinantının bulunması
print(np.linalg.det(mat_iki))
#matrisin transpozu
print(mat_iki.transpose())
#sınıfır matrisin tanımı
print(np.zeros([4,4]))
#Birim matris oluşturma
print(np.identity(4))
mat2=np.array([[1,2,3,4,5],
               [10,20,30,40,50]])
#matrisin köşegen elemanlarını alıp köşegen matris oluşturmak
print(np.diag(np.diag(mat2)))

matris1=np.array([[10,20,30],
                  [5,6,7],
                  [0,2,45]])
print(np.diag([10,20,30,40]))


