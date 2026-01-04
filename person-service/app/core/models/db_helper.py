from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from core.config import settings


class DBHelper:
    def __init__(self, url: str, echo: bool) -> None:
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )

        self.session_factory = async_sessionmaker(
            bind=self.engine, expire_on_commit=False, autocommit=False, autoflush=False
        )

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session

    async def dispose(self):
        await self.engine.dispose()


db_helper = DBHelper(url=settings.db.url, echo=settings.db.echo)
