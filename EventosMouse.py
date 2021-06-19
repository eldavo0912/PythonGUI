from tkinter import * 

def fazeralgo(a):

   print("oiiooi")


janela=Tk()
janela.title('oioi')


janela.bind("<Button-1>",fazeralgo) # Botão esquerdo
janela.bind("<Button-2>",fazeralgo) # Botão do meio
janela.bind("<Button-3>",fazeralgo) # Botão direito


janela.mainloop()