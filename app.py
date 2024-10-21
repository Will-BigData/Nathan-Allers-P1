import os

from pymongo import MongoClient
from config import ConfigManager

db_config = ConfigManager.get_config("database")
client = MongoClient(username=os.environ[db_config["username_env_var"]],
                     password=os.environ[db_config["password_env_var"]],
                     authSource=db_config["name"])

db = client.project1

users = db.users

for user in users.find({}):
    print(user)