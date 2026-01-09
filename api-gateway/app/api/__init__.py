from core.config import settings
from fastapi import APIRouter
from .person import person_router
from .users import users_router

api_router = APIRouter(prefix=settings.api_gateway.prefix)
api_router.include_router(users_router)
api_router.include_router(person_router)
