# import os
# from sms_providers.aws_sns_provider import AWSSNSProvider


# def get_sms_provider():

#     provider = os.getenv("SMS_PROVIDER", "azure").lower()

#     if provider == "azure":
#         return aws()

#     elif provider == "aws":
#         return AWSSNSProvider()

#     else:
#         raise Exception("Invalid SMS_PROVIDER value")
