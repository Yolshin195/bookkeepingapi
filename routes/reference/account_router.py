from fastapi import APIRouter, Depends

from models.DTO.reference_model import ReferenceModel
from services.category_service import CategoryService

account_router = APIRouter(prefix="/account", tags=["reference"])


@account_router.get("/all")
def get_all(skip: int = 0, limit: int = 100, category_service: CategoryService = Depends()) -> list[ReferenceModel]:
    return category_service.find_all(skip, limit)
