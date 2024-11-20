"""Defines schemas for data input/output"""

from pydantic import BaseModel


class ProductCreate(BaseModel):
    """Create a new product."""

    name: str
    description: str
    price: float
