from tkinter import*

def soman ():
    num1 = int(entry_n1.get())
    num2 = int(entry_n2.get())
    somanum = num1 + num2
    #set = define valor
    numero.set(str(somanum))
    

janela = Tk()
janela.title =("SOMA")

largura = 500
altura = 500

largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenheight()
posx = largura_screen/2 - largura/2 
posy = altura_screen/2 - altura/2

#StringVar = Usa essa função para armazenar o valor do objeto criado (type=str)
numero = StringVar()


label_n1=Label(janela,text="Numero1")
entry_n1=Entry(janela)
label_n2=Label(janela,text="Numero2")
entry_n2=Entry(janela)

#textvariable = Aceita uma variavel para exibir no label
Label(janela,textvariable=numero).grid(row=3,column=0)

botao_somar=Button(janela, text="somar", command=soman)

label_n1.grid(row=0,column=0)
entry_n1.grid(row=0,column=1)
label_n2.grid(row=1,column=0)
entry_n2.grid(row=1,column=1)
botao_somar.grid(row=2,column=1)


janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
            
janela.mainloop()

