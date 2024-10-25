from dao import OrderDAO
from model import Order
from datetime import datetime

class OrderService:
    def __init__(self, order_dao: OrderDAO):
        self.order_dao = order_dao
    
    def get_all_orders(self) -> list[Order]:
        return self.order_dao.get_all_orders()
    
    def get_orders_by_username(self, username: str) -> list[Order]:
        return self.order_dao.get_orders_by_username(username)
    
    def add_order(self, username: str, product_name: str, quantity: int):
        self.order_dao.add_order(Order(username, product_name, quantity, datetime.now()))

order_service = OrderService(OrderDAO())