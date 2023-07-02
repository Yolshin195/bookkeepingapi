from .base_reference import BaseReference


class TransactionType(BaseReference):
    __tablename__ = BaseReference.build_table_name("transaction_type")
