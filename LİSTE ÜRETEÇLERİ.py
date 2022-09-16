#LİSTE ÜRETEÇLERİ
#Belirli bir sayı dizilimi ile otomatik listeler üretmenin kısa yoludur.
#0'dan 4'e elemanlardan oluşan liste
"""liste=[a for a in range(5)]
print(liste)
<<[0, 1, 2, 3, 4]

"""
#şu şekilde çalıştırılırsa
"""liste=[a+1 for a in range(5)]
print(liste)
<<[1, 2, 3, 4, 5]"""

#5 ile 16 arasındaki tek sayıları yazdıralım
"""liste1=[a for a in range(5,16) if a%2==1]
print(liste1)
<<[5, 7, 9, 11, 13, 15]"""

#5 ile 100 arasında hem 5'e hem 3'e bölünebilen sayılar
"""liste3=[a for a in range(5,100) if a%5==0 and a%3==0]
print(liste3)
<<[15, 30, 45, 60, 75, 90]"""
