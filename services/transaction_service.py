from pydantic import BaseModel
from decimal import Decimal

from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Transaction, User, TransactionType, Account, Category
from services import user_service
from services import transaction_type_service
from services import account_service
from services import category_service


class ExpenseRegistrationModel(BaseModel):
    expense_account_code: str
    expense: Decimal
    category_code: str
    comment: str | None


def find_all(session: Session, skip: int = 0, limit: int = 100) -> list[Transaction]:
    find_all_sql = select(Transaction).offset(skip).limit(limit)
    result: list[Transaction] = session.scalars(find_all_sql).all()
    return result


def create_expense_transaction(session: Session, expense_registration_data: ExpenseRegistrationModel):
    owner: User = user_service.find_by_login(session, "admin")
    transaction_type: TransactionType = transaction_type_service.find_by_code(session, "expense")
    expense_account: Account = account_service.find_by_code(session, expense_registration_data.expense_account_code)
    expense: Decimal = expense_registration_data.expense
    category: Category = category_service.find_by_code(session, expense_registration_data.category_code)
    comment: str = expense_registration_data.comment

    new_transaction: Transaction = Transaction(
        created_by=owner.login,
        version=1,
        owner=owner,
        type=transaction_type,
        expense_account=expense_account,
        expense=expense,
        category=category,
        comment=comment
    )

    session.add(new_transaction)
    session.commit()
