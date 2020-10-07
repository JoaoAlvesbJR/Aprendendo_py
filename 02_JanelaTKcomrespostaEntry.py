from tkinter import *
#sim ou não

janela = Tk()

janela.title =("Ensinamentos")

largura = 500
altura = 500

largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenheight()
posx = largura_screen/2 - largura/2 
posy = altura_screen/2 - altura/2


def executar():
    if pergunta.get()=="sim":             #get retorna uma informação.
        labelresposta=Label(janela, text="Você prestou atenção por isso aprendeu")
        labelresposta.grid(row=2,column=0)
    elif pergunta.get() == "não":
        labelrespostanao=Label(janela, text="Você nao prestou atenção por isso nao aprendeu")
        labelrespostanao.grid(row=2,column=0)
        


label_pergunta= Label(janela, text="Você aprendeu o conteudo das aulas?", font = "arial 12")
pergunta = Entry (janela)
botao = Button(janela, text="confirma", command=executar)
label_pergunta.grid(row=0, column=0
                    )
pergunta.grid(row=0,column=1)
botao.grid(row=1, column=0)


               


janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
            
janela.mainloop()
