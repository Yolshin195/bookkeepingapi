from fastapi import APIRouter, Depends

from models.DTO.reference_model import ReferenceModel
from services.category_service import CategoryService

category_router = APIRouter(prefix="/category", tags=["reference"])


@category_router.get("/all")
async def get_all(skip: int = 0, limit: int = 100, category_service: CategoryService = Depends()) -> list[ReferenceModel]:
    return category_service.find_all(skip, limit)
