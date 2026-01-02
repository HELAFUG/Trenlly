from email.message import EmailMessage

import aiosmtplib
from core.config import settings


async def send_email(recipient: str, sub: str, body: str) -> None:
    message = EmailMessage()
    message["From"] = settings.admin.email
    message["To"] = recipient
    message["Subject"] = sub
    message.set_content(body)

    await aiosmtplib.send(
        message,
        recipients=[recipient],
        sender=settings.admin.email,
        port=1025,
        hostname="localhost",
    )
