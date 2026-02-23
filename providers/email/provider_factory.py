from providers.email.azure_provider import AzureEmailProvider
#from providers.email.aws_provider import AWSEmailProvider


class EmailProviderFactory:

    @staticmethod
    def get_provider(provider_name: str):

        provider = provider_name.lower()

        if provider == "azure":
            return AzureEmailProvider()

        # if provider == "aws":
        #     return AWSEmailProvider()

        raise ValueError("Unsupported email provider")
