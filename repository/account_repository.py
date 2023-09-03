from typing import Sequence

from sqlalchemy import select

from models import Account
from repository.base_repository import BaseRepository


class CategoryRepository(BaseRepository):
    def find_by_code(self, code: str) -> Account:
        find_by_code_sql = select(Account).where(Account.code == code)
        return self.session.scalar(find_by_code_sql)

    def find_all(self, skip: int = 0, limit: int = 100) -> Sequence[Account]:
        find_all_sql = select(Account).offset(skip).limit(limit)
        return self.session.scalars(find_all_sql).all()
