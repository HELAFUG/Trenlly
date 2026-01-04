from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .goal import Goal
    from .training import Training


class Person(Base):
    email: Mapped[str] = mapped_column(index=True, unique=True)
    name: Mapped[str]
    last_name: Mapped[str]
    age: Mapped[int]
    goals: Mapped[list["Goal"]] = relationship(back_populates="person")
    trainings: Mapped[list["Training"]] = relationship(back_populates="person")
