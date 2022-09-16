#tkinter iletişim kutuları
"""
DİYALOG LETİŞİM PENCERE MODÜLLERİ:
-tkinter.messagebox: kullanıcıya bilgi veren ya da
onay alan mesaj dialog penceresidir.
 tkinter.messagebox.metodadı(başlık,mesaj)
 -askquestion : Mesaj penceresinde Yes/No butonları ve soru işareti simgesi
 bulunur.
"""

import tkinter.messagebox
isEvet=tkinter.messagebox.askquestion(title="Question",message="Eminmisin")
print(isEvet)

"""
import tkinter.messagebox as msj
msj.askyesno(title="Yes-No",message="Evet mi? Hayır mı?")
"""
"""
import tkinter.messagebox as msj
msj.askyesnocancel(title="Yes-No-Cancel",message="Evet mi? Hayır mı? İptal mi?")
"""
"""
import tkinter.messagebox as msj
msj.askokcancel(title="Ok-Cancel",message="Tamam mı?İptal mi?")
"""
import tkinter.messagebox as msj
msj.askretrycancel(title="Retry-Cancel",message="Tekrar dene-İptal")








