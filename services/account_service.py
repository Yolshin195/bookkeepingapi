from sqlalchemy import select

from models import Account
from models.DTO.reference_model import ReferenceModel
from services.base_service import BaseService


class AccountService(BaseService):
    def find_by_code(self, code: str) -> Account:
        find_by_code_sql = select(Account).where(Account.code == code)
        return self.session.scalar(find_by_code_sql)

    def find_all(self, skip: int = 0, limit: int = 100) -> list[ReferenceModel]:
        find_all_sql = select(Account).offset(skip).limit(limit)
        result: list[ReferenceModel] = [ReferenceModel(id=account.id, code=account.code, name=account.name) for
                                        account in self.session.scalars(find_all_sql).all()]
        return result
