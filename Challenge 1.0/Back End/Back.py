import smtplib

# configurar servidor de e-mail e porta
smtp_server = "smtp.gmail.com"
smtp_port = 587

# credenciais de acesso à conta de e-mail
usuario = "seu_email@gmail.com"
senha = "sua_senha"

# criar objeto para conexão com o servidor de e-mail
conexao = smtplib.SMTP(smtp_server, smtp_port)

# estabelecer conexão segura com o servidor de e-mail
conexao.starttls()

# fazer login na conta de e-mail
conexao.login(usuario, senha)

# enviar mensagem de e-mail
assunto = "Assunto do e-mail"
corpo = mensagem.format(", ".join(enderecos_de_email))
destinatarios = enderecos_de_email

msg = f"Subject: {assunto}\n\n{corpo}"
conexao.sendmail(usuario, destinatarios, msg)

# encerrar conexão com o servidor de e-mail
conexao.quit()
