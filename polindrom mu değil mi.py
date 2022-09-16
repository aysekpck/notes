#simpledialog ve messagebox uygulaması
"""
Diyolog penceresinden girilen bir metinsel ifadenin
palindrom olup olmadığını sorgulayan program
"""
from tkinter import *
import tkinter.messagebox as msj
from tkinter import simpledialog

gui=Tk()
#pencereden girilecek string "s" de tutulacak
s=simpledialog.askstring("Palindrom mu?","Kelime:", parent=gui)
#eğer girilen kelime palindrom ise
if s==''.join(reversed(s)):
    msj.showinfo(title=s,message="Evet Palindrom")
else:
    msj.showwarning(title=s,message="Palindrom Değil !!")
gui.mainloop()
