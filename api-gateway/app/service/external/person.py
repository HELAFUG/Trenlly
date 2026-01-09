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
            json=params,
        ) as response:
            return await response.json()


async def proxy_person_by_email(email: str):
    async with ClientSession() as session:
        async with session.get(
            f"{settings.external_services.person_service.get_person_url}{email}",
        ) as response:
            return await response.json()
