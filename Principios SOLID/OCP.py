"""
OCP/ Abierto-Cerrado

"""

from abc  import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass

class AlertSms(NotificationService):
    def send(self, message):
        print(f"Sending Sms: {message}")

class AlertEmail(NotificationService):
    def send(self, message):
        print(f"Sending Email :{message}")
