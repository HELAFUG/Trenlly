from typing import Optional

from core.models import Person
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def get_person(session: AsyncSession, email: str) -> Optional[Person]:
    person = await session.execute(select(Person).where(Person.email == email))
    return person.scalar_one_or_none()


async def create_person(session: AsyncSession, person: Person) -> Optional[Person]:
    person_exists = await get_person(session, person.email)
    if person_exists:
        return None
    session.add(person)
    await session.commit()
    await session.refresh(person)
    return person
