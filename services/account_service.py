from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Account
from models.DTO.reference_model import ReferenceModel


def find_by_code(session: Session, code: str) -> Account:
    find_by_code_sql = select(Account).where(Account.code == code)
    return session.scalar(find_by_code_sql)


def find_all(session: Session, skip: int = 0, limit: int = 100) -> list[ReferenceModel]:
    find_all_sql = select(Account).offset(skip).limit(limit)
    result: list[ReferenceModel] = [ReferenceModel(id=category.id, code=category.code, name=category.name) for category
                                    in session.scalars(find_all_sql).all()]
    return result
