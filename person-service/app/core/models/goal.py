import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .person import Person


class Goal(Base):
    person_id: Mapped[int] = mapped_column(
        ForeignKey("persons.id", ondelete="CASCADE"), nullable=False
    )
    person: Mapped["Person"] = relationship(back_populates="goals")
    description: Mapped[str] = mapped_column(index=True, unique=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.utcnow()
    )
    completed_at: Mapped[datetime.datetime | None] = mapped_column(default=None)
