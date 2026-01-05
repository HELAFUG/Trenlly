import datetime

from pydantic import BaseModel


class GoalBase(BaseModel):
    name: str
    description: str
    deadline_day: datetime.date


class GoalCreate(GoalBase):
    pass


class Goal(GoalBase):
    id: int
    created_at: datetime.date


class GoalUpdate(GoalBase):
    completed_at: datetime.date | None = None
