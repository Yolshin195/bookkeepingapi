from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

import db
from exceptions import UserAlreadyExists
from models.user import CreateUserModel, User, CreateUserFromTelegramModel
from services.auth import get_current_active_user
from services.auth.auth_service import get_current_super_user
from services.user_service import create_user, create_telegram_user

user_router = APIRouter(prefix="/user", tags=["user"])


@user_router.post("/create")
async def create_user_handler(create_user_model: CreateUserModel, session: Annotated[Session, Depends(db.get_db)]):
    return create_user(session, create_user_model)


@user_router.post("/create/telegram")
async def create_user_from_telegram(create_user_model: CreateUserFromTelegramModel,
                                    session: Annotated[Session, Depends(db.get_db)],
                                    superuser: User = Depends(get_current_super_user)):
    return create_telegram_user(session, create_user_model, superuser)


@user_router.get("/profile")
async def get_profile(current_user: User = Depends(get_current_active_user)):
    return current_user
