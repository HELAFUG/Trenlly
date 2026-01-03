from faststream.kafka import KafkaBroker

from core.config import settings
from service.auth import auth_router

fs_broker = KafkaBroker(bootstrap_servers=settings.broker.bootstrap_servers, acks="all")
fs_broker.include_router(auth_router)
