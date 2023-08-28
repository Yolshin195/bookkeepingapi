from pydantic import BaseModel
from sqlalchemy import String, Boolean

from .base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class User(Base):
    __tablename__ = Base.build_table_name("user")

    username: Mapped[str]
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, login={self.username!r}, username={self.username!r})"


class CreateUserModel(BaseModel):
    username: str
    email: str
    password: str
