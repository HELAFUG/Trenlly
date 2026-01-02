from .send_message import send_email


async def send_login_email(email):
    await send_email(
        recipient=email,
        sub="We see some activity on your account",
        body="Some activity has been detected on your account. Please check your account for any suspicious activity.",
    )
