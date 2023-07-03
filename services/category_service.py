from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Category
from models.DTO.reference_model import ReferenceModel


def find_by_code(session: Session, code: str) -> Category:
    find_by_code_sql = select(Category).where(Category.code == code)
    return session.scalar(find_by_code_sql)


def find_all(session: Session, skip: int = 0, limit: int = 100) -> list[ReferenceModel]:
    find_all_sql = select(Category).offset(skip).limit(limit)
    result: list[ReferenceModel] = [ReferenceModel(id=category.id, code=category.code, name=category.name) for category
                                    in session.scalars(find_all_sql).all()]
    return result
