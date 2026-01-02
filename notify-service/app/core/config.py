from os import getenv

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

load_dotenv()


class BrokerConfig(BaseModel):
    bootstrap_servers: str = "localhost:9092"
    after_register_topic: str = "after_registration"


class AdminConfig(BaseModel):
    email: str = getenv("TRENLLY_ADMIN_EMAIL", "trenlly@gmail.com")


class Settings(BaseSettings):
    broker: BrokerConfig = BrokerConfig()
    admin: AdminConfig = AdminConfig()


settings = Settings()
