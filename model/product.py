class Product:
    def __init__(self, name: str, price: float, tags: list[str], stock: int, _id=None):
        self.name = name
        self.price = price
        self.tags = tags
        self.stock = stock
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, value):
        self._price = value
    
    @property
    def tags(self) -> list[str]:
        return self._tags
    
    @tags.setter
    def tags(self, value):
        self._tags = value
    
    @property
    def stock(self) -> int:
        return self._stock
    
    @stock.setter
    def stock(self, value):
        self._stock = value
    
    def get_document_mapping(self):
        return {
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "tags": self.tags
        }

def print_product_table(products: list[Product]):
    name_col_width = 20
    price_col_width = 8
    stock_col_width = 5
    tags_col_width = 20
    name_heading = f"{"Name":<{name_col_width}}"
    price_heading = f"{"Price":<{price_col_width}}"
    stock_heading = f"{"Stock":<{stock_col_width}}"
    tags_heading = f"{"Tags":<{tags_col_width}}"
    divider = " | "
    headings = name_heading + divider + price_heading + divider + stock_heading + divider + tags_heading

    print(headings)
    print('-' * len(headings))

    for product in products:
        print(f"{product.name:<{name_col_width}}{divider}${product.price:<{price_col_width-1}.2f}{divider}{product.stock:<{stock_col_width}}{divider}", end='')
        for num, tag in enumerate(product.tags, start=1):
            print(tag, end='')
            if num < len(product.tags):
                print(", ", end='')
        print()