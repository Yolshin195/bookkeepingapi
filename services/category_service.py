from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Category


def find_by_code(session: Session, code: str) -> Category:
    find_by_code_sql = select(Category).where(Category.code == code)
    return session.scalar(find_by_code_sql)
