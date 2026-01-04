from core import fs_broker
from core.config import settings


async def check_user_exists(email: str) -> bool:
    user_exist = await fs_broker.publish(
        topic=settings.faststream_broker.check_user_exists_topic,
        message={"email": email},
    )
    return bool(user_exist)
