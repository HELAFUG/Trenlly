from core.authentication import fastapi_users_app
from core.config import settings
from core.schemas.user import UserCreate, UserRead
from fastapi import APIRouter

from api.dependencies import authentication_backend

router = APIRouter(prefix=settings.api.auth, tags=["Auth"])


router.include_router(
    router=fastapi_users_app.get_register_router(UserRead, UserCreate),
)


router.include_router(router=fastapi_users_app.get_auth_router(authentication_backend))
