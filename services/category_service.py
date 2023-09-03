from models import Category
from models.DTO.reference_model import ReferenceModel
from repository.category_repository import CategoryRepository
from services.base_service import BaseService


class CategoryService(BaseService):

    def __init__post__(self):
        self.repository = CategoryRepository(self.session, self.current_user)

    def find_by_code(self, code: str) -> Category:
        return self.repository.find_by_code(code)

    def find_all(self, skip: int = 0, limit: int = 100) -> list[ReferenceModel]:
        return [ReferenceModel(id=category.id, code=category.code, name=category.name) for category
                in self.repository.find_all(skip, limit)]
