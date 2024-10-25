from database import DBManager
from model import Product
from log import logger

class ProductDAO:
    def __init__(self):
        self.products = DBManager.get_db().products
    
    def get_all_products(self) -> list[Product]:
        logger.info("Found all products")
        return [Product(**product) for product in self.products.find({})]
    
    def get_product_by_name(self, name: str) -> Product | None:
        product = self.products.find_one({"name": name})
        if product is None:
            logger.info("Failed to find product with name: %s", name)
        else:
            logger.info("Found product with name: %s", name)
            product = Product(**product)
            return product
    
    def add_product(self, product: Product):
        logger.info("Inserted product with name: %s", product.name)
        return self.products.insert_one(product.get_document_mapping())
    
    def update_product(self, product: Product):
        logger.info("Updated product with name: %s", product.name)
        self.products.update_one({"name": product.name}, {"$set": {"price": product.price, "tags": product.tags, "stock": product.stock}})
    
    def delete_product(self, name: str):
        results = self.products.delete_one({"name": name})
        if results.deleted_count == 0:
            logger.info("Failed to delete product with name: %s", name)
        else:
            logger.info("Deleted product with name: %s", name)