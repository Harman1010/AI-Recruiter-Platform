from sqlalchemy import Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from backend.database import Base


class Match(Base):

    __tablename__ = "matches"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    job_id: Mapped[int] = mapped_column(
        ForeignKey("jobs.id"),
        nullable=False
    )

    candidate_id: Mapped[int] = mapped_column(
        ForeignKey("candidates.id"),
        nullable=False
    )

    total_score: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    required_skill_score: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    preferred_skill_score: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    project_score: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    experience_score: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    certification_score: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )