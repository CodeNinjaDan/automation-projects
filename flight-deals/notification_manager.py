import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

class NotificationManager:

    def __init__(self):
        self.account_sid = os.getenv("ACCOUNT_SID")
        self.auth_token = os.getenv("AUTH_TOKEN")
        self.whatsapp_sender = os.getenv("WHATSAPP_SENDER")
        self.whatsapp_receiver = os.getenv("WHATSAPP_RECEIVER")
        self.client = Client(self.account_sid, self.auth_token)


    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=self.whatsapp_sender,
            body=message_body,
            to=self.whatsapp_receiver
        )
        print(message.sid)
