from util import handle_with_message, get_user_int
from frontend import login, register, dispatch_user

@handle_with_message(KeyboardInterrupt, "\nKeyboard interrupt (CTRL+C) received, exiting...")
def main():
    while True:
        current_user = None
        print("Welcome to the Home Goods Store!\n\nOptions:\n 1. Create a new account\n 2. Log in to an existing account\n 3. Exit")
        choice = get_user_int("Enter the number of your selection: ")
        match choice:
            case 1:
                current_user = register()
            case 2:
                current_user = login()
            case 3:
                print("Thank you for visiting the Home Goods Store.\nExiting...")
                break
            case _:
                print("Unknown selection.")
        if current_user is not None:
            dispatch_user(current_user)


if __name__ == "__main__":
    main()