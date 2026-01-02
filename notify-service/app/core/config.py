from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

load_dotenv()


class BrokerConfig(BaseModel):
    bootstrap_servers: str = "localhost:9092"
    after_register_topic: str = "after_registration"


class Settings(BaseSettings):
    broker: BrokerConfig = BrokerConfig()


settings = Settings()
