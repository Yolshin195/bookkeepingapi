from sqlalchemy import select
from sqlalchemy.orm import Session

from models import TransactionType


def find_by_code(session: Session, code: str) -> TransactionType:
    find_by_code_sql = select(TransactionType).where(TransactionType.code == code)
    return session.scalar(find_by_code_sql)



