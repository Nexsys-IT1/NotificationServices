from sqlalchemy.orm import Session
from jinja2 import Environment, FileSystemLoader, Template
from models.email_template import EmailTemplate


class EmailTemplateService:

    def __init__(self, db: Session):
        self.db = db
        self.layout_env = Environment(
            loader=FileSystemLoader("templates/layouts")
        )

    def get_template(self, template_key: str) -> EmailTemplate:

        template = (
            self.db.query(EmailTemplate)
            .filter(EmailTemplate.template_key == template_key)
            .first()
        )

        if not template:
            raise ValueError("Email template not found")

        return template

    def render_email(self, template_key: str, context: dict) -> str:

        db_template = self.get_template(template_key)

        body_html = Template(
            db_template.email_body
        ).render(**context)

        layout = self.layout_env.get_template("email_base.html")

        return layout.render(body_content=body_html)

    def render_pdf(self, template_key: str, context: dict) -> str:

        db_template = self.get_template(template_key)

        # If PDF not enabled
        if not db_template.has_pdf:
            return ""

        # If PDF body is empty or NULL
        if not db_template.pdf_body:
            raise ValueError("PDF body is missing in database.")

        body_html = Template(
            db_template.pdf_body
        ).render(**context)

        layout = self.layout_env.get_template("pdf_base.html")

        return layout.render(body_content=body_html)

