from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session
import db
from services.auth import get_current_active_user
from models import User


class BaseService:
    def __init__(self,
                 session: Annotated[Session, Depends(db.get_db)],
                 current_user: Annotated[User, Depends(get_current_active_user)]):
        self.session: Session = session
        self.current_user: User = current_user
