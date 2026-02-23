from sqlalchemy.orm import Session
from services.templates.email_template_service import EmailTemplateService
from services.pdf.pdf_service import PDFService
from providers.email.provider_factory import EmailProviderFactory


class EmailChannel:
    """
    Handles complete email notification workflow.
    """

    def __init__(self, db: Session, provider_name: str):
        self.template_service = EmailTemplateService(db)
        self.pdf_service = PDFService()
        self.provider = EmailProviderFactory.get_provider(provider_name)

    async def send(
        self,
        template_key: str,
        to_email: str,
        context: dict,
    ) -> None:

        template = self.template_service.get_template(template_key)

        # Render email HTML
        email_html = self.template_service.render_email(
            template_key, context
        )

        pdf_bytes = None

        if template.has_pdf:
            pdf_html = self.template_service.render_pdf(
                template_key, context
            )
            if not pdf_html:
                raise ValueError("PDF HTML content is empty")
            
            pdf_bytes = await self.pdf_service.generate_pdf_from_html(pdf_html)

        await self.provider.send_email(
            to_email=to_email,
            subject=template.subject,
            html_content=email_html,
            pdf_bytes=pdf_bytes,
        )
