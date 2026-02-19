from sqlalchemy.orm import Session
from services.email_template_service import EmailTemplateService
from services.pdf_service import generate_pdf_from_html
from email_providers.provider_factory import get_email_provider
import os

class EmailService:

    def __init__(self, db: Session, provider_name: str = None):

        self.template_service = EmailTemplateService(db)
        self.provider = get_email_provider(provider_name)


    def attach_logos(self, context):
        BASE_DIR = os.getcwd().replace("\\", "/")
        print("BASE_DIR:", os.getcwd())

        LOGO_MAP = {
            "RAKINSURANCE": "rak.png",
            "GIG": "gig.png",
            "AIG": "aig.png"
        }

        for quote in context.get("quotes", []):
            insurer = insurer = quote.get("insurer", {}).get("name")
            logo_file = LOGO_MAP.get(insurer)

            if logo_file:
                quote["logo_path"] = f"file:///{BASE_DIR}/static/logos/{logo_file}"
            else:
                quote["logo_path"] = None


    async def send_email(
        self,
        template_key: str,
        to_email: str,
        context: dict
    ):

        template = self.template_service.get_template(template_key)

        email_html = self.template_service.render_email(
            template_key,
            context
        )

        pdf_bytes = None

        if template.has_pdf:

            self.attach_logos(context)

            pdf_html = self.template_service.render_pdf(
                template_key,
                context
            )

            pdf_bytes = generate_pdf_from_html(pdf_html)

        await self.provider.send_email(
            to_email=to_email,
            subject=template.subject,
            html_content=email_html,
            pdf_bytes=pdf_bytes
        )
