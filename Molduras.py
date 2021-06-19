from tkinter import *
from tkinter.font import Font

janela = Tk()

mold = Frame(janela)  #serve como uma grde onde prende os elementos
mold.pack()


Button(mold,text="W",width=3,font=("ds-digital",18)).pack(side=TOP)
Button(mold,text="S",width=3,font=("ds-digital",18)).pack(side=LEFT)
Button(mold,text="A",width=3,font=("ds-digital",18)).pack(side=LEFT)
Button(mold,text="D",width=3,font=("ds-digital",18)).pack(side=LEFT)



janela.mainloop()