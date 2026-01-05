from typing import Annotated

from core.models import db_helper
from core.schemas.training import Training, TrainingCreate
from fastapi import APIRouter, Depends, HTTPException, Path
from pydantic import EmailStr
from service.training import create_training_service
from sqlalchemy.ext.asyncio import AsyncSession

training_router = APIRouter(prefix="/training")


@training_router.post("/{person_email}", response_model=Training)
async def create_training(
    training_data: TrainingCreate,
    person_email: Annotated[EmailStr, Path(description="Email of the person")],
    session: AsyncSession = Depends(db_helper.session_getter),
):
    new_training = await create_training_service(session, person_email, training_data)
    if not new_training:
        raise HTTPException(status_code=404, detail="Person not found")
    return new_training
