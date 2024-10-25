from model import User, print_product_table, print_order_table
from util import handle_with_message, get_user_int
from service import product_service, order_service
from log import logger

def list_all_products(user: User):
    products = product_service.get_all_products()
    print_product_table(products)
    logger.info("User %s listed all products", user.username)

@handle_with_message(KeyboardInterrupt, "\nCancelling product order...")
def order_product(user: User):
    name = input("Enter the name of the product to order: ")
    if not product_service.product_exists(name):
        print("No product exists with that name.")
        return
    product = product_service.get_product_by_name(name)
    if product.stock == 0:
        print("Product is out of stock.")
        return
    quantity = get_user_int("Enter the quantity of product to order: ", "Quantity must be greater than zero and at most the available stock of the product.", lambda x: x > 0 and x <= product.stock)
    order_service.add_order(user.username, name, quantity)
    product_service.update_product_stock(product.name, product.stock - quantity)
    print("Order added.")
    logger.info("User %s ordered %d units of product: %s", user.username, quantity, name)


def view_your_orders(user: User):
    orders = order_service.get_orders_by_username(user.username)
    print_order_table(orders)
    logger.info("User %s listed their orders")

OPTION_FUNCS = [
    list_all_products,
    order_product,
    view_your_orders
]

OPTION_LISTINGS = [(str(i) + ". " + func.__name__.replace('_', ' ').capitalize(), func) for i, func in enumerate(OPTION_FUNCS, start=1)]

@handle_with_message(KeyboardInterrupt, "\nLogging out...")
def store_menu(user: User):
    print(f"Welcome, {user.username}.")
    while True:
        try:
            print("\nOptions:")
            for option_listing, _ in OPTION_LISTINGS:
                print(option_listing)
            print()
            option = get_user_int("Enter the number of your choice (CTRL+C to log out): ", "Option not in option list.", lambda x: x > 0 and x <= len(OPTION_LISTINGS))
            print()
            OPTION_LISTINGS[option-1][1](user)
        except IndexError:
            print("Unknown option.")