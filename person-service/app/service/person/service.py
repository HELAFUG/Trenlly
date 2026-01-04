from core.schemas.person import PersonCreate,Person
from repository.person import create_person
from service.kafka import check_user_exists
from core import fs_broker
from core.config import settings


async def create_person_service(person: PersonCreate):
    pass
    