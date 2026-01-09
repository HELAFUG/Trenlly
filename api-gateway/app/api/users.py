

from core.config import settings
from core.schemas.user import UserCreate
from fastapi import APIRouter
from service.external.auth import proxy_auth_login, proxy_auth_register

users_router = APIRouter(prefix=settings.api_gateway.auth)


@users_router.post("/register")
async def register_user(user: UserCreate):
    return await proxy_auth_register(user)


@users_router.post("/login")
async def login_user(user: UserCreate):
    return await proxy_auth_login(user)
