#PANDAS MODÜLU ÖRNEK SORULAR
import pandas as pd
#.csv formatındaki dosyanın veri analizi yapacagız
#https://www.kaggle.com/learn/pandas
df=pd.read_csv('Fish.csv')
#dosyayı df isminde DataFrame nesnesine dönüştürdü
#print(df)
print(df.shape)
#(159, 7) dosyanın satır ve sürun sayısı hak.bilgi verir
print(df.columns)#sütun elemanları hak. bil. verir
print(df.dtypes) # herbir sütun elemanının tipini söyler
df.head()  # head() metodu veri setinin ilk 5 satırını gösterir
print(df.head())
df.tail() #tail() metodu son 5 satırı verir. içine 8 yazarsak 8 satırı verir.
print(df.tail(8))
#sadece belirli kolonları görmek istiyorusam
df.Length1  # Lenght1 sütununu listeler
print(df.Length1)
print(df[['Species','Height']]) #birden fazla sütun seçimi yapmak istersem
"""
    Species   Height
0     Bream  11.5200
1     Bream  12.4800
2     Bream  12.3778
3     Bream  12.7300
4     Bream  12.4440
..      ...      ...
154   Smelt   2.0904
155   Smelt   2.4300
156   Smelt   2.2770
157   Smelt   2.8728
158   Smelt   2.9322

[159 rows x 2 columns]
>>> 
"""
#belirli satır arasındaki değerleri görmek için;
#df.loc[from_row:to_row:step,['column1','column2']]

print(df.loc[4:10,['Species','Height']])
"""
   Species   Height
4    Bream  12.4440
5    Bream  13.6024
6    Bream  14.1795
7    Bream  12.6700
8    Bream  14.0049
9    Bream  14.2266
10   Bream  14.262
"""
#info() metodu
print(df.info()) #df hak. genel bilgi verir
#missing values-kayıp veri bulmak için
#pd.isnull()
print(pd.isnull(df.Species))
"""
0       True
1       True
2      False
3       True
4      False
       ...  
154    False
155    False
156    False
157    False
158    False
Name: Species, Length: 159, dtype: bool
"""
print(df[pd.isnull(df.Species)]) # df içerisinde Species kutucuğu boş olan satırı yazar.
df.isnull().sum().sort_values(ascending=False)
#df deki eksik değerlerin sayısının toplamını azalan sırada verir.
print(df.isnull().sum().sort_values(ascending=False))
"""
Species    3
Weight     2
Length1    2
Length2    0
Length3    0
Height     0
Width      0
dtype: int64
"""
#boş değeri değiştirmek : fillna()
print(df.Species.fillna("Bilinmeyen"))
#######################################
## satır silmek ##   drop(satır numarası)
"""
drop() fonk. stenilen satırları sildiğinde, yeni bir daha frame döndürür
Yani asıl Dataframe de değişiklik olmaz.
"""
#1.yöntem
df1=df.drop(1,axis=0)
print(df1)
#2.yöntem
df.drop(1,inplace=True)
print(df)
# Sütunları kaldırmak isin axis=1 yazmalı
df2=df.drop("Width",axis=1)
print(df2)




























