#optionmenu
#İngilizce-Türkçe çeviri yapan sözlük uygulaması
from tkinter import *
gui=Tk()
gui.title("Sözlük Programı")
#değişken tanımlama: deg1, deg2
deg1=StringVar()
deg1.set("İngilizce")
deg2=StringVar()
deg2.set("Türkçe")
L1=["one","two","three","four","five"]
menu1=OptionMenu(gui,deg1,"one","two","three","four","five")
menu1.pack(side=LEFT) #menu1 yerleşimi
L2=["bir","iki","üç","dört","beş"]
menu2=OptionMenu(gui,deg2,"bir","iki","üç","dört","beş")
menu2.pack(side=RIGHT) #menu2 yerleşimi

def cevir(): #ingilizce-türkçe çevirimi  
   # print(deg1.get(),'=',deg2.get())
    for i in L1:
       if i==deg1.get():
           a=L1.index(i)
           print(i,'=',L2[a])
    
buton=Button(gui,text="OK",command=cevir)
buton.pack(side=LEFT)
gui.mainloop()







