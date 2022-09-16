





#✅ Uygulama 1: Numpy projemize ekleyelim;
import numpy as np

#✅ Uygulama 2: Numpy  array ile tek boyutlu array oluşturalım;
array = np.array([1,2,3,4,5,6,7,8,9])

#✅ Uygulama 3: Numpy arange() fonksiyonu ile array olusturalim;
array1 = np.arange(10)

#✅ Uygulama 4: Numpy arange() ile 20’ye kadar çift sayılar array oluşturalım;
array2 = np.arange(0,20,2)

#✅ Uygulama 5: Numpy array içinde 10 dan büyük sayıları sıfır yapalım;
array2[array2>10]=0
print(array2)

#✅ Uygulama 6: Numpy array uzunluğunu bulalım;
print(array2.size)

#✅ Uygulama 8: Numpy array kaç boyutlu olduğuna yani boyut sayısına bakalım;
print(array2.ndim)

#✅ Uygulama 9: Numpy array eleman type bulalim;
print(array2.dtype)

#✅ Uygulama 10: Numpy array bellekte bayt olarak boyutu(int64);
print(array2.itemsize)

#✅ Uygulama 11: Numpy dizinin tüm elemanlarının toplamı;
print(array2.sum())

#✅ Uygulama 12: Numpy array deki en büyük eleman;
print(array2.max())

#✅ Uygulama 13: Numpy array en küçük eleman;
print(array2.min()) 
