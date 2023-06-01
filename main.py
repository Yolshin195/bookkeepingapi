import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select

from models import Base, User

engine = create_engine("sqlite://", echo=True)


def main():
    Base.metadata.create_all(bind=engine)

    with Session(engine) as session:
        gleb = User(
            login="gleb12",
            email="test@gmail.com",
            username="gleb12",
            hash_password="test",
        )

        gleb.created_by = "admin"
        gleb.id = uuid.uuid4()

        print(type(uuid.uuid4()))
        print(gleb)
        print(gleb.id)
        print(type(gleb.id))

        session.add(gleb)
        session.commit()
        print("COMMIT END!!!!!")
        gleb.id = uuid.uuid4()

        print("START!!!!")
        # for user in session.scalars(stmt):
        #     print(user)


if __name__ == "__main__":
    main()
