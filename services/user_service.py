from sqlalchemy import select
from sqlalchemy.orm import Session

from exceptions import UserAlreadyExists
from models import User
from models.user import CreateUserModel, CreateUserFromTelegramModel, UserPassword, TelegramUser
from services.auth.password_service import get_password_hash


def create_user(session: Session, create_user_model: CreateUserModel) -> User:
    if find_by_username(session, create_user_model.username):
        raise UserAlreadyExists(f"User with username {create_user_model.username}, already exists!")

    user_password = UserPassword(
        created_by="bookkeeping_api",
        email=create_user_model.email,
        hashed_password=get_password_hash(create_user_model.password)
    )

    new_user = User(
        created_by="bookkeeping_api",
        username=create_user_model.username,
        user_password=user_password
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user


def create_telegram_user(session: Session, create_user_model: CreateUserFromTelegramModel, superuser: User) -> User:
    if find_by_username(session, create_user_model.username):
        raise UserAlreadyExists(f"User with username {create_user_model.username}, already exists!")

    telegram_user = TelegramUser(
        created_by=superuser.username,
        telegram_id=create_user_model.id,
    )

    new_user = User(
        created_by=superuser.username,
        username=create_user_model.username,
        telegram_user=telegram_user,
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user


def find_by_username(session: Session, username: str) -> User:
    find_by_code_sql = select(User).where(User.username == username,
                                          User.deleted_date.is_(None))
    return session.scalar(find_by_code_sql)
