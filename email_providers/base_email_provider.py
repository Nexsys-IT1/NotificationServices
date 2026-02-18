from abc import ABC, abstractmethod

class BaseEmailProvider(ABC):

    @abstractmethod
    async def send_email(self, to_email: str, subject: str, html_content: str, pdf_bytes: bytes = None):
        pass
