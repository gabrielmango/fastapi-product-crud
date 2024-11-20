# CRUD FastAPI with JSON Simulated Database

This project is a simple backend API built with **FastAPI** that implements a CRUD (Create, Read, Update, Delete) for products, using a JSON file as a simulated database.

## Features

- **List Products**: Retrieve all registered products.
- **Get Product**: Retrieve details of a specific product by its ID.
- **Create Product**: Add new products to the system.
- **Update Product**: Edit information of an existing product.
- **Delete Product**: Remove a product by its ID.

---

## Technologies Used

- **Python 3.10+**
- **FastAPI**
- **Uvicorn**
- **Pydantic**

---

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/gabrielmango/fastapi-product-crud.git
   cd crud-fastapi-json
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate   # Windows
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   fastapi dev app/main.py
   ```

5. **Access the interactive documentation**:
   - [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Project Structure

```plaintext
crud_fastapi/
│
├── app/
│   ├── __init__.py         # Initialization file
│   ├── main.py             # Main API routes
│   ├── database.py         # JSON file management
│   ├── models.py           # Data models (Pydantic)
│   ├── schemas.py          # Data input/output schemas
│   └── crud.py             # CRUD operations
│
├── data/
│   └── products.json       # "Database" JSON file
│
├── requirements.txt        # Dependency list
├── venv/                   # Virtual environment
└── README.md               # Project documentation
```

---

## Endpoint Examples

1. **List all products**  
   **GET** `/products/`

2. **Get a product by ID**  
   **GET** `/products/{id}`

3. **Create a new product**  
   **POST** `/products/`  
   **Example JSON**:
   ```json
   {
       "name": "Smartphone",
       "description": "Smartphone with 128GB of storage",
       "price": 1200.50
   }
   ```

4. **Update an existing product**  
   **PUT** `/products/{id}`  
   **Example JSON**:
   ```json
   {
       "name": "Smartphone Pro",
       "description": "Smartphone with 256GB of storage",
       "price": 1500.99
   }
   ```

5. **Delete a product by ID**  
   **DELETE** `/products/{id}`

---

## Contribution

Feel free to open issues or submit pull requests to improve the project.

---

## License

This project is licensed under the **GNU License**.
```

Let me know if you'd like any further adjustments! 😊