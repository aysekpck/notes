#LİSTELER

#İNSERT:listede istenilen sıradan sonra ekleme yapar
"""
numbers=[1,2,3,4,5,6]
numbers.insert(3,45)
print(numbers)
<<<[1, 2, 3, 45, 4, 5, 6] 
"""
liste_s=[12,34,56]
del.liste_s
print(liste_s)

#APPEND: listeye ekleme yapar sonuna ekler

"""
numbers=[1,2,3,4,5,6]
numbers.append(45)
print(numbers)
<<<[1, 2, 3, 4, 5, 6, 45]
"""
#İNDEX:sorulan elemanın listede hangi numarada olduğunu verir
"""
liste7=[145,23,56,22,34]
indis=liste7.index(34)
print(indis)

4
>>> 
"""

#POP:istenilen satırdaki elemanı siler

"""
liste=[1,2,3,4,5,6]
a=liste.pop()
print(a)
print(liste)
6
[1, 2, 3, 4, 5]
"""
#
"""
numbers=[1,2,3,4,5,6]
numbers.pop(3)
print(numbers)
<<<[1, 2, 3, 5, 6]
"""
#REMOVE:silmek istenilen karakter () içinde verilir

"""
numbers=[1,2,3,4,5,6]
numbers.remove(4)
print(numbers)
<<<[1, 2, 3, 5, 6]
"""
#SORT:liste sayılar küçükten büyüğe doğru sıralanır

"""
numbers=[1,2,3,4,5,6]
numbers.sort()
print(numbers)
"""

#REVERSE:listeyi tersten yazar

"""
numbers=[1,2,3,4,5,6]
numbers.reverse()
print(numbers)
<<<[6, 5, 4, 3, 2, 1]
"""

#COUNT: içinde bulunan elemanın kaç tane olduğunu verir

"""
elemanlar=[1,1,22,2,3,6,55,5]
print(elemanlar.count(1))

"""
#SPLİT:istenileni liste yapar

"""
str="dacia,chevrolet"
result=str.split(',')
print(result)
['dacia', 'chevrolet']
"""

#TUPLE:Listeden farkı listede kullanılan [] yerine () kullanılır
#eleman atandıktan sonra tuple da değiştirilemez ama listede değiştirilebilir

#DİCTİONARY
# KEY - VALUE
"""
değişken={ 'key':  , 'value': } #genel kullanımı
print(değişken['key'])
"""
"""
plakalar={'kocaeli':41, 'istanbul':34}
print(plakalar['kocaeli'])
41
>>> 
"""

# key ve value daha önceden olmayan bir değer eklemek

"""
plakalar={'kocaeli':41, 'istanbul':34}
plakalar['ankara']=6
print(plakalar)
>>>{'kocaeli': 41, 'istanbul': 34, 'ankara': 6}
"""

#BİRDEN ÇOK İSTEDİĞİMİ ÇAĞIRMA
"""
users={
    'aysenurkapcik':{
        'age':20,
        'email':'aysrnur@gmail.com',
        'address': 'istanbul',
        'phone': '122334'
     },
     'furkankapcik':{
        'age':25,
        '2phone':'34534545'
     }   
}    

print(users['furkankapcik'])

>>>{'age': 25, '2phone': '34534545'}
"""

#SETS

#add: tek eleman ekler

"""
fruits={"banana","orange","apple"}
fruits.add("cherry")
print(fruits)
>>>{'apple', 'banana', 'orange', 'cherry'}
"""

#update:sıralamanın içine liste ekler

"""
fruits={"banana","orange","apple"}
fruits.update(["mango","grape"])
print(fruits)
>>>{'banana', 'grape', 'apple', 'orange', 'mango'}
"""

#VALUE and REFERENCE types


#value type:str,nunmbers

"""
x=5
y=25
x=y
y=10
print(x,y)           
>>>25 10            #y deki son atama x 'i etkilemez
"""


#reference types:list,class

"""
a=["banana","apple"]
b=["banana","apple"]

a=b

a[0]="grape"
print(a,b)

>>>['grape', 'apple'] ['grape', 'apple']            #b'deki son değişiklik a'yı da etkiler

"""

#DEL: listenin tamamını veya belli satırdaki elemanı siler

"""
liste1=[1,2,3,4,5,6,7,8]
del liste1[3]
print(liste1)

[1, 2, 3, 5, 6, 7, 8]
>>> 
"""

















