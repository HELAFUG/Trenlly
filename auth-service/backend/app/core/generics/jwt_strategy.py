import time

import jwt
from fastapi_users.authentication.strategy.jwt import JWTStrategy

from core.config import settings
from core.models import User


class JWTStrategyGeneric(JWTStrategy):
    async def write_token(self, user: User) -> str:
        payload = {
            "sub": str(user.id),
            "email": user.email,
            # Optional but nice to have:
            "iat": int(time.time()),
            "exp": int(time.time()) + int(self.lifetime_seconds or 3600),
        }

        return jwt.encode(
            payload,
            settings.jwt_token.secret,
            algorithm=settings.jwt_token.algorithm,
        )
