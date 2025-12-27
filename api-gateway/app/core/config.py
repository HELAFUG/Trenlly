from os import getenv

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

load_dotenv()


class APIGatewayConfig(BaseModel):
    prefix: str = "/trenlly"
    auth: str = "/auth"


class SRVConfig(BaseModel):
    port: int = 8000
    host: str = "localhost"


class UserService(BaseModel):
    url: str = getenv("USER_SERVICE_URL", "http://localhost:8010/")

    @property
    def register_url(self) -> str:
        return f"{self.url}api/auth/register"

    @property
    def login_url(self) -> str:
        return f"{self.url}api/auth/login"


class ExternalServicesConfig(BaseModel):
    user_service: UserService = UserService()


class Settings(BaseSettings):
    external_services: ExternalServicesConfig = ExternalServicesConfig()
    api_gateway: APIGatewayConfig = APIGatewayConfig()
    srv: SRVConfig = SRVConfig()


settings = Settings()
