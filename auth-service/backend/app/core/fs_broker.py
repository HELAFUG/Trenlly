from faststream.kafka import KafkaBroker

from core.config import settings

fs_broker = KafkaBroker(
    bootstrap_servers=settings.broker.bootstrap_servers,
)
