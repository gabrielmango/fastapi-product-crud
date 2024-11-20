from app.database import read_data, write_data
from app.models import Product

def get_all_products():
    return read_data()

def get_product_by_id(product_id: int):
    products = read_data()
    return next((p for p in products if p["id"] == product_id), None)

def create_product(product_data):
    products = read_data()
    new_id = max(p["id"] for p in products) + 1 if products else 1
    new_product = Product(id=new_id, **product_data.dict())
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

def delete_product(product_id: int):
    products = read_data()
    updated_products = [p for p in products if p["id"] != product_id]
    write_data(updated_products)
    return len(products) != len(updated_products)



if __name__ == '__main__':
    product_id = 4
    is_product_deleted = delete_product(product_id)

    if is_product_deleted:
        print(f"Product with id {product_id} has been deleted.")
    
    product = get_product_by_id(product_id)

    if product:
        print(f"Product data: {product}")
    else:
        print(f"Product with id {product_id} not found.")