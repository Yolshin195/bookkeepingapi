from sqlalchemy import select

from models import TransactionType
from services.base_service import BaseService


class TransactionTypeService(BaseService):
    def find_by_code(self, code: str) -> TransactionType:
        find_by_code_sql = select(TransactionType).where(TransactionType.code == code)
        return self.session.scalar(find_by_code_sql)

    def find_all(self, skip: int = 0, limit: int = 100) -> list[TransactionType]:
        find_all_sql = select(TransactionType).offset(skip).limit(limit)
        result: list[TransactionType] = list(self.session.scalars(find_all_sql).all())
        return result
