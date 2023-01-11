#markus pilv


from tkinter import *

#akna seaded
aken = Tk()
aken.title('Joonistamine')


#lõuendi loomine
louend = Canvas(aken, width=500, height=300)
louend.pack()

#kujundite loomine
# 200=vasak start 200=kui korge 20=vasak lopp 20=pikslid ylevalt

louend.create_rectangle(500, 300 ,0,0, fill="red",width=0 )
louend.create_rectangle(500, 120, 0, 170, fill="white",width=0 )
louend.create_rectangle(100, 0, 150, 300, fill="white",width=0 )



aken.mainloop()