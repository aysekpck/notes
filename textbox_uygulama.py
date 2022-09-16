#textbox()- scrollbox()
#text kutusu oluşturma
from tkinter import *
form=Tk()
textbox=Text(form,bg="black",fg="white",height=15, width=40)
textbox.pack()
siir="""Ağlasam sesimi duyar mısınız,
Mısralarımda;
Dokunabilir misiniz,
Gözyaşlarıma, ellerinizle?

Bilmezdim şarkıların bu kadar güzel,
Kelimelerinse kifayetsiz olduğunu
Bu derde düşmeden önce.

Bir yer var, biliyorum;
Her şeyi söylemek mümkün;
Epeyce yaklaşmışım, duyuyorum;
Anlatamıyorum."""
#a=textbox.get(1.0,END)
textbox.insert(END,siir)
form.mainloop()






















