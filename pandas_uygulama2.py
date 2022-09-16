#Pandas ile keşifsel veri analizi
#https://www.kaggle.com/ashishgup/netflix-rotten-tomatoes-metacritic-imdb
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html
import pandas as pd
df=pd.read_csv("StudentsPerformance.csv")
#Dosyanım df isminde DatFrame nesnesine dönüştü
#df in satır ve sütun sayısı hakkında bilgi verir
print(df.shape)
#dosyanın sütunlarının ve veri tipleriin neler old. öğrenebilirim
print(df.columns)
print(df.dtypes)
#df in ilk bir kaç satırına bakalım
#head() metodu df in ilk 5 satırını döndürüyor
#tail() metodu df in son 5 satını döndürüyor.
print(df.head())
print(df.tail(8))
#info() metodu: df hakkında gelen bilgi verir
print(df.info())
