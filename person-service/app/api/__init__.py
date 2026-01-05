from core.config import settings
from fastapi import APIRouter

from .motivation import motivation_router
from .person import person_router
from .training import training_router

api_router = APIRouter(prefix=settings.api.prefix)
api_router.include_router(person_router)
api_router.include_router(training_router)
api_router.include_router(motivation_router)
