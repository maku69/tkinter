from tkinter import *
import tkinter.filedialog
import datetime
from datetime import *

#akna seaded
aken = Tk()
aken.title('Dialoogiaknad')

aken.geometry("250x200")

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
                valjund.config(text="Vastama tuleb "+i)
            jrk +=1


nupp1 = Button(aken, text = "Vali fail...", command = vali_fail)
nupp1.grid(row=1,column=2)

silt = Label(aken, text="Kes vastama tuleb:")
silt.grid(row=1,column=0)

valjund = Label(aken, text="Vastama tuleb ")
valjund.grid(row=3)

aken.mainloop()