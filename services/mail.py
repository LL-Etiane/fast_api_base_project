from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from app import settings
from pathlib import Path
from fastapi.templating import Jinja2Templates
from typing import Dict, Optional

class MailService:
    def __init__(self):
        template_folder = settings.BASE_DIR / "templates/mails"
        if not template_folder.is_dir():
            raise ValueError(f"TEMPLATE_FOLDER path '{template_folder}' does not point to a directory")
    
        self.conf = ConnectionConfig(
            MAIL_USERNAME=settings.mail_username,
            MAIL_PASSWORD=settings.mail_password,
            MAIL_FROM=settings.mail_from,
            MAIL_PORT=settings.mail_port,
            MAIL_SERVER=settings.mail_server,
            MAIL_STARTTLS=True,
            MAIL_SSL_TLS=False,
            USE_CREDENTIALS=True,
            TEMPLATE_FOLDER=template_folder
        )
        self.mail = FastMail(self.conf)
        self.templates = Jinja2Templates(directory=str(self.conf.TEMPLATE_FOLDER))

    async def send_email(
            self, 
            email: str, 
            subject: str, 
            body: Optional[str] = None,
            template_name: Optional[str] = None,
            context: Optional[Dict] = None
        ) -> None:
        if template_name and context:
            template = self.templates.get_template(template_name)
            body = template.render(**context)
        elif not body:
            raise ValueError("You must provide a body or a template_name and context")

        message = MessageSchema(
            subject=subject,
            recipients=[email],
            body=body,
            subtype="html"
        )
        await self.mail.send_message(message)
