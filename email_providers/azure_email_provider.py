from azure.communication.email import EmailClient
from .base_email_provider import BaseEmailProvider
import os
import base64
from dotenv import load_dotenv

load_dotenv()

class AzureEmailProvider(BaseEmailProvider):

    def __init__(self):
        self.connection_string = os.getenv("AZURE_EMAIL_CONNECTION_STRING")
        self.sender = os.getenv("AZURE_SENDER_EMAIL")
        self.client = EmailClient.from_connection_string(self.connection_string)

    async def send_email(self, to_email, subject, html_content, pdf_bytes=None):

        message = {
            "senderAddress": self.sender,
            "recipients": {"to": [{"address": to_email}]},
            "content": {
                "subject": subject,
                "html": html_content
            }
        }

        if pdf_bytes:
            encoded_pdf = base64.b64encode(pdf_bytes).decode()

            message["attachments"] = [{
                "name": "QuoteComparison.pdf",
                "contentType": "application/pdf",
                "contentInBase64": encoded_pdf
            }]

        poller = self.client.begin_send(message)
        poller.result()
