from tkinter import*
#concatenar nome e sobrenome
#criando janela

letras ="abcdefghijklmnopqrstuvwxyz"
caractere_valido = letras + letras.upper() + " "

#definição para juntar nomes
def concatenar():
    nome_completo = entry_nome.get() + " " + entry_sobrenome.get()
#apresenta a função
    label_completo["text"] = nome_completo.title()
    
janela=Tk()
janela.title("Revisão")
largura = 400
altura = 400

largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenheight()

posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

#label e entry
label_nome=Label(janela, text="Nome")
label_sobrenome=Label(janela,text="Sobrenome")
label_completo=Label(janela,text="Nome Completo")

entry_nome=Entry(janela)
entry_sobrenome=Entry(janela)

#botão é para mostrar e concatenar
button_apresentar=Button(janela, text="Mostrar",command=concatenar)
#O botão abaixo é um comando para fechar a janela
button_cancelar=Button(janela, text="fechar", command=janela.destroy)


#posicionamento

label_nome.grid(row=0,column=0)
label_sobrenome.grid(row=1,column=0)
label_completo.grid(row=2,column=0)
entry_nome.grid(row=0,column=1)
entry_sobrenome.grid(row=1,column=1)

button_apresentar.grid(row=3,column=0)
button_cancelar.grid(row=3,column=1)


janela.mainloop()
