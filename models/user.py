from uuid import UUID

from pydantic import BaseModel
from sqlalchemy import String, Boolean, ForeignKey

from .base import Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column


class User(Base):
    __tablename__ = Base.build_table_name("user")

    username: Mapped[str]

    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    user_password_id: Mapped[UUID | None] = mapped_column(ForeignKey("bookkeeping_api_user_password.id"))
    user_password: Mapped["UserPassword"] = relationship(foreign_keys=user_password_id)

    telegram_user_id: Mapped[UUID | None] = mapped_column(ForeignKey("bookkeeping_api_telegram_user.id"))
    telegram_user: Mapped["TelegramUser"] = relationship(foreign_keys=telegram_user_id)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, login={self.username!r}, username={self.username!r})"


class UserPassword(Base):
    __tablename__ = Base.build_table_name("user_password")

    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)


class TelegramUser(Base):
    __tablename__ = Base.build_table_name("telegram_user")

    telegram_id: Mapped[int] = mapped_column(unique=True, index=True, nullable=False)


class CreateUserModel(BaseModel):
    username: str
    email: str
    password: str


class CreateUserFromTelegramModel(BaseModel):
    id: int
    username: str
