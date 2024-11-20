"""Define the product model"""

from pydantic import BaseModel

class Product(BaseModel):
    """Product model"""
    id: int
    name: str
    description: str
    price: float
