import getpass
from service import Service
from security import hash_password
from model import User

if __name__ == "__main__":
    app_service = Service()
    user = User(input("Username: "), hash_password(getpass.getpass()), False)
    print(app_service.add_user(user))