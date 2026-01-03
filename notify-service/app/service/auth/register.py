from core.config import settings
from faststream.kafka import KafkaRouter
from mailing import send_login_email, send_welcome_email

auth_router = KafkaRouter()


@auth_router.subscriber(
    settings.broker.after_register_topic, auto_offset_reset="earliest"
)
async def after_register(message: dict):
    email = message.get("email")
    await send_welcome_email(email)


@auth_router.subscriber(settings.broker.after_login_topic, auto_offset_reset="earliest")
async def after_login(message: dict):
    email = message.get("email")
    await send_login_email(email)
