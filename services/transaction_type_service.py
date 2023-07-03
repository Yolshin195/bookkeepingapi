from sqlalchemy import select
from sqlalchemy.orm import Session

from models import TransactionType


def find_by_code(session: Session, code: str) -> TransactionType:
    find_by_code_sql = select(TransactionType).where(TransactionType.code == code)
    return session.scalar(find_by_code_sql)


def find_all(session: Session, skip: int = 0, limit: int = 100) -> list[TransactionType]:
    find_all_sql = select(TransactionType).offset(skip).limit(limit)
    result: list[TransactionType] = session.scalars(find_all_sql).all()
    return result
