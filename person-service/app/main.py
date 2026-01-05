import logging
from contextlib import asynccontextmanager

import uvicorn
from api import api_router
from core.config import settings
from core.models import db_helper
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.basicConfig(
        level=settings.logging.level,
        format=settings.logging.format,
        datefmt=settings.logging.datefmt,
    )
    yield
    await db_helper.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.srv.host,
        port=settings.srv.port,
        reload=settings.srv.reload_on_startup,
    )
