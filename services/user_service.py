from sqlalchemy import select
from sqlalchemy.orm import Session

from models import User


def find_by_login(session: Session, login: str) -> User:
    find_by_code_sql = select(User).where(User.login == login)
    return session.scalar(find_by_code_sql)
