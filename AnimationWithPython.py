from tkinter import *
import time



janela=Tk()
janela.title("Descanço de Tela")


ALTURA = 500
LARGURA =500
eixoXvelo= 2
eixoYvelo= 1

janela.geometry("500x500")
tela= Canvas(janela, width=499, height=499)
tela.pack()

imgFundo = PhotoImage(file="espaco.png")
TelaDeFundo = tela.create_image(0,0,image=imgFundo,anchor=NW)

img = PhotoImage(file='terra.png',)
minhaimagem = tela.create_image(0 ,8 , image = img, anchor=NW)


while True:
    
    coordenadas = tela.coords(minhaimagem)
    print(coordenadas)
    if(coordenadas[0] >= LARGURA or coordenadas[0]<0):
        eixoXvelo=-eixoXvelo
    if(coordenadas[1] >= ALTURA or coordenadas[1] < 0):
        eixoYvelo = -eixoYvelo

    tela.move(minhaimagem, eixoXvelo,eixoYvelo)
    janela.update()
    time.sleep(.02)
    

janela.mainloop()