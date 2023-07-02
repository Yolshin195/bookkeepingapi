from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Currency


def find_by_code(session: Session, code: str) -> Currency:
    find_by_code_sql = select(Currency).where(Currency.code == code)
    return session.scalar(find_by_code_sql)
