#front end final

import tkinter as tk

# criar janela
root = tk.Tk()
root.title("Tabela")

# criar labels para as colunas
area_label = tk.Label(root, text="Area", width=15, font="bold", background="yellow")
pontuacao_label = tk.Label(root, text="Pontuação", width=15, font="bold", background="black", foreground="white")
situacao_label = tk.Label(root, text="Situação", width=15, font="bold", background="white")

# posicionar labels das colunas
area_label.grid(row=0, column=0)
pontuacao_label.grid(row=0, column=1)
situacao_label.grid(row=0, column=2)

# criar labels para os dados
matematica_area = tk.Label(root, text="RH", width=15)
matematica_pontuacao = tk.Label(root, text="320", width=15,)
matematica_situacao = tk.Label(root, text="Preocupante", width=15)

portugues_area = tk.Label(root, text="CyberSecurity", width=15)
portugues_pontuacao = tk.Label(root, text="900", width=15)
portugues_situacao = tk.Label(root, text="Seguro", width=15)

ciencias_area = tk.Label(root, text="Developers", width=15)
ciencias_pontuacao = tk.Label(root, text="750", width=15,)
ciencias_situacao = tk.Label(root, text="Seguro", width=15)

historia_area = tk.Label(root, text="Financeiro", width=15)
historia_pontuacao = tk.Label(root, text="890", width=15)
historia_situacao = tk.Label(root, text="Seguro", width=15)

geografia_area = tk.Label(root, text="Complience", width=15)
geografia_pontuacao = tk.Label(root, text="520", width=15)
geografia_situacao = tk.Label(root, text="Instavel", width=15)

# posicionar labels dos dados
matematica_area.grid(row=1, column=0)
matematica_pontuacao.grid(row=1, column=1)
matematica_situacao.grid(row=1, column=2)

portugues_area.grid(row=2, column=0)
portugues_pontuacao.grid(row=2, column=1)
portugues_situacao.grid(row=2, column=2)

ciencias_area.grid(row=3, column=0)
ciencias_pontuacao.grid(row=3, column=1)
ciencias_situacao.grid(row=3, column=2)

historia_area.grid(row=4, column=0)
historia_pontuacao.grid(row=4, column=1)
historia_situacao.grid(row=4, column=2)

geografia_area.grid(row=5, column=0)
geografia_pontuacao.grid(row=5, column=1)
geografia_situacao.grid(row=5, column=2)

# iniciar loop da janela
root.mainloop()