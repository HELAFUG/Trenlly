import logging

from core import fs_broker
from core.config import settings

log = logging.getLogger(__name__)


async def after_user_registered(email: str):
    await fs_broker.publish(
        topic=settings.broker.after_register_topic,
        message={"email": email},
    )


async def after_user_logged_in(email: str):
    await fs_broker.publish(
        topic=settings.broker.after_login_topic,
        message={"email": email},
    )
