from pydantic import BaseModel


class TrainingBase(BaseModel):
    group: str
    duration: float
    distance: float
    cardio: bool
    notes: str


class TrainingCreate(TrainingBase):
    pass


class Training(TrainingBase):
    id: int
