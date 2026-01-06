from os import getenv

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

load_dotenv()


class AuthTopics(BaseModel):
    after_register: str = "after_registration"
    after_login: str = "after_login"


class TrainingTopics(BaseModel):
    pass


class GoalTopics(BaseModel):
    overdue: str = "overdue_goals"


class BrokerConfig(BaseModel):
    bootstrap_servers: str = "localhost:9092"
    auth_topic: AuthTopics = AuthTopics()
    training_topic: TrainingTopics = TrainingTopics()
    goal_topic: GoalTopics = GoalTopics()


class AdminConfig(BaseModel):
    email: str = getenv("TRENLLY_ADMIN_EMAIL", "trenlly@gmail.com")


class Settings(BaseSettings):
    broker: BrokerConfig = BrokerConfig()
    admin: AdminConfig = AdminConfig()


settings = Settings()
