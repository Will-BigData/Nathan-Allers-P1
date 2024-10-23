from log import logger
from getpass import getpass
from service import UserService
from security import hash_password
from model import User

user_service = UserService()

def try_login() -> User | None:
    username = input("Username: ")
    password = getpass()
    user = user_service.verify_credentials(username, password)
    if user is None:
        print("Invalid username or password")
        logger.info("Failed login attempt against user: %s", username)
    else:
        logger.info("Successful login for user: %s", username)
    return user

def login():
    user = try_login()
    while user is None:
        again = input("Login failed, try again? [y/n]: ").lower()[0]
        match again:
            case 'y':
                user = try_login()
            case 'n':
                break
            case _:
                print("Unknown input.")
    return user

def main():
    user = login()
    if user is not None:
        print("Logged in")
    else:
        print("Login failed")

if __name__ == "__main__":
    main()