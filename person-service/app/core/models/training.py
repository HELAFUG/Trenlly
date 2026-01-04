from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .person import Person


class Training(Base):
    person_id: Mapped[int] = mapped_column(
        ForeignKey("persons.id", ondelete="CASCADE"),
        nullable=False,
    )
    person: Mapped["Person"] = relationship(back_populates="trainings")
    group: Mapped[str]
    duration: Mapped[float]
    distance: Mapped[float]
    cardio: Mapped[bool]
    notes: Mapped[str]
