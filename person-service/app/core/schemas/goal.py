import datetime

from pydantic import BaseModel


class GoalBase(BaseModel):
    name: str
    description: str
    deadline_day: str


class GoalCreate(GoalBase):
    pass


class GoalUpdate(GoalBase):
    completed_at: datetime.datetime | None = None
