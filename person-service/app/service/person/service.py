from typing import Optional

from core.models import Person
from core.schemas.person import Person as PersonSchema
from core.schemas.person import PersonCreate
from repository.person import create_person
from sqlalchemy.ext.asyncio import AsyncSession

from service.external.auth_service import proxy_auth_login


async def create_person_service(
    session: AsyncSession, person_data: PersonCreate
) -> Optional[Person]:
    user_exist = await proxy_auth_login(person_data)
    if user_exist:
        new_person = Person(**person_data.model_dump())
        await create_person(session, new_person)
        return new_person

    return None
