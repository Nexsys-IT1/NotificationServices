from sqlalchemy.orm import Session
from jinja2 import Template, Environment, FileSystemLoader
from models.email_template import EmailTemplate


class EmailTemplateService:

    def __init__(self, db: Session):

        self.db = db

        self.layout_env = Environment(
            loader=FileSystemLoader("templates/layouts")
        )

    def get_template(self, template_key: str):

        template = (
            self.db.query(EmailTemplate)
            .filter(EmailTemplate.template_key == template_key)
            .first()
        )

        if not template:
            raise Exception("Template not found")

        return template


    def render_email(self, template_key: str, context: dict):

        db_template = self.get_template(template_key)

        # render DB body
        body_html = Template(
            db_template.email_body
        ).render(**context)

        # wrap with layout
        layout = self.layout_env.get_template(
            "email_base.html"
        )

        final_html = layout.render(
            body_content=body_html
        )

        return final_html


    def render_pdf(self, template_key: str, context: dict):

        db_template = self.get_template(template_key)

        if not db_template.has_pdf:
            return None

        body_html = Template(
            db_template.pdf_body
        ).render(**context)

        layout = self.layout_env.get_template(
            "pdf_base.html"
        )

        final_html = layout.render(
            body_content=body_html
        )

        return final_html
