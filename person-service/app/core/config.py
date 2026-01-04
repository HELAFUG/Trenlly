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
    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


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
