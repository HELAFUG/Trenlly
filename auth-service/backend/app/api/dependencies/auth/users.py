from typing import TYPE_CHECKING, Annotated

from core.models import User, db_helper
from fastapi import Depends

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_users(
    session: Annotated["AsyncSession", Depends(db_helper.get_session)],
):
    yield User.get_db(session)
