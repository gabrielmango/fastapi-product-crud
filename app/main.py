from fastapi import FastAPI
from app.crud import get_all_products


app = FastAPI()

@app.get("/products/")
def read_products():
    return get_all_products()
