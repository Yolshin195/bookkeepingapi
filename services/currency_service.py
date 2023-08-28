from sqlalchemy import select

from models import Currency
from services.base_service import BaseService


class CurrencyService(BaseService):
    def find_by_code(self, code: str) -> Currency:
        find_by_code_sql = select(Currency).where(Currency.code == code)
        return self.session.scalar(find_by_code_sql)
