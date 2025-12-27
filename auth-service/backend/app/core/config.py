from os import getenv

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

load_dotenv()


class DBConfig(BaseModel):
    url: str = getenv("DATABASE_URL", "sqlite:///db.sqlite")
    echo: bool = False


class APIConfig(BaseModel):
    prefix: str = "/api"


class SRVConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8010


class Settings(BaseSettings):
    db: DBConfig = DBConfig()
    api: APIConfig = APIConfig()
    srv: SRVConfig = SRVConfig()


settings = Settings()
