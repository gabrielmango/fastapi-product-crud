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


if __name__ == "__main__":
    data = read_data()
    print("Current products:")
    for product in data:
        print(f"{product['id']}: {product['name']} - ${product['price']}")