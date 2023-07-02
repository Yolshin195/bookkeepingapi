from .base_reference import BaseReference


class Category(BaseReference):
    __tablename__ = BaseReference.build_table_name("category")
