from fastapi import APIRouter, Depends

import db
from models.DTO.reference_model import ReferenceModel
from services.category_service import find_all

category_router = APIRouter(prefix="/category")


@category_router.get("/all")
def get_all(skip: int = 0, limit: int = 100, session=Depends(db.get_db)) -> list[ReferenceModel]:
    return find_all(session, skip, limit)
