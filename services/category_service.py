from sqlalchemy import select

from models import Category
from models.DTO.reference_model import ReferenceModel
from services.base_service import BaseService


class CategoryService(BaseService):

    def find_by_code(self, code: str) -> Category:
        find_by_code_sql = select(Category).where(Category.code == code)
        return self.session.scalar(find_by_code_sql)

    def find_all(self, skip: int = 0, limit: int = 100) -> list[ReferenceModel]:
        find_all_sql = select(Category).offset(skip).limit(limit)
        result: list[ReferenceModel] = [ReferenceModel(id=category.id, code=category.code, name=category.name) for
                                        category in self.session.scalars(find_all_sql).all()]
        return result
