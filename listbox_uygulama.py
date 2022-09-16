#Listbox uygulaması
#İngilizce-Tğrkçe çeviri ypan basit sözlük uygulaması
from tkinter import *
gui=Tk()
gui.title("Sözlük Program")
#Listbox 1 nesnesi tanımlandı ve yerleştirildi
lbox1=Listbox(gui) 
lbox1.grid(row=0,column=0)
#Listbox 2 nesnesi tanımlandı ve yerleştirildi
lbox2=Listbox(gui) 
lbox2.grid(row=0,column=1)
#lbox1 nesnesine eleman ekleme
lbox1.insert(END,"İngilizce")
eng=["one","two","three","four","five"]
for i in eng:
    lbox1.insert(END,i)
#lbox2 nesnesine eleman eklema
lbox2.insert(END,"Türkçe")
trk=["bir","iki","üç","dört","beş"]
for i in trk:
    lbox2.insert(END,i)
gui.mainloop()    
