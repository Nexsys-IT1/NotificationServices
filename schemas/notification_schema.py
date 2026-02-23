from pydantic import BaseModel, EmailStr
from typing import List, Dict, Any, Optional


class ChannelConfig(BaseModel):
    type: str                # "email" or "sms"
    provider: str            # "azure" or "aws"
    enabled: bool = True


class NotificationRequest(BaseModel):
    template_key: str
    channels: List[ChannelConfig]

    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None

    customer_name: str
    trip_details: Dict[str, Any]
    quotes: List[Dict[str, Any]]
