from typing import Optional

from core.models import Training
from core.schemas.training import TrainingCreate
from fastapi import HTTPException
from repository.training import create_training, get_trainings
from sqlalchemy.ext.asyncio import AsyncSession


async def create_training_service(
    session: AsyncSession, person_email: str, training_data: TrainingCreate
) -> Optional[Training]:
    new_training = await create_training(session, person_email, training_data)
    if not new_training:
        raise HTTPException(status_code=404, detail="Person not found")
    return new_training


async def get_trainings_service(
    session: AsyncSession, person_email: str
) -> Optional[list[Training]]:
    trainings = await get_trainings(session, person_email)
    if not trainings:
        raise HTTPException(status_code=404, detail="Person not found")
    return trainings
