#DÖNGÜ METOTLARI RANGE- ENUMERATE
"""
index=0
greeting="Hello There"

for letter in greeting:
    print(f'index: {index} letter: {greeting[index]}')
    index+=1
<<index: 0 letter: H
index: 1 letter: e
index: 2 letter: l
index: 3 letter: l
index: 4 letter: o
index: 5 letter:  
index: 6 letter: T
index: 7 letter: h
index: 8 letter: e
index: 9 letter: r
index: 10 letter: E
"""

#YUKARIDAKİNİ ENUMERATE İLE YAPALIM
"""
greeting="HELLO KELTOŞ"
for item in enumerate(greeting):
     print(item)
<<<(0, 'H')
(1, 'E')
(2, 'L')
(3, 'L')
(4, 'O')
(5, ' ')
(6, 'K')
(7, 'E')
(8, 'L')
(9, 'T')
(10, 'O')
(11, 'Ş')
"""

#RANGE

"""
for i in range(2,50,3):
    print(i)
print(list(range(2,50,3)))

 =
2
5
8
11
14
17
20
23
26
29
32
35
38
41
44
47
[2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47]
>>> 
"""

#ZİP :Eşleştirme yapar

"""
list1=[1,2,3,4,5,6]
list2=["a","b","c","d","e"]

print(list(zip(list1,list2)))

[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
"""



"""
liste=[a for a in range (11)]
print(liste)
liste2=[a+10 for a in range(11)]
print(liste2)

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
"""

#5 İLE 16 ARASINDAKİ  tek sayı ELEMANLARDAN OLUŞAN LİSTE
"""
liste3=[a for a in range(5,16)if a%2==1]
print(liste3)
        
[5, 7, 9, 11, 13, 15]
"""


















