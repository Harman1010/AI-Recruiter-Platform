from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from backend.database import Base


class Job(Base):

    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(primary_key=True,index=True)

    title: Mapped[str] = mapped_column(String,nullable=False)

    description: Mapped[str] = mapped_column(Text,nullable=False)

    jd_file_path: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )