from aiohttp import ClientSession
from core.config import settings
from core.schemas.person import PersonCreate


async def proxy_new_person(person: PersonCreate):
    async with ClientSession() as session:
        params = {
            "email": person.email,
            "name": person.name,
            "age": person.age,
            "password": person.password,
        }
        async with session.post(
            f"{settings.external_services.person_service.create_person_url}",
            params=params,
        ) as response:
            return await response.json()
