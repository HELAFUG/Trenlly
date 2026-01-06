from .send_message import send_email


async def overdue_goals_mail(email):
    await send_email(
        email, "Overdue Goals", "You have overdue goals,check it in Trenlly"
    )
