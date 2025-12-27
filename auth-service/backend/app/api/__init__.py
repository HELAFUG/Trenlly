from core.config import settings
from fastapi import APIRouter

api_router = APIRouter(prefix=settings.api.prefix)
