from typing import Optional
import boto3
import os
import base64


class AWSEmailProvider():

    def __init__(self):
        self.client = boto3.client(
            "ses",
            region_name=os.getenv("AWS_REGION"),
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        )

        self.sender = os.getenv("AWS_SENDER_EMAIL")


    async def send_email(
        self,
        to_email: str,
        subject: str,
        html_content: str,
        pdf_bytes: Optional[bytes] = None
    ):

        if pdf_bytes:
            # For attachments we must use RAW email
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            from email.mime.application import MIMEApplication

            msg = MIMEMultipart()
            msg["Subject"] = subject
            msg["From"] = self.sender
            msg["To"] = to_email

            msg.attach(MIMEText(html_content, "html"))

            part = MIMEApplication(pdf_bytes)
            part.add_header(
                "Content-Disposition",
                "attachment",
                filename="attachment.pdf"
            )
            msg.attach(part)

            self.client.send_raw_email(
                Source=self.sender,
                Destinations=[to_email],
                RawMessage={"Data": msg.as_string()},
            )

        else:
            self.client.send_email(
                Source=self.sender,
                Destination={"ToAddresses": [to_email]},
                Message={
                    "Subject": {"Data": subject},
                    "Body": {"Html": {"Data": html_content}},
                },
            )
