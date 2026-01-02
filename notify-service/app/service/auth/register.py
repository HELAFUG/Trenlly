from core import fs_broker
from core.config import settings


@fs_broker.subscriber(settings.broker.after_register_topic)
async def after_register(message: dict):
    email = message.get("email")
    print(f"User {email} registered")
