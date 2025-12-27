from typing import TYPE_CHECKING, Annotated

from core.models import AccessToken, db_helper
from fastapi import Depends

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_access_token(
    session: Annotated["AsyncSession", Depends(db_helper.get_session)],
):
    yield AccessToken.get_db(session)
