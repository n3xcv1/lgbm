from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.criando_botoes()
        root.mainloop()

    def tela(self):
        self.root.title("LGBM")
        self.root.configure(background='black')
        self.root.geometry("3000x1200")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=400)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, background='#004B57')
        self.frame_1.place(relx=0.01, rely=0.01, relwidth=0.17, relheight=0.98)

        self.frame_2 = Frame(self.root, background='#004B57')
        self.frame_2.place(relx=0.25, rely=0.01, relwidth=0.74, relheight=0.98)

    def abrir_janela_tusuarios(self):
        nova_janela = Frame(self.frame_2, background='black')
        nova_janela.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label = Label(nova_janela, text="Tabela Usuários")
        label.pack(pady=50)

    def abrir_janela_tsetores(self):
        nova_janela = Frame(self.frame_2, background='blue')
        nova_janela.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label = Label(nova_janela, text="Tabela Setores")
        label.pack(pady=50)

    def abrir_janela_cadastro(self):
        nova_janela = Frame(self.frame_2, background='white')
        nova_janela.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label = Label(nova_janela, text="Tabela Cadastro")
        label.pack(pady=50)

    def abrir_janela_catalogo(self):
        nova_janela = Frame(self.frame_2, background='yellow')
        nova_janela.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label = Label(nova_janela, text="Tabela Catalogo")
        label.pack(pady=50)

    def abrir_janela_config(self):
        nova_janela = Frame(self.frame_2, background='red')
        nova_janela.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label = Label(nova_janela, text="Tabela Config")
        label.pack(pady=50)

    def criando_botoes(self):
        self.bt_usuarios = Button(self.frame_1, text="Pontos Usuários", background='#daa520', command=self.abrir_janela_tusuarios)
        self.bt_usuarios.place(relx=0.019, rely=0.01, relwidth=0.97, relheight=0.07)

        self.bt_setores = Button(self.frame_1, text="Pontos Setores", background='#daa520', command=self.abrir_janela_tsetores)
        self.bt_setores.place(relx=0.019, rely=0.09, relwidth=0.97, relheight=0.07)

        self.bt_cadastro = Button(self.frame_1, text="Cadastro de Funcionários", background='#daa520', command=self.abrir_janela_cadastro)
        self.bt_cadastro.place(relx=0.019, rely=0.17, relwidth=0.97, relheight=0.07)

        self.bt_catalogo = Button(self.frame_1, text="Catálogo de Phishing", background='#daa520', command=self.abrir_janela_catalogo)
        self.bt_catalogo.place(relx=0.019, rely=0.25, relwidth=0.97, relheight=0.07)

        self.bt_configuracoes = Button(self.frame_1, text="Configurações", background='#daa520', command=self.abrir_janela_config)
        self.bt_configuracoes.place(relx=0.019, rely=0.92, relwidth=0.97, relheight=0.07)


Application()
