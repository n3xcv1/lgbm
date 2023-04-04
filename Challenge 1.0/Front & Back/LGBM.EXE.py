import tkinter as tk
import threading
import BackEnd

# criar a janela e definir o tamanho e cor de fundo
janela = tk.Tk()
janela.title("LGBM")
janela.geometry("1100x150")
janela.configure(bg="#F0F0F0")

# criar o rótulo para o campo de entrada de e-mail e posicionar na coluna 0, linha 1
rotulo_email = tk.Label(janela, text="Destinatários:", font=("Helvetica", 14), bg="#F0F0F0")
rotulo_email.grid(row=1, column=0, padx=5, pady=5)

# criar o campo de entrada de e-mail e posicionar na coluna 1, linha 1 com width=50 e height=3
endereco_email = tk.Text(janela, width=100, height=3, font=("Helvetica", 12))
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

# criar o botão de envio de e-mail e posicionar na coluna 1, linha 4 com width=10
botao_enviar = tk.Button(janela, text="Enviar", width=10, font=("Helvetica", 12), bg="#4CAF50", fg="white", command=lambda: threading.Thread(target=BackEnd.enviar_email, args=(endereco_email.get("1.0", "end-1c").split(","), BackEnd.assunto, BackEnd.mensagem)).start() if endereco_email.get("1.0", "end-1c").strip() != "" else None)
botao_enviar.grid(row=4, column=1, padx=5, pady=5)

# iniciar a janela
janela.mainloop()
