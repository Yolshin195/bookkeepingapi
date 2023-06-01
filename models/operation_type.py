from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship
from models.base_reference import BaseReference

if TYPE_CHECKING:
    from models import Operation


class OperationType(BaseReference):
    __tablename__ = BaseReference.build_table_name("operation_type")

    operation: Mapped[list["Operation"]] = relationship(
        back_populates="type", cascade="all, delete-orphan"
    )
