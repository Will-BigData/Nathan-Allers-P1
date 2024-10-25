from model import User
from util import handle_with_message
from getpass import getpass
from log import logger
from service import user_service

@handle_with_message(KeyboardInterrupt, "Cancelling login attempt...")
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

def login() -> User | None:
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

@handle_with_message(KeyboardInterrupt, "Cancelling registration attempt...")
def try_register() -> User | None:
    username = input("Username: ")
    while user_service.user_exists(username):
        print("That username is taken, please enter a different one.")
        username = input("Username: ")
    
    password = getpass()
    password_again = getpass("Re-enter password: ")
    while password != password_again:
        print("Password does not match! Try again.")
        password = getpass()
        password_again = getpass("Re-enter password: ")
    
    user = user_service.add_user(username, password)
    if user is None:
        logger.info("Failed registration attempt")
    else:
        logger.info("Successful registration for user: %s", user.username)
    
    return user

def register() -> User | None:
    user = try_register()
    while user is None:
        again = input("Registration failed, try again? [y/n]: ")
        match again:
            case 'y':
                user = try_register()
            case 'n':
                break
            case _:
                print("Unknown input.")
    return user