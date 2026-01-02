import logging

from fastapi import Request, Response
from fastapi_users import BaseUserManager

from core.config import settings
from core.models import User
from core.models.mixins import IDIntPKMixin
from service.kafka import after_user_logged_in, after_user_registered

log = logging.getLogger(__name__)


class UserManager(IDIntPKMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.access_token.reset_password_token_secret
    verification_token_secret = settings.access_token.verification_token_secret

    async def on_after_register(
        self, user: User, request: Request | None = None
    ) -> None:
        log.info("User signed up %s", user.id)
        await after_user_registered(user.email)

    async def on_after_login(
        self,
        user: User,
        request: Request | None = None,
        response: Response | None = None,
    ) -> None:
        log.info("User logged in %s", user.id)
        await after_user_logged_in(user.email)
