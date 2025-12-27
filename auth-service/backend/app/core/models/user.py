from mmap import ACCESS_COPY
from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import (
    SQLAlchemyBaseUserTable as SQLAlchemyBaseUserTableGeneric,
)
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.orm import Mapped, relationship

from core.models import Base
from core.models.mixins import IDIntPKMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from core.models import AccessToken


class SQLAlchemyBaseUserTable(SQLAlchemyBaseUserTableGeneric[int]):
    pass


class User(Base, IDIntPKMixin, SQLAlchemyBaseUserTable):  # pyright: ignore[reportIncompatibleVariableOverride]
    access_tokens: Mapped[list["AccessToken"]] = relationship(back_populates="user")

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)
