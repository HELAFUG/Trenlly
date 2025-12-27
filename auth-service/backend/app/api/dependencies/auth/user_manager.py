from typing import (
    TYPE_CHECKING,
    Annotated,
)

from core.authentication.user_manager import UserManager
from fastapi import Depends

from .users import get_users

if TYPE_CHECKING:
    from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase


async def get_user_manager(
    users_db: Annotated["SQLAlchemyUserDatabase", Depends(get_users)],
):
    yield UserManager(users_db)
