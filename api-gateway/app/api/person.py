from typing import Annotated

from core.schemas.person import PersonCreate
from fastapi import APIRouter, Depends
from pydantic import EmailStr
from service.external.person import proxy_new_person, proxy_person_by_email

person_router = APIRouter(prefix="/person")


@person_router.post("")
async def create_person(person_data: Annotated[PersonCreate, Depends()]):
    return await proxy_new_person(person=person_data)


@person_router.get("/me/{email}")
async def get_person_by_email(email: EmailStr):
    return await proxy_person_by_email(email=email)
