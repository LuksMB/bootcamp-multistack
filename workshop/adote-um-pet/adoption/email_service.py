import email
from unicodedata import name


from django.core.mail import send_mail


def send_email_confirmation(adoption):
    about = "Adoção realizada com sucesso!"
    content = f"Parabéns por realizar a adoção do pet {adoption.pet.name} com o valor mensal de {adoption.value}"
    sender = "lucasmb.7@gmail.com"
    recipient = [adoption.email]
    send_mail(about, content, sender, recipient)
