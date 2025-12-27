from typing import TYPE_CHECKING, Annotated

from core.config import settings
from fastapi import Depends
from fastapi_users.authentication.strategy.db import DatabaseStrategy

if TYPE_CHECKING:
    from core.models import AccessToken
    from fastapi_users.authentication.strategy.db import AccessTokenDatabase

    from api.dependencies import get_access_tokens


async def get_strategy(
    access_token: Annotated[
        "AccessTokenDatabase[AccessToken]", Depends(get_access_tokens)
    ],
) -> DatabaseStrategy:
    return DatabaseStrategy(
        database=access_token,
        lifetime_seconds=settings.access_token.lifetime,
    )
