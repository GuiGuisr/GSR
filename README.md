from imap_tools import MailBox, AND

usuario = "seu_email@gmail.com"
senha = "12345"

meu_email = MailBox("imap.gmail.com").login(usuario, senha)

lista_emails = meu_email.fetch(AND(from_="seu_email@gmail.com", subject="assunto_que_vc_deseja"))
for email in lista_emails:
    print(email.subject)
    print(email.text)
