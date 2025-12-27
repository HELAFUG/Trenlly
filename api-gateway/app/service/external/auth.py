from aiohttp import ClientSession
from core.config import settings
from core.schemas.user import UserCreate


async def proxy_auth_register(user: UserCreate):
    async with ClientSession() as session:
        async with session.post(
            url=settings.external_services.user_service.register_url,
            json=user.model_dump(exclude_unset=True),
        ) as response:
            return await response.json()


async def proxy_auth_login(user: UserCreate):
    async with ClientSession() as session:
        async with session.post(
            url=settings.external_services.user_service.login_url,
            json=user.model_dump(exclude_unset=True),
        ) as response:
            return await response.json()
