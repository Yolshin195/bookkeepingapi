from fastapi import APIRouter, Depends

import db
from services.transaction_service import ExpenseRegistrationModel, create_expense_transaction, find_all

transaction_router = APIRouter(prefix="/transaction")


@transaction_router.post("/expense/add")
def add_expense_transaction(expense_registration_model: ExpenseRegistrationModel, session=Depends(db.get_db)):
    create_expense_transaction(session, expense_registration_model)


@transaction_router.get("/all")
def get_all_transaction(session=Depends(db.get_db)):
    return find_all(session)
