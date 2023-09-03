from models import Currency
from models.DTO.reference_model import ReferenceModel
from repository.currency_service import CurrencyRepository
from services.base_service import BaseService


class CurrencyService(BaseService):
    def __init__post__(self):
        self.repository = CurrencyRepository(self.session, self.current_user)

    def find_by_code(self, code: str) -> Currency:
        return self.repository.find_by_code(code)

    def find_all(self, skip: int = 0, limit: int = 100) -> list[ReferenceModel]:
        return [ReferenceModel(id=currency.id, code=currency.code, name=currency.name) for currency
                in self.repository.find_all(skip, limit)]
