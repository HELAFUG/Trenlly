from typing import Optional

from core.models import Training
from core.schemas.training import TrainingCreate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from .person import get_person


async def create_training(
    session: AsyncSession, person_email: str, training_data: TrainingCreate
) -> Optional[Training]:
    person = await get_person(session, person_email)
    if not person:
        return None
    training = Training(**training_data.model_dump(), person=person)
    session.add(training)
    await session.commit()
    await session.refresh(training)
    return training


async def get_trainings(
    session: AsyncSession, person_email: str
) -> Optional[list[Training]]:
    person = await get_person(session, person_email)
    if not person:
        return
    trainings = await session.execute(
        select(Training)
        .options(joinedload(Training.person))
        .where(Training.person_id == person.id)
    )
    return list(trainings.scalars().all())
