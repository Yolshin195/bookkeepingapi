from fastapi import APIRouter

from .account_router import account_router
from .category_router import category_router

reference_router = APIRouter(prefix="/reference")

reference_router.include_router(account_router)
reference_router.include_router(category_router)
