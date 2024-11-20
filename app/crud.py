from database import read_data

def get_all_products():
    return read_data()

def get_product_by_id(product_id: int):
    products = read_data()
    return next((p for p in products if p["id"] == product_id), None)

if __name__ == '__main__':
    product_id = 1
    product = get_product_by_id(product_id)
    if product:
        print(f"\nProduct with ID {product_id}:")
        print(f"Name: {product['name']}, Price: {product['price']}")
    
