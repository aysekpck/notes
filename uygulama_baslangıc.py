#Uygulama_tkinter_başlagıç
"""
tkinter: Python'ın görsel arayüz oluşturma modülünün adıdır.
"""
#tkinter program şablonu:
"""
from tkinter import * 
pencere=Tk() #pencere adlı nesne oluşturdum
#grafiksel bileşenler yazılacak
mainloop() #sınırsız döngünün çalışması için mainloop() yazıyoruz.
"""
#Button()
"""
from tkinter import * 
pencere=Tk()
def clicked():
    print("YBS DOĞUŞ BURADA")
button1=Button(pencere)
#Button(sayfa_adı)
button1.config(text="Tıkla",bg="yellow",fg="black",command=clicked)
#command parametresi ile clicked adlı fonksiyona sinyal gönderiyor.
button1.pack() #pack() konumlandırmaya yarıyor
mainloop()
"""
#Button-diğer yöntem
"""
from tkinter import * 
pencere=Tk()
def clicked():
    print("YBS DOĞUŞ BURADA")
Button(pencere,text="Tıkla",bg="yellow",fg="black",command=clicked).pack()
mainloop()
"""
#Entry(sayfa_adı)
"""
from tkinter import * 
pencere=Tk()
Entry(pencere).pack()
mainloop()
"""
#Label(sayfa_adı)
from tkinter import * 
pencere=Tk()
Label(pencere,text="Sevilen bir bölüm YBS",bg="red",font=("Vertana",18)).pack()
mainloop()
#font(parametre1,parametre2): yazı şeklide, boyutu



    





