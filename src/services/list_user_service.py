from typing import List

from src.repositories.user_repository import UserRepository
from src.models.user_models import UserModel
from src.config.database import db


class ListUserSerive:

    def __init__(self):
        self._repository = UserRepository(session_factory=db.session)
    
    def list_users(self) -> List[UserModel]:
        return self._list_users()
    
    def _list_users(self) -> List[UserModel]:
        return self._repository.list_users()
