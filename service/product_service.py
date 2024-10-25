from dao import ProductDAO
from model import Product

class ProductService:
    def __init__(self, product_dao: ProductDAO):
        self.product_dao = product_dao

    def get_all_products(self) -> list[Product]:
        return self.product_dao.get_all_products()
    
    def get_product_by_name(self, name: str) -> Product | None:
        return self.product_dao.get_product_by_name(name)
    
    def product_exists(self, name: str) -> bool:
        return self.get_product_by_name(name) is not None
    
    def add_product(self, name: str, price: float, stock: int, tags: list[str]) -> Product | None:
        if self.product_exists(name):
            return None
        self.product_dao.add_product(Product(name, price, tags, stock))
        return self.get_product_by_name
    
    def update_product_stock(self, name: str, stock: int):
        product = self.get_product_by_name(name)
        if product is not None:
            self.product_dao.update_product(Product(name, product.price, product.tags, stock))
    
    def delete_product(self, name: str):
        self.product_dao.delete_product(name)



product_service = ProductService(ProductDAO())