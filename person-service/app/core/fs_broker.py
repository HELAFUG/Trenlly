from faststream.kafka import KafkaBroker

from core.config import settings

fs_broker = KafkaBroker(settings.faststream_broker.bootstrap_servers, acks="all")
