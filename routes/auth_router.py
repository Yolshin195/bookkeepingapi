from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

import db
from config import ACCESS_TOKEN_EXPIRE_MINUTES
from models import User
from models.auth import Token
from models.auth.telegram_login_form import TelegramLoginModel
from services.auth import authenticate_user, create_access_token
from services.auth.auth_service import get_current_super_user, get_user, is_super_user

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/token", response_model=Token)
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        session=Depends(db.get_db)
):
    user = authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@auth_router.post("/telegram", response_model=Token)
async def telegram_login_for_access_token(
        form_data: TelegramLoginModel,
        superuser=Depends(get_current_super_user),
        session=Depends(db.get_db)):
    user: User = get_user(session, form_data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
