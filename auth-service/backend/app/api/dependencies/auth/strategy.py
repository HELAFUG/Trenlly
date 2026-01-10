from core.config import settings
from core.generics import JWTStrategyGeneric


async def get_strategy() -> JWTStrategyGeneric:
    return JWTStrategyGeneric(
        secret=settings.jwt_token.secret,
        lifetime_seconds=settings.access_token.lifetime,
    )
