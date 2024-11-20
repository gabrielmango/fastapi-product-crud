""" Manages reading/writing in the JSON file. """

import json
from pathlib import Path

DB_PATH = Path("data/products.json")

def read_data():
    """ Read the JSON file."""
    if DB_PATH.exists():
        with open(DB_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def write_data(data):
    """ Write the given data to the JSON file. """
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
