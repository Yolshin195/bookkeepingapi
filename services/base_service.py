from typing import TYPE_CHECKING
from sqlalchemy.orm import Session

if TYPE_CHECKING:
    from models import Base


class BaseService:

    def __init__(self, session: Session):
        self.__session: Session = session

    def find_by_id(self):
        pass

    def create(self, entity: Base):
        self.__session.add(entity)

    def update(self):
        pass

    def delete(self):
        pass
