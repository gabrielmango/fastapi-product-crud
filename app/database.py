""" Manages reading/writing in the JSON file. """
import json
from pathlib import Path

DB_PATH = Path("data/products.json")

def read_data():
    """ Read the JSON file and return a dictionary containing information about the products."""
    if DB_PATH.exists():
        with open(DB_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def write_data(data):
    """ Write the given data to the JSON file. """
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    
    data = read_data()
    print("Current products:")
    for product in data:
        print(f"{product['id']}: {product['name']} - ${product['price']}")
    
    new_product = {
        "id": 2,
        "name": "New Product",
        "description": "This is a new product.",
        "price": 9.99
    }
    
    data.append(new_product)
    write_data(data)
    
    print("\nNew product added:")
    print(f"{new_product['id']}: {new_product['name']} - ${new_product['price']}")