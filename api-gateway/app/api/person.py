from typing import Annotated

from core.schemas.person import PersonCreate
from fastapi import APIRouter, Depends
from service.external.person import proxy_new_person

person_router = APIRouter(prefix="/person")


@person_router.post("")
async def create_person(person_data: Annotated[PersonCreate, Depends()]):
    return await proxy_new_person(person=person_data)
