from typing import Annotated

from core.models import db_helper
from core.schemas.goal import Goal, GoalCreate
from fastapi import APIRouter, Depends, HTTPException
from pydantic import EmailStr
from service.goal import create_goal_service
from sqlalchemy.ext.asyncio import AsyncSession

goal_router = APIRouter(prefix="/goals", tags=["Goals"])


@goal_router.post("/{person_email}", response_model=Goal)
async def create_goal(
    person_email: EmailStr,
    goal_create: GoalCreate,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    new_goal = await create_goal_service(session, person_email, goal_create)
    if new_goal:
        return new_goal
    raise HTTPException(status_code=404, detail="Person not found")
