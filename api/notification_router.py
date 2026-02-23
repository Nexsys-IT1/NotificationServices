from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.notification_schema import NotificationRequest
from services.notification_service import NotificationService
from db.database import get_db

router = APIRouter()


@router.post("/send-notification")
async def send_notification(
    request: NotificationRequest,
    db: Session = Depends(get_db),
):
    service = NotificationService(db)
    await service.send_notification(request)

    return {"message": "Notification sent successfully"}
