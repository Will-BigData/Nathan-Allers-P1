from dao import UserDAO
from model import User
from security import verify_password, hash_password

class UserService:
    def __init__(self):
        self.user_dao = UserDAO()
    
    def add_user(self, username: str, password: str) -> User | None:
        if self.user_exists(username):
            return None
        self.user_dao.add_user(User(username, hash_password(password), False))
        return self.get_user_by_username(username)
    
    def get_user_by_username(self, username: str) -> User | None:
        return self.user_dao.get_user_by_username(username)
    
    def user_exists(self, username: str) -> bool:
        return self.get_user_by_username(username) is not None
    
    def verify_credentials(self, username: str, password: str) -> User | None:
        user = self.get_user_by_username(username)
        if user is not None and verify_password(user.password_hash, password):
            return user