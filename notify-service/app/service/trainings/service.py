from core.config import settings
from faststream.kafka import KafkaRouter
from mailing import send_few_trainings_mail_notification

trainings_router = KafkaRouter()


@trainings_router.subscriber(
    settings.broker.training_topic.few_trainings,
    auto_offset_reset="earliest",
    group_id="few_trainings_consumers",
)
async def after_register(message: dict):
    email = message.get("email")

    await send_few_trainings_mail_notification(email)
