from os import getenv

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

load_dotenv()


class APIConfig(BaseModel):
    prefix: str = "/api"
    person_prefix: str = "/person"


class SRVConfig(BaseModel):
    port: int = 8030
    host: str = "0.0.0.0"
    reload_on_startup: bool = True


class DBConfig(BaseModel):
    url: str = getenv("DATABASE_URL", "")
    echo: bool = False


class LoggingConfig(BaseModel):
    level: str = "INFO"
    format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    datefmt: str = "%Y-%m-%d %H:%M:%S"


class Settings(BaseSettings):
    api: APIConfig = APIConfig()
    srv: SRVConfig = SRVConfig()
    db: DBConfig = DBConfig()
    logging: LoggingConfig = LoggingConfig()


settings = Settings()
