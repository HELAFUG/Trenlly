from os import getenv

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

load_dotenv()


class DBConfig(BaseModel):
    url: str = getenv("DB_URL", "sqlite:///db.sqlite")
    echo: bool = False
    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class APIConfig(BaseModel):
    prefix: str = "/api"
    auth: str = "/auth"

    @property
    def token_url(self) -> str:
        return f"{self.prefix}{self.auth}/login"


class SRVConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8010


class AccessToken(BaseModel):
    reset_password_token_secret: str = getenv("RESET_PASSWORD_TOKEN_SECRET", "secret")
    verification_token_secret: str = getenv("VERIFICATION_TOKEN_SECRET", "secret")
    lifetime: int = 3600


class Settings(BaseSettings):
    db: DBConfig = DBConfig()
    api: APIConfig = APIConfig()
    srv: SRVConfig = SRVConfig()
    access_token: AccessToken = AccessToken()


settings = Settings()
