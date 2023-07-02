from typing import TYPE_CHECKING
from decimal import Decimal
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base import Base

if TYPE_CHECKING:
    from .transaction_type import TransactionType
    from .user import User
    from .account import Account
    from .category import Category


class Transaction(Base):
    __tablename__ = Base.build_table_name("transaction")

    owner_id: Mapped[UUID] = mapped_column(ForeignKey("bookkeeping_api_user.id"))
    owner: Mapped["User"] = relationship(foreign_keys=owner_id)

    type_id: Mapped[UUID] = mapped_column(ForeignKey("bookkeeping_api_transaction_type.id"))
    type: Mapped["TransactionType"] = relationship(foreign_keys=type_id)

    # Расход
    expense_account_id: Mapped[UUID] = mapped_column(ForeignKey("bookkeeping_api_account.id"))
    expense_account: Mapped["Account"] = relationship(foreign_keys=expense_account_id)
    expense: Mapped[Decimal] = mapped_column(default=lambda: Decimal("0.0"))

    # Доход
    income_account_id: Mapped[UUID] = mapped_column(ForeignKey("bookkeeping_api_account.id"))
    income_account: Mapped["Account"] = relationship(foreign_keys=income_account_id)
    income: Mapped[Decimal] = mapped_column(default=lambda: Decimal("0.0"))

    category_id: Mapped[UUID] = mapped_column(ForeignKey("bookkeeping_api_category.id"))
    category: Mapped["Category"] = relationship(foreign_keys=category_id)

    comment: Mapped[str]
