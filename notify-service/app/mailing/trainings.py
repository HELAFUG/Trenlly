from .send_message import send_email


async def send_few_trainings_mail_notification(email):
    await send_email(
        email,
        "We have seen your activity,you're wanna give up?",
        "Your are not trained more than 3 times,just stay tuned",
    )
