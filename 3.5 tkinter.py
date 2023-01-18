from tkinter import *
import tkinter.filedialog
import datetime
from datetime import *

#akna seaded
aken = Tk()
aken.title('Dialoogiaknad')

aken.geometry("200x200")

def vali_fail():
    faili_tyyp = [('txt fail', '*.txt'), ('Kõik failid', '*')]
    nimi = tkinter.filedialog.Open(filetypes=faili_tyyp)
    valik = nimi.show()
    
    if valik != '':
        print(valik)
        


      

    laul = datetime.now().day
    f = open(valik, "r")
    jrk = 1
    for i in f:
            if jrk == laul:
                print(f"\nmangitav laulupala on {i}")
            jrk +=1


nupp1 = Button(aken, text = "Vali fail...", command = vali_fail).pack()

aken.mainloop()