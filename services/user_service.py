from sqlalchemy import select
from sqlalchemy.orm import Session

from exceptions import UserAlreadyExists
from models import User
from models.user import CreateUserModel
from services.auth.password_service import get_password_hash


def create_user(session: Session, create_user_model: CreateUserModel) -> User:
    if find_by_username(session, create_user_model.username):
        raise UserAlreadyExists(f"User with username {create_user_model.username}, already exists!")

    new_user = User(
        created_by="system",
        username=create_user_model.username,
        email=create_user_model.email,
        hashed_password=get_password_hash(create_user_model.password)
    )

    session.add(new_user)

    return new_user


def find_by_username(session: Session, username: str) -> User:
    find_by_code_sql = select(User).where(User.username == username,
                                          User.deleted_date.is_(None))
    return session.scalar(find_by_code_sql)
