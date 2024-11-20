from database import read_data, write_data
from models import Product

def get_all_products():
    return read_data()

def get_product_by_id(product_id: int):
    products = read_data()
    return next((p for p in products if p["id"] == product_id), None)

def create_product(product_data):
    products = read_data()
    new_id = max(p["id"] for p in products) + 1 if products else 1
    new_product = Product(id=new_id, **product_data)
    products.append(new_product.dict())
    write_data(products)
    return new_product


if __name__ == '__main__':

    new_product_data = {"name": "New Product", "price": 9.99, "description": "New Product Description"}
    new_product = create_product(new_product_data)
    print("New product:", new_product)

    
