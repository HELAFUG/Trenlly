import logging
from contextlib import asynccontextmanager

import uvicorn
from core.config import settings
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.basicConfig(
        level=settings.logging.level,
        format=settings.logging.format,
        datefmt=settings.logging.datefmt,
    )
    yield


app = FastAPI(lifespan=lifespan)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.srv.host,
        port=settings.srv.port,
        reload=settings.srv.reload_on_startup,
    )
