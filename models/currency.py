from .base_reference import BaseReference


class Currency(BaseReference):
    __tablename__ = BaseReference.build_table_name("currency")
