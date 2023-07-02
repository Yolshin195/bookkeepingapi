
from sqlalchemy.orm import Session
import db
from models import TransactionType
from services import transaction_type_service


def main():
    with db.SessionLocal() as session:
        transaction_type: TransactionType = transaction_type_service.find_by_code(session, 'expense')
        print(transaction_type.code)


if __name__ == "__main__":
    main()
