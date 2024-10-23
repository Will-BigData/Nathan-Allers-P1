from dao import UserDAO
from model import User

class Service:
    def __init__(self):
        self.user_dao = UserDAO()
    
    def add_user(self, user: User):
        if self.user_dao.get_user_by_username(user.username) is not None:
            return False
        self.user_dao.add_user(user)
        return True