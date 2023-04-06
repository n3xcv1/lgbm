from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
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
        self.frame_1 = Frame(self.root)
        self.frame_1.place(relx= 0.01, rely=0.01, relwidth=0.2, relheight= 0.98)

        self.frame_2 = Frame(self.root)
        self.frame_2.place(relx=0.25, rely=0.01, relwidth=0.74, relheight=0.98)
# Aqui está os botões


Application()