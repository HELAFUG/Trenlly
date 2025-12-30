from contextlib import asynccontextmanager

import uvicorn
from api import api_router
from core import fs_broker
from core.config import settings
from core.models import db_helper
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    await fs_broker.start()
    yield
    await fs_broker.stop()
    await db_helper.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.srv.host,
        port=settings.srv.port,
        reload=True,
    )
