from core.config import settings
from fastapi import APIRouter

from .users import users_router

api_router = APIRouter(prefix=settings.api_gateway.prefix)
api_router.include_router(users_router)
