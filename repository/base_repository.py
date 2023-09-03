from sqlalchemy.orm import Session

from models import User


class BaseRepository:
    def __init__(self, session: Session, current_user: User):
        self.session: Session = session
        self.current_user = current_user
