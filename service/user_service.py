from dao import UserDAO
from model import User
from security import verify_password, hash_password

class UserService:
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao
    
    def add_user(self, username: str, password: str) -> User | None:
        if self.user_exists(username):
            return None
        self.user_dao.add_user(User(username, hash_password(password), False))
        return self.get_user_by_username(username)
    
    def get_all_users(self) -> list[User]:
        return self.user_dao.get_all_users()
    
    def get_user_by_username(self, username: str) -> User | None:
        return self.user_dao.get_user_by_username(username)
    
    def user_exists(self, username: str) -> bool:
        return self.get_user_by_username(username) is not None
    
    def verify_credentials(self, username: str, password: str) -> User | None:
        user = self.get_user_by_username(username)
        if user is not None and verify_password(user.password_hash, password):
            return user
    
    def update_user_password(self, username: str, password: str):
        user = self.get_user_by_username(username)
        if user is not None:
            self.user_dao.update_user(User(username, hash_password(password), user.is_admin))
    
    def toggle_user_admin_status(self, username: str):
        user = self.get_user_by_username(username)
        if user is not None:
            self.user_dao.update_user(User(username, user.password_hash, not user.is_admin))
    
    def delete_user_account(self, username):
        self.user_dao.delete_user(username)

user_service = UserService(UserDAO())