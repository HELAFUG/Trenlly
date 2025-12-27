import uvicorn
from api import api_router
from core.config import settings
from fastapi import FastAPI

app = FastAPI()
app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.srv.host,
        port=settings.srv.port,
        reload=True,
    )
