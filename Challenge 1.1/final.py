from tkinter import *


root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.criando_botoes()
        root.mainloop()

# Aqui está o redimensionamento da Janela
    def tela(self):
        self.root.title("LGBM")
        self.root.configure(background='#1c1c1c')
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        self.root.maxsize(width= 900, height= 700)
        self.root.minsize(width= 500, height= 400)


# Aqui estão os frames
    def frames_da_tela(self):

# Aqui está o frame da coluna dos botões
        self.frame_1 = Frame(self.root)
        self.frame_1.place(relx= 0.01, rely=0.01, relwidth=0.2, relheight= 0.98)

# Aqui está o frame da visualização das tabelas
        self.frame_2 = Frame(self.root)
        self.frame_2.place(relx=0.25, rely=0.01, relwidth=0.74, relheight=0.98)

# Aqui estão os botões
    def criando_botoes(self):

# Aqui está o botão da tabela dos usuários
        self.bt_usuarios =  Button(self.frame_1, text= "Pontos Usuários")
        self.bt_usuarios.place(relx= 0.019, rely=0.01, relwidth=0.95, relheight= 0.07)

# Aqui está o botão da tabela dos setores
        self.bt_setores = Button(self.frame_1, text= "Pontos Setores")
        self.bt_setores.place(relx=0.019, rely=0.09, relwidth=0.95, relheight=0.07)

# Aqui está o botão da tabela do cadastro de funcionários
        self.bt_cadastro = Button(self.frame_1, text= "Cadastro de Funcionários")
        self.bt_cadastro.place(relx=0.019, rely=0.17, relwidth=0.95, relheight=0.07)

# Aqui está o botão de catalógo
        self.bt_catalogo = Button(self.frame_1, text="Catálogo de Phishing")
        self.bt_catalogo.place(relx=0.019, rely=0.25, relwidth=0.95, relheight=0.07)

# Aqui está o botão de configuracoes
        self.bt_configuracoes = Button(self.frame_1, text="Configurações")
        self.bt_configuracoes.place(relx=0.019, rely=0.92, relwidth=0.95, relheight=0.07)




Application()