from .base import Base

from sqlalchemy.orm import Mapped


class BaseReference(Base):
    __abstract__ = True

    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str]
