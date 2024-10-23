import os

from pymongo import MongoClient
from config import ConfigManager

class DBManager:
    _db = None
    def get_db():
        if DBManager._db is None:
            db_config = ConfigManager.get_config("database")
            DBManager._db = MongoClient(username=os.environ[db_config["username_env_var"]],
                                            password=os.environ[db_config["password_env_var"]],
                                            authSource=db_config["name"])[db_config["name"]]
        return DBManager._db