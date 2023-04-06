import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
#
def send_email():
    # Obter informações do usuário
    email_user = email_entry.get()
    email_password = password_entry.get()
    email_send = send_to_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END)

    # Configurar email
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    # Adicionar mensagem
    msg.attach(MIMEText(message, 'plain'))

    # Conectar ao servidor SMTP e enviar email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)
    text = msg.as_string()
    server.sendmail(email_user, email_send, text)
    server.quit()

    # Limpar campos
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    send_to_entry.delete(0, tk.END)
    subject_entry.delete(0, tk.END)
    message_text.delete("1.0", tk.END)

# Configurar janela
window = tk.Tk()
window.title("Ferramenta de Disparos de Emails")

# Configurar labels e entry boxes
email_label = tk.Label(window, text="Seu email:")
email_label.grid(row=0, column=0)
email_entry = tk.Entry(window)
email_entry.grid(row=0, column=1)

password_label = tk.Label(window, text="Sua senha:")
password_label.grid(row=1, column=0)
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=1, column=1)

send_to_label = tk.Label(window, text="Enviar para:")
send_to_label.grid(row=2, column=0)
send_to_entry = tk.Entry(window)
send_to_entry.grid(row=2, column=1)

subject_label = tk.Label(window, text="Assunto:")
subject_label.grid(row=3, column=0)
subject_entry = tk.Entry(window)
subject_entry.grid(row=3, column=1)

message_label = tk.Label(window, text="Mensagem:")
message_label.grid(row=4, column=0)
message_text = tk.Text(window, height=10, width=50)
message_text.grid(row=4, column=1)

send_button = tk.Button(window, text="Enviar", command=send_email)
send_button.grid(row=5, column=0, columnspan=2)

# Iniciar janela
window.mainloop()