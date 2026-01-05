from typing import Optional

from core.models import Goal
from core.schemas.goal import GoalCreate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from repository.person import get_person


async def create_goal(
    session: AsyncSession, person_email: str, goal_data: GoalCreate
) -> Optional[Goal]:
    person = await get_person(session, person_email)
    if not person:
        return None
    new_goal = Goal(**goal_data.model_dump(), person=person)
    session.add(new_goal)
    await session.commit()
    await session.refresh(new_goal)
    return new_goal


async def get_goals(session: AsyncSession, person_email: str) -> Optional[list[Goal]]:
    person = await get_person(session, person_email)
    if not person:
        return None
    goals = await session.execute(
        select(Goal).options(joinedload(Goal.person)).where(Goal.person_id == person.id)
    )
    return list(goals.scalars().all())


async def get_goal(session: AsyncSession, goal_id: int) -> Optional[Goal]:
    goal = await session.execute(select(Goal).where(Goal.id == goal_id))
    return goal.scalars().first()
