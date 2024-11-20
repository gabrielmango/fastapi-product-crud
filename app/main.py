from fastapi import FastAPI, HTTPException
from app.crud import get_all_products, get_product_by_id


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