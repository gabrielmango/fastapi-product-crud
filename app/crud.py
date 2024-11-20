from database import read_data

def get_all_products():
    return read_data()

if __name__ == '__main__':
    products = get_all_products()
    for product in products:
        print(product)