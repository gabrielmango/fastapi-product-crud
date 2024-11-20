from fastapi import FastAPI, HTTPException
from app.crud import get_all_products, get_product_by_id, create_product, update_product
from app.schemas import ProductCreate


app = FastAPI()

@app.get("/products/")
def read_products():
    return get_all_products()

@app.get("/products/{product_id}")
def read_product_by_id(product_id: int):
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/products/", response_model=ProductCreate)
def create_new_product(product: ProductCreate):
    return create_product(product)

@app.put("/products/{product_id}", response_model=ProductCreate)
def update_existing_product(product_id: int, product: ProductCreate):
    updated = update_product(product_id, product)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated