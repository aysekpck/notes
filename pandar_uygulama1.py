#Pandas kütüphanesi
#Veri analizi yaparken kullanılır.
#Temel veri yapıları Seriler ve DataFrame lerdir.
#cmd'ye pip install pandas yazarız
#daha sonrada kütüphaneyi sayfaya yüklüyoruz
import pandas as pd
import numpy as np
"""
Pandas veri yapıları:
*Series
   my_series=pd.Series(data,index)
Data parametresi:
-sabit değer
-liste
-NumPy dizisi,
-Sözlük(dictionary) olabilir
*DataFrames
"""
numbers=[1,2,3,4,5,6,7,8,9]
numpy_array=np.array(numbers)
print(numpy_array)
pandas_series=pd.Series(data=numbers)
print(pandas_series)
my_index=["a","b","c","d","e","f","g","h","i"]
pandas_series=pd.Series(data=numbers,index=my_index,dtype=float)
print(pandas_series)
"""
dictionary(sözlük) {key:value,key1:value1,..}
"""
my_dictionary={"apple":"elma", "cherry":"kiraz","banana":"muz",
               "strawberyy":"çilek"}
new_series=pd.Series(data=my_dictionary)
print(new_series)
"""
Seriler Numpy dizilerine çok benzer.
NumPydaki birçok metod pandasta da vardır.
ndim, dtype, shape gibi özellikler burdada vardır.
"""
print(new_series.ndim)
print(new_series.dtype)
print(new_series.shape)
#max() min() sum() median() mean()...
print(pandas_series.max())
print(pandas_series.min())
print(pandas_series.sum())
print(pandas_series.median())
print(pandas_series.mean())
#MATEMATİKSEL İŞLEMLER
num1=[12,13,14,15,16,17]
num2=[5,10,15,1,5,6]
series1=pd.Series(data=num1)
series2=pd.Series(data=num2)
print(series1+series2)
print(np.sqrt(series2))
print(series1*series1)
#KOŞULLU İFADE
print(series1[series1>14])
print(series1[series1<series1.median()])
print(series2[series2==5])

"""
DataFrame:
        my_dataframe=pd.DataFrame(data,index)
data parametresi:
-dictionary
-series
-listelerden oluşan dictionary
-2 boyutlu numpy dizi
-başka bir datafram yapısı olabilir.
"""
#data dictionaryden oluştuğunda

dict1=dict(a=1,b=2,c=3,d=4)
dict2=dict(a=5,b=6,c=8,d=9)
data1=dict(first=dict1,second=dict2)
df1=pd.DataFrame(data1)
print(df1)

#Data serilerden oluştuğunda
s1=pd.Series([1.1, 1.2, 1.3, 1.4])
s2=pd.Series(["a","b","c","d"])
data2=dict(first=s1,second=s2)
print(pd.DataFrame(data2))

#Data başka bir DataFrame den oluşabilir
df2=pd.DataFrame(data2)
df3=pd.DataFrame(df2)
print(df3)

#Pandas veri seçme işlemler(selecting) işlemleri
#df.loc[row,column]



