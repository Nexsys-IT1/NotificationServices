from abc import ABC, abstractmethod
from typing import Optional


class BaseEmailProvider(ABC):

    @abstractmethod
    async def send_email(
        self,
        to_email: str,
        subject: str,
        html_content: str,
        pdf_bytes: Optional[bytes] = None
    ):
        pass
