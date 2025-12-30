import logging

from fastapi import Request
from fastapi_users import BaseUserManager
from service.kafka import after_user_registered

from core.config import settings
from core.models import User
from core.models.mixins import IDIntPKMixin

log = logging.getLogger(__name__)


class UserManager(IDIntPKMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.access_token.reset_password_token_secret
    verification_token_secret = settings.access_token.verification_token_secret

    async def on_after_register(
        self, user: User, request: Request | None = None
    ) -> None:
        log.info("User signed up %s", user.id)
        await after_user_registered(user.email)
