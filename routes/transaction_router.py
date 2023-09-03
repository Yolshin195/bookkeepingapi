from typing import Annotated

from fastapi import APIRouter, Depends
from services.transaction_service import TransactionService, ExpenseRegistrationModel

transaction_router = APIRouter(prefix="/transaction", tags=["transaction"])


@transaction_router.post("/expense/add")
async def add_expense_transaction(
        transaction_service: Annotated[TransactionService, Depends()],
        expense_registration_model: ExpenseRegistrationModel,
):
    transaction_service.create_expense_transaction(expense_registration_model)


@transaction_router.get("/all")
async def get_all_transaction(
        transaction_service: Annotated[TransactionService, Depends()],
        skip: int = 0, limit: int = 100
):
    return transaction_service.find_all(skip, limit)
