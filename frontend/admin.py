from model import User, print_user_table, print_product_table, print_order_table
from log import logger
from service import user_service, product_service, order_service
from util import get_user_int, handle_with_message, get_user_float
from getpass import getpass

def list_all_users(admin: User):
    users = user_service.get_all_users()
    print_user_table(users)
    logger.info("Admin %s listed all users", admin.username)

@handle_with_message(KeyboardInterrupt, "\nCancelling password update...")
def change_user_account_password(admin: User):
    username = input("Enter the username for the account to update: ")
    if not user_service.user_exists(username):
        print("That user does not exist.")
        return
    
    password = getpass()
    password_again = getpass("Re-enter password: ")
    while password != password_again:
        print("Password does not match! Try again.")
        password = getpass()
        password_again = getpass("Re-enter password: ")
    
    
    user_service.update_user_password(username, password)
    print("Password updated.")
    logger.info("Admin %s updated the password of user: %s", admin.username, username)

@handle_with_message(KeyboardInterrupt, "\nCancelling admin status toggle...")
def toggle_user_admin_status(admin: User):
    username = input("Enter the username for the account to update: ")
    if not user_service.user_exists(username):
        print("That user does not exist.")
        return
    if username == admin.username:
        print("You can't toggle your own admin status.")
        return
    
    user_service.toggle_user_admin_status(username)
    print("Admin status updated")
    logger.info("Admin %s toggled admin status of user %s", admin.username, username)

@handle_with_message(KeyboardInterrupt, "\nCancelling user account deletion...")
def delete_user_account(admin: User):
    username = input("Enter the username for the account to delete: ")
    if not user_service.user_exists(username):
        print("That user does not exist.")
        return
    if username == admin.username:
        print("You can't delete your own account.")
        return
    
    user_service.delete_user_account(username)
    print("Account deleted.")
    logger.info("Admin %s deleted the account of user: %s", admin.username, username)

def list_all_products(admin: User):
    products = product_service.get_all_products()
    print_product_table(products)
    logger.info("Admin %s listed all products", admin.username)

@handle_with_message(KeyboardInterrupt, "\nCancelling addition of new product...")
def add_new_product(admin: User):
    name = input("Enter a name for the new product: ")
    if product_service.product_exists(name):
        print("A product with that name already exists.")
        return
    price = get_user_float("Enter a price for the product: ", "Price can't be negative.", lambda x: x >= 0.0)
    stock = get_user_int("Enter the available stock for the product: ", "Stock can't be nagative.", lambda x: x >= 0)
    tags = []

    try:
        while True:
            tags.append(input("Enter a tag for the product (CTRL+C to stop adding tags): "))
    except KeyboardInterrupt:
        print("\nFinished addding tags")
    
    product = product_service.add_product(name, price, stock, tags)
    if product is None:
        print("Failed to add product.")
        logger.info("Admin %s failed to add new product with name: %s", admin.username, name)
    else:
        print("Added product.")
        logger.info("Admin %s added new product with name: %s", admin.username, name)

@handle_with_message(KeyboardInterrupt, "\nCanceling deletion of product...")
def delete_product(admin: User):
    name = input("Enter the name of the product to delete: ")
    if not product_service.product_exists(name):
        print("No product exists with that name.")
        return
    
    product_service.delete_product(name)
    print("Product deleted.")
    logger.info("Admin %s deleted product with name: %s", admin.username, name)

def list_all_orders(admin: User):
    orders = order_service.get_all_orders()
    print_order_table(orders)
    logger.info("Admin %s listed all orders", admin.username)

OPTION_FUNCS = [
    list_all_users,
    change_user_account_password,
    toggle_user_admin_status,
    delete_user_account,
    list_all_products,
    add_new_product,
    delete_product,
    list_all_orders
]

OPTION_LISTINGS = [(str(i) + ". " + func.__name__.replace('_', ' ').capitalize(), func) for i, func in enumerate(OPTION_FUNCS, start=1)]

@handle_with_message(KeyboardInterrupt, "\nLogging out...")
def admin_menu(admin: User):
    print(f"Welcome, administrator {admin.username}.")
    while True:
        try:
            print("\nAdministrator Options:")
            for option_listing, _ in OPTION_LISTINGS:
                print(option_listing)
            print()
            option = get_user_int("Enter the number of your choice (CTRL+C to log out): ", "Option not in option list.", lambda x: x > 0 and x <= len(OPTION_LISTINGS))
            print()
            OPTION_LISTINGS[option-1][1](admin)
        except IndexError:
            print("Unknown option.")