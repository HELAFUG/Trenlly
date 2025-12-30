import logging

from core import fs_broker
from core.config import settings

log = logging.getLogger(__name__)


async def after_user_registered(username: str):
    log.info("User signed up %s", username)
    await fs_broker.publish(
        topic=settings.broker.after_register_topic,
        message={"username": username},
    )
