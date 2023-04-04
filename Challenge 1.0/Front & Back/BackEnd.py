import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def enviar_email(destinatarios, assunto, mensagem, remetente, senha):
    try:
        msg = MIMEMultipart()
        msg['From'] = remetente
        msg['To'] = ", ".join(destinatarios)
        msg['Subject'] = assunto

        corpo_mensagem = mensagem
        msg.attach(MIMEText(corpo_mensagem, 'plain'))

        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(remetente, senha)
        smtp.sendmail(remetente, destinatarios, msg.as_string())
        smtp.quit()

        print("Email enviado com sucesso!")
    except Exception as ex:
        print("Não foi possível enviar o email. Erro:", str(ex))


def main():
    remetente = "seuemail@gmail.com"
    senha = "suasenha"

    destinatarios = ["email1@example.com", "email2@example.com"]
    assunto = "Urgente: Retomada do uso de máscaras em São Paulo"
    mensagem = """Será necessário a retomada da utilização em massa de máscara, em todos os estabelecimentos e transportes comerciais e públicos.

Clique no link abaixo para verificar a data de início no Estado de São Paulo.
https://www.saopaulo.sp.gov.br/"""

    enviar_email(destinatarios, assunto, mensagem, remetente, senha)


if __name__ == '__main__':
    main()
