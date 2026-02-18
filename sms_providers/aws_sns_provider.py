from sms_providers.base_sms_provider import BaseSMSProvider
import boto3
import os


class AWSSNSProvider(BaseSMSProvider):

    def __init__(self):
        self.client = boto3.client(
            "sns",
            region_name=os.getenv("AWS_REGION"),
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        )


    async def send_sms(self, to_number: str, message: str):

        self.client.publish(
            PhoneNumber=to_number,
            Message=message
        )
