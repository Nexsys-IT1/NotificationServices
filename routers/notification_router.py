from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from services.sms_service import SMSService
from schemas.notification_request import NotificationRequest
from services.email_service import EmailService


router = APIRouter()


@router.post("/send-email")
async def send_email(
    request: NotificationRequest,
    db: Session = Depends(get_db)
):

    service = EmailService(db)

    await service.send_email(
        template_key=request.template_key,
        to_email=request.email,
        context=request.model_dump(exclude={"template_key", "email"})
    )

    return {"message": "Email sent successfully"}


@router.post("/send-sms")
async def send_sms(request: NotificationRequest):

    service = SMSService()

    await service.send_sms(
        to_number=request.phone_number,
        message="Your message here"
    )

    return {"message": "SMS sent successfully"}