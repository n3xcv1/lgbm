from tkinter import *
import sqlite3
import pandas as pd

root = Tk()


#Criando conexão com o Banco de Dados
conexao = sqlite3.connect('banco.db')

cursor = conexao.cursor()

#Criando Tabela e Colunas do Banco de Dados
cursor.execute('''CREATE TABLE funcionarios (
    nome text,
    email text,
    setor text
    )
''')

conexao.commit()

conexao.close()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.criando_botoes()
        self.conexao_banco()
        self.criar_widgets()
        root.mainloop()

    #Redimensionamento da Janela
    def tela(self):
        self.root.title("LGBM")
        self.root.configure(background='black')
        self.root.geometry("3000x1200")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=400)

    # Criaçado de Frames para Introdução
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, background='#004B57')
        self.frame_1.place(relx=0.01, rely=0.01, relwidth=0.17, relheight=0.98)

        self.frame_2 = Frame(self.root, background='#004B57')
        self.frame_2.place(relx=0.25, rely=0.01, relwidth=0.74, relheight=0.98)

    #Janela Usuários
    #def abrir_janela_tusuarios(self):
        #nova_janela = Frame(self.frame_2, background='black')
        #nova_janela.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        #label = Label(nova_janela, text="Tabela Usuários")
        #label.pack(pady=50)

    # Janela Setores
    #def abrir_janela_tsetores(self):
       # nova_janela = Frame(self.frame_2, background='blue')
        #nova_janela.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
       #label = Label(nova_janela, text="Tabela Setores")
        #label.pack(pady=50)

    def conexao_banco(self):
        self.conexao = sqlite3.connect('banco.db')

    def salvar_dados(self):
        cursor = self.conexao.cursor()

        cursor.execute("INSERT INTO funcionarios VALUES (:nome, :email, :setor)",
                       {
                           'nome': self.nome_entry.get(),
                           'email': self.email_entry.get(),
                           'setor': self.setor_entry.get(),
                       }
                       )

        self.conexao.commit()

    def criar_widgets(self):
        #Cadastro de Nome do Funcionário
        self.lb_nome = Label(self.frame_2, text = "Nome do Funcionário")
        self.lb_nome.place(relx= 0.05, rely= 0.05)
        self.nome_entry = Entry (self.frame_2)
        self.nome_entry.place(relx= 0.25, rely= 0.05, relwidth= 0.5, relheight=0.031)

        # Cadastro do E-mail do Funcionário
        self.lb_email = Label(self.frame_2, text="E-mail do Funcionário")
        self.lb_email.place(relx=0.05, rely=0.1)
        self.email_entry = Entry(self.frame_2)
        self.email_entry.place(relx=0.25, rely=0.1, relwidth= 0.5, relheight=0.031)

        # Cadastro do Setor do Funcionário
        self.lb_setor = Label(self.frame_2, text="Setor do Funcionário")
        self.lb_setor.place(relx=0.05, rely=0.15)
        self.setor_entry = Entry(self.frame_2)
        self.setor_entry.place(relx=0.25, rely=0.15, relwidth= 0.5, relheight=0.031)

        # Botão Limpar
        self.bt_limpar = Button(self.frame_2, text="Limpar", background='white', bd=3)
        self.bt_limpar.place(relx=0.3, rely=0.6, relwidth=0.1)

        # Botão Salvar
        self.bt_salvar = Button(self.frame_2, text="Salvar", background='white', bd=3, command=self.salvar_dados)
        self.bt_salvar.place(relx=0.5, rely=0.6, relwidth=0.1)


    # Janela Catalogo
    #def abrir_janela_catalogo(self):
        #nova_janela = Frame(self.frame_2, background='yellow')
        #nova_janela.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        #label = Label(nova_janela, text="Tabela Catalogo")
        #label.pack(pady=50)

    #Janela Configurações
    #def abrir_janela_config(self):
        #nova_janela = Frame(self.frame_2, background='red')
        #nova_janela.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        #label = Label(nova_janela, text="Tabela Config")
        #label.pack(pady=50)

    # Criação de Botões
    def criando_botoes(self):
        self.bt_usuarios = Button(self.frame_1, text="Pontos Usuários", background='#daa520', bd=3)
        self.bt_usuarios.place(relx=0.019, rely=0.01, relwidth=0.97, relheight=0.07)

        #Botão Setores
        self.bt_setores = Button(self.frame_1, text="Pontos Setores", background='#daa520', bd=3)
        self.bt_setores.place(relx=0.019, rely=0.09, relwidth=0.97, relheight=0.07)

        # Botão Cadastro
        self.bt_cadastro = Button(self.frame_1, text="Cadastro de Funcionários", background='#daa520', bd=3, command=self.criar_widgets)
        self.bt_cadastro.place(relx=0.019, rely=0.17, relwidth=0.97, relheight=0.07)

        # Botão Catalogo
        self.bt_catalogo = Button(self.frame_1, text="Catálogo de Phishing", background='#daa520', bd=3,)
        self.bt_catalogo.place(relx=0.019, rely=0.25, relwidth=0.97, relheight=0.07)

        # Botão Config
        #self.bt_configuracoes = Button(self.frame_1, text="Configurações", background='#daa520', command=self.abrir_janela_config)
        #self.bt_configuracoes.place(relx=0.019, rely=0.92, relwidth=0.97, relheight=0.07)


Application()