from typing import Optional

from aiohttp import ClientSession, FormData
from core.config import settings
from core.schemas.person import PersonCreate


async def proxy_auth_login(person: PersonCreate) -> Optional[dict]:
    form_data = FormData()
    form_data.add_field("grant_type", "password")
    form_data.add_field("username", person.email)
    form_data.add_field("password", person.password)
    form_data.add_field("scope", "")
    form_data.add_field("client_id", "")
    form_data.add_field("client_secret", "")

    async with ClientSession() as session:
        async with session.post(
            url=settings.external_service.auth_service.login_url,
            data=form_data,
            headers={
                "Accept": "application/json",
            },
        ) as response:
            response.raise_for_status()
            if response.status == 200:
                return await response.json()
            else:
                return None
