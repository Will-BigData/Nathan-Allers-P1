from database import DBManager
from model import User

class UserDAO:
    def __init__(self):
        self.users = DBManager.get_db().users

    def get_user_by_username(self, username: str) -> User | None:
        user = self.users.find_one({"username": username})
        return User(**user) if user is not None else None
    
    def add_user(self, user: User):
        return self.users.insert_one(user.get_document_mapping())