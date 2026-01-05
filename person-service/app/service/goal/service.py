from typing import Optional

from core.models.goal import Goal
from core.schemas.goal import GoalCreate
from fastapi import HTTPException
from repository.goal import create_goal
from sqlalchemy.ext.asyncio import AsyncSession


async def create_goal_service(
    session: AsyncSession, person_email: str, goal_create: GoalCreate
) -> Optional[Goal]:
    new_goal = await create_goal(session, person_email, goal_create)
    if new_goal:
        return new_goal

    raise HTTPException(status_code=404, detail="Person not found")
