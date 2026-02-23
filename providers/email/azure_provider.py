import os
import base64
from azure.communication.email import EmailClient


class AzureEmailProvider:

    def __init__(self):
        self.connection_string = os.getenv(
            "AZURE_EMAIL_CONNECTION_STRING"
        )
        print("AZURE_EMAIL_CONNECTION_STRING:", os.getenv("AZURE_EMAIL_CONNECTION_STRING"))
        self.sender = os.getenv("AZURE_SENDER_EMAIL")

        self.client = EmailClient.from_connection_string(
            self.connection_string
        )

    async def send_email(
        self,
        to_email: str,
        subject: str,
        html_content: str,
        pdf_bytes: bytes | None = None,
    ) -> None:

        message = {
            "senderAddress": self.sender,
            "recipients": {"to": [{"address": to_email}]},
            "content": {
                "subject": subject,
                "html": html_content,
            },
        }

        if pdf_bytes:
            encoded_pdf = base64.b64encode(pdf_bytes).decode()

            message["attachments"] = [{
                "name": "QuoteComparison.pdf",
                "contentType": "application/pdf",
                "contentInBase64": encoded_pdf,
            }]

        poller = self.client.begin_send(message)
        poller.result()
