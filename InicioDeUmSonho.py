from tkinter import*

#define classes
class Cliente:
    def __init__(self, razao_social, nome_fantasia, cnpj, inscricao_estadual, inscricao_municipal, rua, numero, complemento, bairro, municipio, uf, cep, telefone, whatsapp, celular, url, email):
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.cpnj = cnpj
        self.inscricao_estadual = inscricao_estadual
        self.inscricao_municipal = inscricao_municipal
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.municipio = municipio
        self.uf = uf
        self.cep = cep
        self.telefone = telefone
        self.whatsapp = whatsapp
        self.celular = celular
        self.url = url
        self.email = email
#define metodos
    def inserir(self):
        pass
    def editar(self):
        pass
    def excluir(self):
        pass
    def consultar(self):
        pass
    def listar(self):
        pass
#janela
janela = Tk()
janela.title =("Ensinamentos")
janela.geometry("1000x1000+250+250")
#Label
label_razao_social = Label(janela, text="Razão Social")
label_nome_fantasia = Label(janela, text="Nome Fantasia")
label_cpnj = Label(janela, text="CNPJ")
label_inscricao_estadual = Label(janela, text="Inscrição Estadual")
label_inscricao_municipal = Label(janela, text="Inscrição Municipal")
label_rua = Label(janela, text="Rua")
label_numero = Label(janela, text="Numero")
label_complemento = Label(janela, text="Numero")
label_bairro = Label(janela, text="Bairro")
label_municipio = Label(janela, text="Municipio")
label_uf = Label(janela, text="UF")
label_cep = Label(janela, text="CEP")
label_telefone = Label(janela, text="Telefone")
label_whatsapp = Label(janela, text="Whatsapp")
label_celular = Label(janela, text="Celular")
label_url = Label(janela, text="URL")
label_email = Label(janela, text="E-mail")
#entry
entry_razao_social = Entry(janela)
entry_nome_fantasia = Entry(janela)
entry_cpnj = Entry(janela)
entry_inscricao_estadual = Entry(janela)
entry_inscricao_municipal = Entry(janela)
entry_rua = Entry(janela)
entry_numero = Entry(janela)
entry_complemento = Entry(janela)
entry_bairro = Entry(janela)
entry_municipio = Entry(janela)
entry_uf = Entry(janela)
entry_cep = Entry(janela)
entry_telefone = Entry(janela)
entry_whatsapp = Entry(janela)
entry_celular = Entry(janela)
entry_url = Entry(janela)
entry_email = Entry(janela)
#geometria
label_razao_social.grid(row=0,column=0)
label_nome_fantasia.grid(row=1,column=0)
label_cpnj.grid(row=2,column=0)
label_inscricao_estadual.grid(row=3,column=0)
label_inscricao_municipal.grid(row=4,column=0)
label_rua.grid(row=5,column=0)
label_numero.grid(row=6,column=0)
label_complemento.grid(row=7,column=0)
label_bairro.grid(row=8,column=0)
label_municipio.grid(row=9,column=0)
label_uf.grid(row=10,column=0)
label_cep.grid(row=11,column=0)
label_telefone.grid(row=12,column=0)
label_whatsapp.grid(row=13,column=0)
label_celular.grid(row=14,column=0)
label_url.grid(row=15,column=0)
label_email.grid(row=16,column=0)
entry_razao_social.grid(row=0,column=1)
entry_nome_fantasia.grid(row=1,column=1)
entry_cpnj.grid(row=2,column=1)
entry_inscricao_estadual.grid(row=3,column=1)
entry_inscricao_municipal.grid(row=4,column=1)
entry_rua.grid(row=5,column=1)
entry_numero.grid(row=6,column=1)
entry_complemento.grid(row=7,column=1)
entry_bairro.grid(row=8,column=1)
entry_municipio.grid(row=9,column=1)
entry_uf.grid(row=10,column=1)
entry_cep.grid(row=11,column=1)
entry_telefone.grid(row=12,column=1)
entry_whatsapp.grid(row=13,column=1)
entry_celular.grid(row=14,column=1)
entry_url.grid(row=15,column=1)
entry_email.grid(row=16,column=1)
#botão
button_salvar = Button(janela, text="Salvar")
#geometria botão
button_salvar.grid(row=17,column=0)



janela.mainloop()



    
        
