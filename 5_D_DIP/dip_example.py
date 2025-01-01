"""
D - Dependency Inversion Principle (DIP) - Princípio da Inversão da Depedência

Módulos de alto nível não devem depender diretamente dos módulos de baixo nível

"O Princípio da Inversão da Dependência (DIP) nos diz que os sistemas mais flexívei são aqueles em que as dependências do código-fonte referem-se apenas a abstrações, não a concreções."
"""

from abc import ABC, abstractmethod

# Interface de Notificação
class NotificacaoService(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass

# Implementação de Notificação via Email
class EmailService(NotificacaoService):
    def enviar(self, mensagem):
        print(f"Enviando e-mail com a mensagem: {mensagem}")

# Implementação de Notificação via SMS
class SMSService(NotificacaoService):
    def enviar(self, mensagem):
        print(f"Enviando SMS com a mensagem: {mensagem}")

# Classe Notificador que depende da abstração (NotificacaoService)
class Notificador:
    def __init__(self, notificacao_service: NotificacaoService):
        self.notificacao_service = notificacao_service  # Dependência injetada

    def enviar_notificacao(self, mensagem):
        self.notificacao_service.enviar(mensagem)

email_service = EmailService()
notificador_email = Notificador(email_service)
notificador_email.enviar_notificacao("Alerta por E-mail!")

sms_service = SMSService()
notificador_sms = Notificador(sms_service)
notificador_sms.enviar_notificacao("Alerta por SMS!")
