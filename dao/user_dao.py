from database import DBManager

class UserDAO:
    def __init__(self):
        self.users = DBManager.get_db().users
    def get_user_by_username(self, username: str):
        return self.users.find_one({"username": username})
    def add_user(self, user: dict):
        return self.users.insert_one(user)