import tkinter as tk

janela = tk.Tk()
janela.title("LGBM")

# criar o rótulo para o campo de entrada de e-mail e posicionar na coluna 0, linha 1
rotulo_email = tk.Label(janela, text="Destinatários:")
rotulo_email.grid(row=1, column=0, padx=5, pady=5)

# criar o campo de entrada de e-mail e posicionar na coluna 1, linha 1 com width=50 e height=3
endereco_email = tk.Text(janela, width=100, height=3)
endereco_email.grid(row=1, column=1, padx=5, pady=5)

# adicionar a frase de sombra no campo de entrada de e-mail
def on_focusin(event):
    if endereco_email.get("1.0", "end-1c") == "Insira os Endereços de E-mail dos Destinatários, Separados por Vírgula":
        endereco_email.delete("1.0", "end-1c")
        endereco_email.config(fg="black")

def on_focusout(event):
    if endereco_email.get("1.0", "end-1c") == "":
        endereco_email.insert("1.0", "Insira os Endereços de E-mail dos Destinatários, Separados por Vírgula")
        endereco_email.config(fg="gray")

endereco_email.insert("1.0", "Insira os Endereços de E-mail dos Destinatários, Separados por Vírgula")
endereco_email.config(fg="gray")
endereco_email.bind("<FocusIn>", on_focusin)
endereco_email.bind("<FocusOut>", on_focusout)


def enviar_email():
    destinatarios = endereco_email.get("1.0", "end-1c").split(",")
    Back.enviar_email(destinatarios)

# botão para enviar o e-mail e posicionar na coluna 1, linha 3
botao = tk.Button(janela, text="Enviar", command=enviar_email)
botao.grid(row=3, column=1, padx=5, pady=5)

janela.mainloop()
