from database import DBManager
from model import User
from log import logger

class UserDAO:
    def __init__(self):
        self.users = DBManager.get_db().users

    def get_user_by_username(self, username: str) -> User | None:
        user = self.users.find_one({"username": username})
        if user is None:
            logger.info("Failed to find user with username: %s", username)
        else:
            logger.info("Found user with username: %s", username)
            user = User(**user)
            return user
    
    def add_user(self, user: User):
        logger.info("Inserted user with username: %s", user.username)
        return self.users.insert_one(user.get_document_mapping())
    
    def update_user(self, user: User):
        logger.info("Updated user with username: %s", user.username)
        pass