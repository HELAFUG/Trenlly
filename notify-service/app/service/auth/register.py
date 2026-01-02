from core.config import settings
from faststream.kafka import KafkaRouter
from mailing import send_welcome_email

auth_router = KafkaRouter()


@auth_router.subscriber(settings.broker.after_register_topic)
async def after_register(message: dict):
    email = message.get("email")
    await send_welcome_email(email)


