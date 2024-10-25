from datetime import datetime
class Order:
    def __init__(self, username: str, productName: str, quantity: int, timestamp: datetime, _id=None):
        self.username = username
        self.product_name = productName
        self.quantity = quantity
        self.timestamp = timestamp
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        self._username = value
    
    @property
    def product_name(self):
        return self._product_name
    
    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    
    @property
    def timestamp(self) -> datetime:
        return self._timestamp
    
    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = value
    
    def get_document_mapping(self):
        return {
            "username": self.username,
            "productName": self.product_name,
            "quantity": self.quantity,
            "timestamp": self.timestamp
        }

def print_order_table(orders: list[Order]):
    username_col_width = 20
    product_name_col_width = 20
    quantity_col_width = 8
    timestamp_col_width = 26
    username_heading = f"{"Username":<{username_col_width}}"
    product_name_heading = f"{"Product Name":<{product_name_col_width}}"
    quantity_heading = f"{"Quantity":<{quantity_col_width}}"
    timestamp_heading = f"{"Timestamp":<{timestamp_col_width}}"
    divider = " | "
    headings = username_heading + divider + product_name_heading + divider + quantity_heading + divider + timestamp_heading

    print(headings)
    print('-' * len(headings))

    for order in orders:
        print(f"{order.username:<{username_col_width}}{divider}{order.product_name:<{product_name_col_width}}{divider}{order.quantity:<{quantity_col_width}}{divider}{order.timestamp}")
        