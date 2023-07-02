from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime
from uuid import UUID
from uuid import uuid4


class Base(DeclarativeBase):

    id: Mapped["UUID"] = mapped_column(primary_key=True, default=uuid4)

    created_by: Mapped[str]
    created_date: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    last_modified_by: Mapped[str | None]
    last_modified_date: Mapped[datetime | None]

    deleted_by: Mapped[str | None]
    deleted_date: Mapped[datetime | None]

    version: Mapped[int]

    @staticmethod
    def build_table_name(table_name: str) -> str:
        return f'bookkeeping_api_{table_name}'
