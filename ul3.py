#markus pilv
from tkinter import *

aken = Tk()
aken.resizable(0, 0)
aken.iconbitmap('a.ico')
aken.configure(background='black')

tekst = Label(aken, bg="black", text="Nimi: Markus Pilv\nit22\n2023", fg="red", font="Tahoma 12 bold italic", padx=20, pady=20)
tekst.pack()

aken.mainloop()

