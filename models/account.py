from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_reference import BaseReference

if TYPE_CHECKING:
    from .currency import Currency


class Account(BaseReference):
    __tablename__ = BaseReference.build_table_name("account")

    currency_id: Mapped[UUID] = mapped_column(ForeignKey("bookkeeping_api_currency.id"))
    currency: Mapped["Currency"] = relationship(foreign_keys=currency_id)
