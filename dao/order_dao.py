from database import DBManager
from model import Order
from log import logger

class OrderDAO:
    def __init__(self):
        self.orders = DBManager.get_db().orders
    
    def get_all_orders(self) -> list[Order]:
        logger.info("Found all orders")
        return [Order(**order) for order in self.orders.find({})]
    
    def get_orders_by_username(self, username: str) -> list[Order]:
        logger.info("found all orders from user: %s", username)
        return [Order(**order) for order in self.orders.find({"username": username})]
    
    def add_order(self, order: Order):
        logger.info("Inserted order from user: %s", order.username)
        return self.orders.insert_one(order.get_document_mapping())