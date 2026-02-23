from sqlalchemy.orm import Session
from schemas.notification_schema import NotificationRequest
from services.channels.email_channel import EmailChannel
from services.assets.logo_service import LogoService


class NotificationService:
    def __init__(self, db: Session):
        self.db = db
        self.logo_service = LogoService() 

    async def send_notification(self, request: NotificationRequest) -> None:

        # Prepare template context
        context = request.model_dump(
            exclude={"channels", "email", "phone_number"}
        )

        context = self.logo_service.attach_logos(context)
        for channel in request.channels:

            if not channel.enabled:
                continue

            if channel.type.lower() == "email":
                await self._handle_email(channel, request, context)

    async def _handle_email(self, channel, request, context) -> None:

        if not request.email:
            raise ValueError("Email is required for email channel")

        email_channel = EmailChannel(
            db=self.db,
            provider_name=channel.provider,
        )

        await email_channel.send(
            template_key=request.template_key,
            to_email=request.email,
            context=context,
        )
