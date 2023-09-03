from fastapi import APIRouter, Depends

from models.DTO.reference_model import ReferenceModel
from services.account_service import AccountService

account_router = APIRouter(prefix="/account", tags=["reference"])


@account_router.get("/all")
async def get_all(skip: int = 0, limit: int = 100, account_service: AccountService = Depends()) -> list[ReferenceModel]:
    return account_service.find_all(skip, limit)
