from core.config import settings
from fastapi import APIRouter

from api.auth import router as auth_router

api_router = APIRouter(prefix=settings.api.prefix)

api_router.include_router(auth_router)
