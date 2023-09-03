from typing import Sequence

from sqlalchemy import select

from models import Category, Currency
from repository.base_repository import BaseRepository


class CurrencyRepository(BaseRepository):
    def find_by_code(self, code: str) -> Currency:
        find_by_code_sql = select(Currency).where(Category.code == code)
        return self.session.scalar(find_by_code_sql)

    def find_all(self, skip: int = 0, limit: int = 100) -> Sequence[Currency]:
        find_all_sql = select(Currency).offset(skip).limit(limit)
        return self.session.scalars(find_all_sql).all()
