import os
from email_providers.azure_email_provider import AzureEmailProvider
from email_providers.aws_email_provider import AWSEmailProvider


def get_email_provider():

    provider = os.getenv("EMAIL_PROVIDER", "azure").lower()

    if provider == "azure":
        return AzureEmailProvider()

    elif provider == "aws":
        return AWSEmailProvider()

    else:
        raise Exception("Invalid EMAIL_PROVIDER value")
