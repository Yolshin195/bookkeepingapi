from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from models.base import Base

if TYPE_CHECKING:
    from models.operation_type import OperationType
    from models.user import User


class Operation(Base):
    __tablename__ = Base.build_table_name("operation")

    owner: Mapped["User"] = relationship(back_populates="operation")
    owner_id: Mapped[UUID] = mapped_column(ForeignKey("bookkeeping_api_user.id"))

    type: Mapped["OperationType"] = relationship(back_populates="operation")
    type_id: Mapped[UUID] = mapped_column(ForeignKey("bookkeeping_api_operation_type.id"))

    comment: Mapped[str]
