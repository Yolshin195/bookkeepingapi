from typing import Annotated

from fastapi import APIRouter, Depends
from services.transaction_service import TransactionService, ExpenseRegistrationModel

transaction_router = APIRouter(prefix="/transaction", tags=["transaction"])


@transaction_router.post("/expense/add")
def add_expense_transaction(
        expense_registration_model: ExpenseRegistrationModel,
        transaction_service: Annotated[TransactionService, Depends()]
):
    transaction_service.create_expense_transaction(expense_registration_model)


@transaction_router.get("/all")
def get_all_transaction(
        transaction_service: Annotated[TransactionService, Depends()]
):
    return transaction_service.find_all()
