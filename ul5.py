from tkinter import *

#akna seaded
aken = Tk()
aken.title('Käibemaksukalkulaator')
#aken.iconbitmap('favicon.ico')
aken.resizable(0, 0)

#funktsioonid

    
def arvuta():
    hind = float(sisestus.get())
    kaibe = var.get()
    tehe = hind*kaibe
    tehe2 = tehe+hind
    print(tehe,tehe2)
    valjund2.config(text=f"{tehe:.2f}€")
    valjund1.config(text=f"{tehe2:.2f}€")

#sildid
silt = Label(aken, text="Hind käibemaksuta: ")
silt.grid(row=0,column=0)

silt = Label(aken, text="Käibemaksumäär: ")
silt.grid(row=1,column=0)

silt = Label(aken, text="___________________________________________________________")
silt.grid(row=3,column=0,columnspan=10)

silt = Label(aken, text="Käibemaks: ")
silt.grid(row=4,column=0)

silt = Label(aken, text="Hind käibemaksuta: ")
silt.grid(row=5,column=0)

valjund1 = Label(aken, text="0.00€")
valjund1.grid(row=5,column=1)

valjund2 = Label(aken, text="0.00€")
valjund2.grid(row=4,column=1)

#sisestusväljad
sisestus = Entry(aken)
sisestus.grid(row=0,column=1)

#nupud
nupp1 = Button(aken, text="OK", width=10,command=arvuta)
nupp1.grid(row=6, column=5,padx=2,pady=2)

#valikukast
var = DoubleVar()
valikukast = Radiobutton(aken,text="9%", variable=var, value=0.09)
valikukast.grid(row=1,column=1)
valikukast = Radiobutton(aken,text="20%", variable=var, value=0.2)
valikukast.grid(row=2,column=1)

aken.mainloop()
