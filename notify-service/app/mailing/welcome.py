from .send_message import send_email


async def send_welcome_email(email) -> None:
    await send_email(
        recipient=email, sub="Welcome To Trenlly!", body="Thank you for joining us!"
    )
