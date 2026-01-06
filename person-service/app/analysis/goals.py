from datetime import datetime

from core.models import Goal, db_helper
from repository.goal import get_goals_for_analysis


async def overdue_goals_analysis() -> str | None:
    async with db_helper.session_factory() as session:
        goals = await get_goals_for_analysis(session)
        if not goals:
            return None
        overdue_goals: list[Goal] = [
            goal for goal in goals if goal.deadline_day < datetime.now().date()
        ]
        while overdue_goals:
            goal = overdue_goals.pop()
            email = goal.person.email
            return email
