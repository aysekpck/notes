#scrollbar
from tkinter import *
form=Tk()
S=Scrollbar(form) # kaydırma çubuğu
T=Text(form, height=4,width=50) #çok satırlı metinin kontrolü
S.pack(side=RIGHT,fill=Y) #kontrol bileşenlerinin yönünü belirler
T.pack(side=LEFT,fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
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
T.insert(END,siir)
mainloop()
