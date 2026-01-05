from typing import Optional

from core.models import Person
from core.schemas.person import PersonCreate
from fastapi import HTTPException
from repository.person import create_person, get_person
from sqlalchemy.ext.asyncio import AsyncSession

from service.external.auth_service import proxy_auth_login


async def create_person_service(
    session: AsyncSession, person_data: PersonCreate
) -> Optional[Person]:
    user_exist = await proxy_auth_login(person_data)
    if user_exist:
        new_person = Person(
            email=person_data.email,
            name=person_data.name,
            last_name=person_data.last_name,
            age=person_data.age,
        )
        await create_person(session, new_person)
        return new_person

    raise HTTPException(status_code=400, detail="Bad login credentials")


async def get_person_service(session: AsyncSession, email: str) -> Optional[Person]:
    person = await get_person(session, email)
    if person:
        return person

    raise HTTPException(status_code=404, detail="Person not found")
