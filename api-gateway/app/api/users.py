from typing import Annotated

from core.config import settings
from core.schemas.user import UserCreate
from fastapi import APIRouter, Depends
from service.external.auth import proxy_auth_register

users_router = APIRouter(prefix=settings.api_gateway.auth)


@users_router.post("/register")
async def register_user(user: Annotated[UserCreate, Depends]):
    return await proxy_auth_register(user)
