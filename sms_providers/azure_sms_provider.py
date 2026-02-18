from sms_providers.base_sms_provider import BaseSMSProvider
from azure.communication.sms import SmsClient
import os


class AzureSMSProvider(BaseSMSProvider):

    def __init__(self):
        connection_string = os.getenv("AZURE_SMS_CONNECTION_STRING")
        self.client = SmsClient.from_connection_string(connection_string)
        self.from_number = os.getenv("AZURE_SMS_FROM_NUMBER")


    async def send_sms(self, to_number: str, message: str):

        response = self.client.send(
            from_=self.from_number,
            to=[to_number],
            message=message,
            enable_delivery_report=True
        )

        # Optional logging
        for r in response:
            if r.successful:
                print(f"SMS sent to {to_number}")
            else:
                print(f"Failed to send SMS: {r.error_message}")
