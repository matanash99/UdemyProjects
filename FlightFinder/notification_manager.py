import requests
from twilio.rest import Client
import smtplib

account_sid = 'AC83e859e340a210486b25ce6245083f13'
auth_token = '52fc5a23b32f814d68f3d59719b0bb8c'
client = Client(account_sid, auth_token)

my_email = "mataniwani1999@gmail.com"
password = "spbp hiex aetm oquh"




class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def notify(self, city):
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body= f"Price changed for city: {city}, check sheet to see change.",
            to='whatsapp:+972548154767'
        )
        print(message.sid)


