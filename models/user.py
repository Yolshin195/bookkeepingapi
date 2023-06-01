from typing import TYPE_CHECKING

from .base import Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

if TYPE_CHECKING:
    from .operation import Operation


class User(Base):
    __tablename__ = Base.build_table_name("user")

    login: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    username: Mapped[str]
    hash_password: Mapped[str] = mapped_column(nullable=False)

    operation: Mapped[list["Operation"]] = relationship(
        back_populates="owner", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, login={self.login!r}, username={self.username!r})"
