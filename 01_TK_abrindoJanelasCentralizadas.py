from tkinter import *
#sim ou não

#chama módulo Tk
janela = Tk()

#titulo da janela
janela.title =("Ensinamentos")
#dimensão da janela
largura = 350 #definido a largura do formulario
altura = 350 #definido a altura do formulario

#resolução do sistema
largura_screen = janela.winfo_screenwidth()#retorna o tamanho real da tela do seu pc
altura_screen = janela.winfo_screenheight()#retorna o tamanho real da tela do seu pc | centraliza o tamanho da sua janela

#posição da janela
posx = largura_screen/2 - largura/2 #calculo para centralizar a largura do meio
posy = altura_screen/2 - altura/2 #calculo para centralizar a altura do meio 

#definir a geometria
janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy)) #passando as posições definidas para a janela
            
#para deixar a janela aberta
janela.mainloop()
