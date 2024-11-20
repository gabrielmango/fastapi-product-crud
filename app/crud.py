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

def update_product(product_id: int, product_data):
    products = read_data()
    for product in products:
        if product["id"] == product_id:
            product.update(product_data)
            write_data(products)
            return product
    return None



if __name__ == '__main__':

    update_product_data = {
        "name": "Updated Product",
        "price": 19.99,
        "description": "Updated Product Description",
        "id": 3
    }
    
    updated_product = update_product(update_product_data["id"], update_product_data)
    print("Updated product:", updated_product)
