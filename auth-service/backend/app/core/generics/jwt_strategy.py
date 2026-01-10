from fastapi_users.authentication.strategy.jwt import JWTStrategy

from core.models import User


class JWTStrategyGeneric(JWTStrategy):
    async def write_token(self, user: User) -> str:
        # You can put here whatever you want
        data = {
            "sub": str(user.id),
            "email": user.email,
        }
        return await super().write_token(data)
