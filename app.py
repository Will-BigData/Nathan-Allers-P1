from log import logger
from getpass import getpass
from service import UserService
from model import User
from util import handle_with_message, get_user_int

class App:
    def __init__(self):
        self.user_service = UserService()
        self.current_user = None
    
    @handle_with_message(KeyboardInterrupt, "Cancelling login attempt...")
    def try_login(self) -> User | None:
        username = input("Username: ")
        password = getpass()
        user = self.user_service.verify_credentials(username, password)
        if user is None:
            print("Invalid username or password")
            logger.info("Failed login attempt against user: %s", username)
        else:
            logger.info("Successful login for user: %s", username)
        return user

    def login(self):
        self.current_user = self.try_login()
        while self.current_user is None:
            again = input("Login failed, try again? [y/n]: ").lower()[0]
            match again:
                case 'y':
                    self.current_user = self.try_login()
                case 'n':
                    break
                case _:
                    print("Unknown input.")
    
    @handle_with_message(KeyboardInterrupt, "Cancelling registration attempt...")
    def try_register(self) -> User | None:
        username = input("Username: ")
        while self.user_service.user_exists(username):
            print("That username is taken, please enter a different one.")
            username = input("Username: ")
        
        password = getpass()
        password_again = getpass("Re-enter password: ")
        while password != password_again:
            print("Password does not match! Try again.")
            password = getpass()
            password_again = getpass("Re-enter password: ")
        
        user = self.user_service.add_user(username, password)
        if user is None:
            logger.info("Failed registration attempt")
        else:
            logger.info("Successful registration for user: %s", user.username)
        
        return user
    
    def register(self):
        self.current_user = self.try_register()
        while self.current_user is None:
            again = input("Registration failed, try again? [y/n]: ")
            match again:
                case 'y':
                    self.current_user = self.try_register()
                case 'n':
                    break
                case _:
                    print("Unknown input.")

    @handle_with_message(KeyboardInterrupt, "\nKeyboard interrupt (CTRL+C) received, exiting...")
    def main(self):
        while True:
            print("Welcome to the Home Goods Store!\n\nOptions:\n 1. Register as a new user\n 2. Log in as an existing user\n 3. Exit")
            choice = get_user_int("Enter the number of your selection: ")
            match choice:
                case 1:
                    self.register()
                case 2:
                    self.login()
                case 3:
                    print("Thank you for shopping at the Home Goods Store.\nExiting...")
                    break
                case _:
                    print("Unknown selection.")


if __name__ == "__main__":
    app = App()
    app.main()