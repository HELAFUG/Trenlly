from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import (
    SQLAlchemyBaseUserTable as SQLAlchemyBaseUserTableGeneric,
)
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from core.models import Base
from core.models.mixins import IDIntPKMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class SQLAlchemyBaseUserTable(SQLAlchemyBaseUserTableGeneric[int]):
    pass


class User(Base, IDIntPKMixin, SQLAlchemyBaseUserTable):  # pyright: ignore[reportIncompatibleVariableOverride]
    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)
