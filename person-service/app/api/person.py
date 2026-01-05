from typing import Annotated

from core.config import settings
from core.models import db_helper
from core.schemas.person import Person, PersonCreate
from fastapi import APIRouter, Depends
from service.person import create_person_service
from sqlalchemy.ext.asyncio import AsyncSession

person_router = APIRouter(prefix=settings.api.person_prefix)


@person_router.post("/", response_model=Person)
async def create_person(
    person: Annotated[PersonCreate, Depends()],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    new_person = await create_person_service(
        person_data=person,
        session=session,
    )
    return new_person
