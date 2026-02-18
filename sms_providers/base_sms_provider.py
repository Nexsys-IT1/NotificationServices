from abc import ABC, abstractmethod


class BaseSMSProvider(ABC):

    @abstractmethod
    async def send_sms(
        self,
        to_number: str,
        message: str
    ):
        pass
