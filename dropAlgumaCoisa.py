from tkinter import *

def comandomouse(event):
    parte.startX = event.x
    parte.startY = event.y

def mousemovimento(event):
    api = event.widget
    x= widget.winfo_x() - widget.startX + event.x
    y= widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

janela= Tk()


parte = Label(janela, bg= "purple" , width=50, height=10)
parte.place(x=30,y=30)

parte.bind("<Button-1>", comandomouse)
parte.bind("<Bl-Motion>", mousemovimento)




janela.mainloop()