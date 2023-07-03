from fastapi import APIRouter, Depends

import db
from models.DTO.reference_model import ReferenceModel
from services.account_service import find_all

account_router = APIRouter(prefix="/account")


@account_router.get("/all")
def get_all(skip: int = 0, limit: int = 100, session=Depends(db.get_db)) -> list[ReferenceModel]:
    return find_all(session, skip, limit)
