from aiohttp import ClientSession, FormData
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
    form_data = FormData()
    form_data.add_field("grant_type", "password")
    form_data.add_field("username", user.email)
    form_data.add_field("password", user.password)
    form_data.add_field("scope", "")
    form_data.add_field("client_id", "")
    form_data.add_field("client_secret", "")

    async with ClientSession() as session:
        async with session.post(
            url=settings.external_services.user_service.login_url,
            data=form_data,
            headers={
                "Accept": "application/json",
            },
        ) as response:
            response.raise_for_status()
            return await response.json()
