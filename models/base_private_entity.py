from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .user import User


class BasePrivateEntity(Base):
    __abstract__ = True

    owner_id: Mapped[UUID] = mapped_column(ForeignKey("bookkeeping_api_user.id"))
    owner: Mapped["User"] = relationship(foreign_keys=owner_id)
