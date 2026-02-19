from pydantic import BaseModel, EmailStr
from typing import List, Dict, Any


class NotificationRequest(BaseModel):

    template_key: str
    email: EmailStr
    service: str

    customer_name: str
    trip_details: Dict[str, Any]
    quotes: List[Dict[str, Any]]