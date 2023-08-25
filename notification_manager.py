from twilio.rest import Client



TWILIO_SID = "ACf0d223f90f6a94b482ecbb7ef871acb4"
TWILIO_AUTH_TOKEN = "214bb300143bdf1de7afadf3108e4a24"
TWILIO_VIRTUAL_NUMBER = "+16189958701"
TWILIO_VERIFIED_NUMBER = YOUR PHONE NUMBER


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )

        print(message.sid)
