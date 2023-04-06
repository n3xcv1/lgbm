import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

# Configurar janela
window = tk.Tk()
window.title("Tabela Front End")

# Definir cores das colunas
member_color = "white"
area_color = "gray"
easy_color = "green"
medium_color = "blue"
hard_color = "orange"
insane_color = "red"
total_color = "black"  # Alterado para preto

# Configurar nomes das colunas com as cores
area_label = tk.Label(window, text="Area de Atuação", bg=area_color)
area_label.grid(row=0, column=0, padx=5, pady=5)

member_label = tk.Label(window, text="Integrantes", bg=member_color)
member_label.grid(row=0, column=1, padx=5, pady=5)

easy_label = tk.Label(window, text="Easy", bg=easy_color)
easy_label.grid(row=0, column=2, padx=5, pady=5)

medium_label = tk.Label(window, text="Medium", bg=medium_color)
medium_label.grid(row=0, column=3, padx=5, pady=5)

hard_label = tk.Label(window, text="Hard", bg=hard_color)
hard_label.grid(row=0, column=4, padx=5, pady=5)

insane_label = tk.Label(window, text="Insane", bg=insane_color)
insane_label.grid(row=0, column=5, padx=5, pady=5)

total_label = tk.Label(window, text="Total de Pontos Perdidos", bg=total_color, fg="white")  # Alterado para cor branca
total_label.grid(row=0, column=6, padx=5, pady=5)

# Configurar células da tabela com cores alternadas
labels = []
for i in range(1, 6):
    row = []
    for j in range(7):
        if j == 0:
            color = area_color
            if i == 1:
                text = "RH"
            elif i == 2:
                text = "CyberSecurity"
            elif i == 3:
                text = "Developers"
            elif i == 4:
                text = "Financeiro"
            else:
                text = "Complience"
        elif j == 1:
            color = member_color
            if i == 1:
                text = "Lucas de Brito"
            elif i == 2:
                text = "Mateus Andrade"
            elif i == 3:
                text = "Mateus Miranda"
            elif i == 4:
                text = "Bruno Neris"
            else:
                text = "Edward Snowden"
        elif j == 2:
            color = easy_color
            text = f"{i * j}"
        elif j == 3:
            color = medium_color
            text = f"{i * j * 2}"
        elif j == 4:
            color = hard_color
            text = f"{i * j * 3}"
        elif j == 5:
            color = insane_color
            text = f"{i * j * 4}"
        else:
            color = total_color
            text = f"{i * j * 5}"
        color = "white" if (i + j) % 2 == 0 else "lightgray"
        label = tk.Label(window, text=text, bg=color, fg="white" if color == "black" else "black")  # Alterado para cor branca nas células pretas
        label.grid(row=i, column=j, padx=5, pady=5)
        row.append(label)
    labels.append(row)

# Iniciar janela
window.mainloop()