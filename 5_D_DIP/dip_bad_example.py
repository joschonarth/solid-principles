class Notificador:
    def __init__(self):
        # Dependência direta do serviço de e-mail
        self.email_service = EmailService()

    def enviar_notificacao(self, mensagem):
        self.email_service.enviar_email(mensagem)

class EmailService:
    def enviar_email(self, mensagem):
        print(f"Enviando e-mail com a mensagem: {mensagem}")

class SMSService:
    def enviar(self, mensagem):
        print(f"Enviando SMS com a mensagem: {mensagem}")

notificador = Notificador()
notificador.enviar_notificacao("Alerta importante!")
