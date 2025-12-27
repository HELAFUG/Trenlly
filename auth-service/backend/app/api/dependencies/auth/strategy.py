from typing import TYPE_CHECKING, Annotated

from core.config import settings
from fastapi import Depends
from fastapi_users.authentication.strategy.db import DatabaseStrategy

from api.dependencies.auth.access_tokens import get_access_token

if TYPE_CHECKING:
    from core.models import AccessToken
    from fastapi_users.authentication.strategy.db import AccessTokenDatabase


async def get_strategy(
    access_token: Annotated[
        "AccessTokenDatabase[AccessToken]", Depends(get_access_token)
    ],
) -> DatabaseStrategy:
    return DatabaseStrategy(
        database=access_token,
        lifetime_seconds=settings.access_token.lifetime,
    )
