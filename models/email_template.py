from sqlalchemy import Column, Integer, String, Text, Boolean
from db.database import Base


class EmailTemplate(Base):

    __tablename__ = "email_templates"

    id = Column(Integer, primary_key=True, index=True)

    template_key = Column(String, unique=True, nullable=False)

    subject = Column(String, nullable=False)

    email_body = Column(Text, nullable=False)

    pdf_body = Column(Text, nullable=True)

    has_pdf = Column(Boolean, default=False)
