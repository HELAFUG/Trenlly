from os import getenv

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

load_dotenv()


class APIGatewayConfig(BaseModel):
    prefix: str = "/trenlly"
    auth: str = "/auth"

    @property
    def token_url(self) -> str:
        return f"{self.prefix}{self.auth}/login"


class SRVConfig(BaseModel):
    port: int = 8000
    host: str = "localhost"


class PersonService(BaseModel):
    url: str = getenv("PERSON_SERVICE_URL", "http://localhost:8030/")

    @property
    def create_person_url(self) -> str:
        return f"{self.url}api/person/"

    @property
    def get_person_url(self) -> str:
        return f"{self.url}api/person/"


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
    person_service: PersonService = PersonService()


class JWTSettings(BaseModel):
    secret_key: str = getenv("JWT_SECRET_KEY", "secret")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60


class Settings(BaseSettings):
    external_services: ExternalServicesConfig = ExternalServicesConfig()
    api_gateway: APIGatewayConfig = APIGatewayConfig()
    srv: SRVConfig = SRVConfig()
    jwt: JWTSettings = JWTSettings()


settings = Settings()
