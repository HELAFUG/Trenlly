import datetime

from pydantic import BaseModel


class GoalBase(BaseModel):
    name: str
    description: str
    deadline_day: datetime.datetime


class GoalCreate(GoalBase):
    pass


class Goal(GoalBase):
    id: int
    created_at: datetime.datetime


class GoalUpdate(GoalBase):
    completed_at: datetime.datetime | None = None
