from faststream.kafka import KafkaBroker
from service.auth import auth_router

from core.config import settings

fs_broker = KafkaBroker(
    bootstrap_servers=settings.broker.bootstrap_servers,
)
fs_broker.include_router(auth_router)
