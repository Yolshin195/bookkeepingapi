from pydantic import BaseModel
from decimal import Decimal
from sqlalchemy import select

from models import Transaction, User, TransactionType, Account, Category
from services.account_service import AccountService
from services.base_service import BaseService
from services.category_service import CategoryService
from services.transaction_type_service import TransactionTypeService


class ExpenseRegistrationModel(BaseModel):
    expense_account_code: str
    expense: Decimal
    category_code: str
    comment: str | None


class TransactionService(BaseService):
    def __init__post__(self):
        self.category_service = CategoryService(self.session, self.current_user)
        self.transaction_type_service = TransactionTypeService(self.session, self.current_user)
        self.account_service = AccountService(self.session, self.current_user)

    def find_all(self, skip: int = 0, limit: int = 100) -> list[Transaction]:
        find_all_sql = select(Transaction).where(
            Transaction.deleted_date.is_(None),
            Transaction.owner == self.current_user
        ).offset(skip).limit(limit)
        result: list[Transaction] = list(self.session.scalars(find_all_sql).all())
        return result

    def create_expense_transaction(self, expense_registration_data: ExpenseRegistrationModel):
        transaction_type: TransactionType = self.transaction_type_service.find_by_code("expense")
        expense_account: Account = self.account_service.find_by_code(expense_registration_data.expense_account_code)
        expense: Decimal = expense_registration_data.expense
        category: Category = self.category_service.find_by_code(expense_registration_data.category_code)
        comment: str = expense_registration_data.comment

        new_transaction: Transaction = Transaction(
            created_by=self.current_user.username,
            version=1,
            owner=self.current_user,
            type=transaction_type,
            expense_account=expense_account,
            expense=expense,
            category=category,
            comment=comment
        )

        self.session.add(new_transaction)
        self.session.commit()
